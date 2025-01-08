import pyautogui
import keyboard
import os
import time
import random
from datetime import datetime

# Define the folder for saving screenshots
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
screenshot_folder = os.path.join(desktop_path, "Screenshots")
os.makedirs(screenshot_folder, exist_ok=True)

print("Press 'esc' to quit.")
print(f"Screenshots will be saved in: {screenshot_folder}")

def capture_screenshot():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"screenshot_{timestamp}.png"
    filepath = os.path.join(screenshot_folder, filename)
    try:
        time.sleep(1.5)  # Optional delay before capturing
        print(f"Attempting to save a screenshot to: {filepath}")
        screenshot = pyautogui.screenshot()  # Capture the screenshot
        screenshot.save(filepath)           # Save the screenshot
        print(f"Screenshot saved successfully: {filepath}")
    except Exception as e:
        print(f"Error while saving screenshot: {e}")

try:
    while True:
        # Simulate pressing the 'down' key
        pyautogui.press('down')
        print("Simulated 'down' key press.")

        # Capture the screenshot after simulating the key press
        capture_screenshot()

        # Wait for a random time between 3 and 20 seconds
        random_delay = round(random.uniform(3, 20), 1)
        print(f"Waiting for {random_delay} seconds before the next action.")
        time.sleep(random_delay)

        # Check if 'esc' is pressed to exit the loop
        if keyboard.is_pressed('esc'):
            print("Exiting...")
            break
except KeyboardInterrupt:
    print("Program terminated.")