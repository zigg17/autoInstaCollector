# For recording data from mouse moevement and use
from pynput.mouse import Listener

# For numerical manipulation and saving
import pandas as pd
import numpy as np

# Housekeeping for many functions
import time
import os

# Taking photos of screen
from PIL import ImageGrab

# To move folders and files around
import shutil

# To open instagram and train that
import webbrowser

# For screenshots in clicks
screenshotCountClick = 0

# Ticker for screenshots in scroll so i dont blow up my processor
ticker = 0

# For screenshots in scrolls
screenshotCountScroll = 0

# List to store mouse data
mouse_data = []

# Set the time limit in seconds
time_limit = 60 # Adjust as needed

# Variable to store start time
start_time = time.time()

# Incorporating filepath to save screenshots in relative files
folderName = time.ctime().replace(' ', '')[3:16]
folderName = folderName[0:5] + ':' + folderName[5:]

# For all the click relevant data
clickFolder = "click" + folderName
clickPath = os.path.join(os.getcwd(), clickFolder)
os.makedirs(clickPath, exist_ok=True)

# For all the scroll relevant data
scrollFolder = "scroll" + folderName
scrollPath = os.path.join(os.getcwd(), scrollFolder)
os.makedirs(scrollPath, exist_ok=True)

# Master folder
masterFolder = folderName + "data"
masterPath = os.path.join(os.getcwd(), masterFolder)
os.makedirs(masterFolder, exist_ok=True)

# Just monitoring mouse movement for general datakeeping
def on_move(x, y):
    # Time check
    elapsed_time = time.time() - start_time

    # Append mouse data to the list for move events
    mouse_data.append({'Time': elapsed_time, 'X': x, 'Y': y, 'Action': 'Move', 'DeltaX': np.nan, 
                       'DeltaY': np.nan, 'Screenshot File': ''})
    
    # Exit @ time
    if elapsed_time >= time_limit:
        listener.stop()

# Monitoring clicks, assigns screenshot + mouse loc for each click
def on_click(x, y, button, pressed):
    # Simple house keeping for function
    global screenshotCountClick
    elapsed_time = time.time() - start_time
    action = 'Press' if pressed else 'Release'
    
    # All under press action only, just to limit the amount of times we're incorporating things
    if action == 'Press':
        # Take a screenshot of the entire screen
        screenshotOfClick = ImageGrab.grab()

        # Save the screenshot to a click path
        clickSave = os.path.join(clickPath, f"Cscreenshot{screenshotCountClick}.png")
        screenshotOfClick.save(clickSave)
        screenshotCountClick += 1
        mouse_data.append({'Time': elapsed_time, 'X': x, 'Y': y, 'Action': f'Click-{action}-{button}', 'DeltaX': np.nan, 
                       'DeltaY': np.nan, 'Screenshot File': f"Cscreenshot{screenshotCountClick}.png"})

    # Exit at time limit
    if elapsed_time >= time_limit:
        listener.stop()

# Functon for sceolling, captures change in deltax and deltay on top of coords
def on_scroll(x, y, dx, dy): 
    # Housekeeping
    global ticker
    global screenshotCountScroll
    elapsed_time = time.time() - start_time

    # Append mouse data to the list for scroll events
    if ticker % 62 == 0:
        # Taking screenshot, every couple scrolls to get an idea, may have to adjust
        screenshotOfScroll = ImageGrab.grab()
        scrollSave = os.path.join(scrollPath, f"Rscreenshot{screenshotCountScroll}.png")
        screenshotOfScroll.save(scrollSave)
        
        # Add to data
        mouse_data.append({'Time': elapsed_time, 'X': x, 'Y': y, 'Action': f'Scroll', 'DeltaX': dx, 'DeltaY': dy,
                        'Screenshot File': f"Rscreenshot{screenshotCountScroll}.png"})
        
        # Counter update
        screenshotCountScroll += 1
    else:
        # Recording data if scrolling but no photos
        mouse_data.append({'Time': elapsed_time, 'X': x, 'Y': y, 'Action': f'Scroll', 'DeltaX': dx, 'DeltaY': dy,
                            'Screenshot File': ''})

    # Conditional exit on time check
    if elapsed_time >= time_limit:
        listener.stop()
    
    # To help time photo taking so I dont nuke my CPU
    ticker += 1

# Here we open a safari of a certain specification to ensure a little more consistency in data representation
webbrowser.get("safari").open("instagram.com")

# Create a listener that will call the on_move, on_click, and on_scroll functions for mouse events
with Listener(on_move = on_move, on_click = on_click, on_scroll = on_scroll) as listener:
    listener.join()



# Convert the list to a Pandas DataFrame
df = pd.DataFrame(mouse_data)

# Save the DataFrame to a CSV file
df.to_csv(folderName +':data.csv', index = False)

# This is doing stuff and things
os.makedirs(masterPath, exist_ok=True)
shutil.move(clickPath, masterPath)
shutil.move(scrollPath, masterPath)
shutil.move(folderName +':data.csv', masterPath)