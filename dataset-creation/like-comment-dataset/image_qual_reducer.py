import os
import random
from PIL import Image

def reduce_quality(image, output_path, quality):
    """Saves an image with reduced quality."""
    image.save(output_path, quality=quality, optimize=True)
    print(f"Saved with quality {quality}: {output_path}")

def process_images(input_folder, output_folder, min_quality=10, max_quality=90):
    """Processes all images in the input folder, reduces their quality, and saves them to the output folder."""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            try:
                with Image.open(input_path) as img:
                    # Generate a random quality value
                    quality = random.randint(min_quality, max_quality)
                    reduce_quality(img, output_path, quality)
            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    input_folder = input("Enter the path to the folder containing images: ")
    output_folder = input("Enter the path to the folder where altered images will be saved: ")

    # You can adjust the quality range as needed
    min_quality = 50  # Minimum quality (0 is very low; 10 is typical for heavy compression)
    max_quality = 90  # Maximum quality (close to original but slightly compressed)

    process_images(input_folder, output_folder, min_quality, max_quality)
