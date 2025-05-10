import torch
import torchvision.transforms as transforms
from PIL import Image
import shuzishibie as szsb

# Load the trained model
model = szsb.Net()
model.load_state_dict(torch.load('./model_Mnist.pth'))
model.eval()

# Define the transformation
transform = transforms.Compose([
    transforms.Grayscale(num_output_channels=1),
    transforms.Resize((28, 28)),
    transforms.RandomRotation(10),  # Random rotation
    transforms.RandomAffine(0, shear=10, scale=(0.8,1.2)),  # Random affine transformation
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])

def detect_digit(image_path):
    # Open the image
    image = Image.open(image_path)
    # Apply the transformation
    image = transform(image).unsqueeze(0)
    # Predict the digit
    with torch.no_grad():
        output = model(image)
        _, predicted = torch.max(output.data, 1)
    return predicted.item()

# 测试
if __name__ == '__main__':
    image_path = '无标题.png'
    digit = detect_digit(image_path)
    print(f'The detected digit is: {digit}')