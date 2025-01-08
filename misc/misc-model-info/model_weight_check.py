import torch

def model_diagnostics(model_path):
    try:
        # Load the state_dict
        state_dict = torch.load(model_path, map_location=torch.device('cpu'))
        
        # Check if it's a state_dict or a full model
        if isinstance(state_dict, dict) and 'state_dict' in state_dict:
            state_dict = state_dict['state_dict']  # Handle wrapped state_dicts
        
        print("\n===== Model Diagnostics =====")
        
        if isinstance(state_dict, dict):
            print(f"Number of parameters: {len(state_dict.keys())}\n")
            
            # Print all keys
            print("Keys in state_dict:")
            for key in state_dict.keys():
                print(f" - {key}: shape {state_dict[key].shape}")
        else:
            print("The loaded file is not a valid state_dict.")

    except Exception as e:
        print(f"Error loading model: {e}")

# Path to your .pth file
model_path = "/Users/jakeziegler/Desktop/CODING/insta-collector/botsV1/models/reel_interact_V1.pth"
model_diagnostics(model_path)