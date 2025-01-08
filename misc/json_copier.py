import os
import json
import shutil

# Define paths
json_file_path = "/Users/jakeziegler/Desktop/instaUI.json"  # Replace with your JSON file path
destination_folder = os.path.join(os.path.expanduser("~"), "Desktop", "ImageExport")
label_studio_media_path = "/Users/jakeziegler/Library/Application Support/label-studio/media/upload/4/"  # Correct path to media

# Create destination folder if it doesn't exist
os.makedirs(destination_folder, exist_ok=True)

# Load the JSON file
with open(json_file_path, 'r') as file:
    data = json.load(file)

# Iterate through JSON and copy images
for item in data:
    image_path = item['data']['img']  # Path in the JSON
    original_path = os.path.join(label_studio_media_path, os.path.basename(image_path))  # Adjust to correct media path

    # Debug: print the paths being checked
    print(f"Looking for: {original_path}")
    
    if os.path.exists(original_path):
        shutil.copy(original_path, destination_folder)
        print(f"Copied: {original_path} -> {destination_folder}")
    else:
        print(f"File not found: {original_path}")

print(f"All images copied to {destination_folder}")
