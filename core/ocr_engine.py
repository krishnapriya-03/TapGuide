import pytesseract
from PIL import Image
import os
import re
# path to tesseract installed in windows
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
def extract_text_from_image(image_path):
    # Open the image file
    image = Image.open(image_path)

    # Convert to grayscale for potentially better OCR performance
    image = image.convert('L')
    # Resize the image to half its original size for faster processing.
    # This is a common optimization for OCR where very high resolution isn't critical.
    width, height = image.size
    image = image.resize((width // 2, height // 2), Image.LANCZOS)

    # Extract text using OCR
    text = pytesseract.image_to_string(image)

    # Clean up extra whitespace and newlines
    cleaned_text = re.sub(r'\s+', ' ', text).strip()

    return cleaned_text
