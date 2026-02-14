import pytesseract
from PIL import Image
import re

def extract_text_from_image(capture.png):
    # Open the image file
    image = Image.open(capture.png)

    # Use pytesseract to do OCR on the image
    text = pytesseract.image_to_string(image)

    # Clean up the extracted text
    cleaned_text = re.sub(r'\s+', ' ', text).strip()

    return cleaned_text