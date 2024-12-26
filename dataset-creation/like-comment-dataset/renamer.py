import os
from tkinter import Tk
from tkinter.filedialog import askdirectory

def add_suffix_to_files(directory, suffix="RESIZED"):
    """
    Adds a suffix to all files in the specified directory.

    :param directory: The path to the directory containing the files.
    :param suffix: The suffix to add to each file name.
    """
    try:
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            if os.path.isfile(filepath):  # Ensure it's a file
                name, ext = os.path.splitext(filename)  # Split name and extension
                new_name = f"{name}_{suffix}{ext}"  # Add suffix before extension
                new_filepath = os.path.join(directory, new_name)
                os.rename(filepath, new_filepath)  # Rename the file
        print("File renaming completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Use Tkinter to select the directory
    Tk().withdraw()  # Hide the root window
    directory = askdirectory(title="Select Directory")
    
    if directory:
        print(f"Selected directory: {directory}")
        add_suffix_to_files(directory, suffix="RESIZED")
    else:
        print("No directory selected. Exiting.")
