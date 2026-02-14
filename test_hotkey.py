from system.hotkey_listener import wait_for_hotkey
from system.screenshot import capture_screen
from core.ocr_engine import extract_text_from_image
from core.response_formatter import process_text
from ui.output_window import show_message


def run_tapguide():
    print("Hotkey triggered...")

    # Step 1: Capture screenshot
    image_path = capture_screen()
    print("Screenshot saved:", image_path)

    # Step 2: OCR
    text = extract_text_from_image(image_path)
    print("OCR TEXT:", text)

    if not text or "OCR Error" in text:
        show_message("OCR failed or no readable text detected.")
        return

    # Step 3: Risk + AI
    result = process_text(text)
    print("AI RESULT:", result)

    # Step 4: Show AI explanation in popup
    show_message(result["ai_explanation"])


wait_for_hotkey(run_tapguide)
print("hi")