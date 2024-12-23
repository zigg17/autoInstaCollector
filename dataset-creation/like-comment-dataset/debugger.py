import pyautogui
import os

# Define the folder path and filename
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
test_file = os.path.join(desktop_path, "test_screenshot.png")

try:
    # Capture a screenshot
    print(f"Attempting to save a screenshot to: {test_file}")
    screenshot = pyautogui.screenshot()  # Capture the screenshot
    screenshot.save(test_file)           # Save the screenshot
    print(f"Test screenshot saved successfully as: {test_file}")
except Exception as e:
    print(f"Error while saving screenshot: {e}")

