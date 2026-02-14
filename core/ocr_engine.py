import pytesseract
from PIL import Image
import os
import re
# path to tesseract installed in windows
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
def extract_text_from_image(image_path):
    # Open the image file
    image = Image.open(image_path)

    # Extract text using OCR
    text = pytesseract.image_to_string(image)

    # Clean up extra whitespace and newlines
    cleaned_text = re.sub(r'\s+', ' ', text).strip()

    return cleaned_text
