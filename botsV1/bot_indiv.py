import torch
from torchvision import transforms
from PIL import Image
import pyautogui

# Load the model with adjusted state_dict
class CustomModel(torch.nn.Module):
    def __init__(self):
        super(CustomModel, self).__init__()
        # Define backbone to match the saved model structure
        self.backbone = torch.nn.Sequential(
            *list(torch.hub.load('pytorch/vision:v0.10.0', 'resnet18', pretrained=False).children())[:-1]
        )
        self.fc = torch.nn.Linear(512, 8)  # Assuming 8 outputs, replace with actual output dimensions

    def forward(self, x):
        x = self.backbone(x)
        x = x.view(x.size(0), -1)
        x = self.fc(x)
        return x

# Instantiate and load the model
model_path = "path/to/your/model.pth"
model = CustomModel()
state_dict = torch.load(model_path, map_location=torch.device('cpu'))

# Remove 'backbone.' prefix from state_dict keys
adjusted_state_dict = {k.replace("backbone.", ""): v for k, v in state_dict.items()}
model.load_state_dict(adjusted_state_dict)
model.eval()

# Function to preprocess the input image
def preprocess_image(image_path):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),  # Adjust as per your model's requirements
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])  # Adjust mean/std if needed
    ])
    image = Image.open(image_path).convert("RGB")
    return transform(image).unsqueeze(0)  # Add batch dimension

# Load and preprocess the image
image_path = "path/to/your/image.png"
input_image = preprocess_image(image_path)

# Make a prediction
with torch.no_grad():
    output = model(input_image)
    x, y = output[0][:2].tolist()  # Extract x and y coordinates from the first two outputs

# Normalize and move the cursor
screen_width, screen_height = pyautogui.size()
cursor_x = int(x * screen_width)
cursor_y = int(y * screen_height)
pyautogui.moveTo(cursor_x, cursor_y)

print(f"Cursor moved to: ({cursor_x}, {cursor_y})")
