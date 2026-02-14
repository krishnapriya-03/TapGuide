import pytesseract
from PIL import Image
import os

# path to tesseract installed in windows
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# pick any random image from folder
image_path = "capture.png"   # change name if needed

if os.path.exists(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    print("\nExtracted Text:\n")
    print(text)
else:
    print("Image not found in folder")
