import torch
from torchvision import models, transforms
from PIL import Image
import pyautogui
import time

# Load ResNet18 and modify the final layer to match the saved model
model = models.resnet18(pretrained=False)
num_features = model.fc.in_features
model.fc = torch.nn.Linear(num_features, 8)  # 8 outputs for 4 sets of coordinates (x1, y1, x2, y2, ...)

# Load the saved state_dict and adapt the keys
model_path = "botsV1/models/reel_interact_V1.pth"
state_dict = torch.load(model_path, map_location=torch.device('cpu'))
adjusted_state_dict = {k.replace("backbone.", ""): v for k, v in state_dict.items()}
model.load_state_dict(adjusted_state_dict)
model.eval()

# Preprocess the input image
def preprocess_image(image_path):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),  # ResNet18 expects 224x224 input
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])  # Match training normalization
    ])
    image = Image.open(image_path).convert("RGB")
    return transform(image).unsqueeze(0)  # Add batch dimension

# Load and preprocess the image
image_path = "/Users/jakeziegler/Desktop/Screenshot 2025-01-07 at 8.27.43 PM.png"
input_image = preprocess_image(image_path)

# Predict and extract coordinates
with torch.no_grad():
    output = model(input_image)
    keypoints = output[0].view(-1, 2).tolist()  # Reshape to 4 pairs of (x, y)

# Extract x-coordinates and compute the average
x_coords = [x for x, y in keypoints if 0 <= x <= 1 and 0 <= y <= 1]
average_x = sum(x_coords) / len(x_coords) if x_coords else 0.5  # Default to 0.5 if no valid x-coordinates

# Move cursor using the average x-coordinate and y-coordinate for each keypoint
screen_width, screen_height = pyautogui.size()
cursor_x = int(average_x * screen_width)
for i, (x, y) in enumerate(keypoints):
    if 0 <= x <= 1 and 0 <= y <= 1:  # Ensure valid coordinates
        cursor_y = int(y * screen_height)
        pyautogui.moveTo(cursor_x, cursor_y)
        pyautogui.click() 
        time.sleep(1)
        print(f"Keypoint {i}: Moved cursor to averaged x={cursor_x}, y={cursor_y}")
    else:
        print(f"Invalid coordinates for keypoint {i}: x={x}, y={y}")
