import torch
from torchvision import transforms
from PIL import Image
import pyautogui
import torchvision.models as models

# Load the model
model_path = "/Users/jakeziegler/Desktop/CODING/insta-collector/botsV1/models/reel_interact_V1.pth"
model = models.resnet18()
model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))

# Function to preprocess the input image
def preprocess_image(image_path):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),  # Adjust size as per your model
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])  # Adjust mean/std if needed
    ])
    image = Image.open(image_path).convert("RGB")
    return transform(image).unsqueeze(0)  # Add batch dimension

# Load and preprocess the image
image_path = "/Users/jakeziegler/Desktop/Screenshot 2025-01-05 at 9.44.56 PM.png"
input_image = preprocess_image(image_path)

# Make a prediction
with torch.no_grad():
    output = model(input_image)  # Assuming model returns raw coordinates
    x, y = output[0].tolist()  # Extract coordinates (adjust index if needed)

# Move the cursor to the predicted coordinates
screen_width, screen_height = pyautogui.size()
cursor_x = int(x * screen_width)
cursor_y = int(y * screen_height)
pyautogui.moveTo(cursor_x, cursor_y)

print(f"Cursor moved to: ({cursor_x}, {cursor_y})")
