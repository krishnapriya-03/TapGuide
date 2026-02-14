import pytesseract
from PIL import Image
import re
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\steny\Downloads\tesseract-ocr-w64-setup-5.5.0.20241111.exe"
def extract_text_from_image(image_path):
    # Open the image file
    image = Image.open(image_path)

    # Extract text using OCR
    text = pytesseract.image_to_string(image)

    # Clean up extra whitespace and newlines
    cleaned_text = re.sub(r'\s+', ' ', text).strip()

    return cleaned_text
