from torchvision.io.image import read_image
from torchvision.models.detection import fasterrcnn_resnet50_fpn_v2, FasterRCNN_ResNet50_FPN_V2_Weights
from torchvision.utils import draw_bounding_boxes
from torchvision.transforms.functional import to_pil_image
from PIL import Image
import os

def convert_png_to_jpg(png_folder, jpg_folder):
    # Ensure the output folder exists
    os.makedirs(jpg_folder, exist_ok=True)

    # List all files in the input folder
    png_files = os.listdir(png_folder)

    for png_file in png_files:
        if png_file.endswith(".png"):
            # Open PNG image
            png_path = os.path.join(png_folder, png_file)
            img = Image.open(png_path)

            # Remove extension and add .jpg
            jpg_file = os.path.splitext(png_file)[0] + ".jpg"
            jpg_path = os.path.join(jpg_folder, jpg_file)

            # Convert and save as JPEG
            img.convert("RGB").save(jpg_path, "JPEG")
            print(f"Converted {png_file} to {jpg_file}")

#convert_png_to_jpg('/Users/jakeziegler/Desktop/x/projects/📵/Jun24:22:05:11data/clickJun24:22:05:11', '/Users/jakeziegler/Desktop/x/projects/📵/empty')

img = read_image("/Users/jakeziegler/Downloads/puzzle-schmidt-1000-pieces-random-galaxy.jpg")

# Step 1: Initialize model with the best available weights
weights = FasterRCNN_ResNet50_FPN_V2_Weights.DEFAULT
model = fasterrcnn_resnet50_fpn_v2(weights=weights, box_score_thresh=0.9)
model.eval()

# Step 2: Initialize the inference transforms
preprocess = weights.transforms()

# Step 3: Apply inference preprocessing transforms
batch = [preprocess(img)]

# Step 4: Use the model and visualize the prediction
prediction = model(batch)[0]
labels = [weights.meta["categories"][i] for i in prediction["labels"]]
box = draw_bounding_boxes(img, boxes=prediction["boxes"],
                          labels=labels,
                          colors="red",
                          width=4, font_size=30)
im = to_pil_image(box.detach())
im.show()
