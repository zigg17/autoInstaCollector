import os
from PIL import Image

def flip_images(input_folder, output_folder, flip_type='horizontal'):
    """
    Flips all images in the input folder and saves them to the output folder.

    Parameters:
        input_folder (str): Path to the folder containing images to flip.
        output_folder (str): Path to the folder where flipped images will be saved.
        flip_type (str): Type of flip ('horizontal' or 'vertical'). Defaults to 'horizontal'.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        
        try:
            with Image.open(input_path) as img:
                if flip_type == 'horizontal':
                    flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)
                elif flip_type == 'vertical':
                    flipped_img = img.transpose(Image.FLIP_TOP_BOTTOM)
                else:
                    print(f"Invalid flip type: {flip_type}. Skipping {filename}.")
                    continue

                output_path = os.path.join(output_folder, filename)
                flipped_img.save(output_path)
                print(f"Flipped and saved: {output_path}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")

# Example usage
input_folder = input("Input folder, NOW: ")
output_folder = input('Output folder, pleashe: ')
flip_type = 'horizontal'  # Change to 'vertical' for vertical flipping

flip_images(input_folder, output_folder, flip_type)
