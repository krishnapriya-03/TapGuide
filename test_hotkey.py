import threading
from system.hotkey_listener import wait_for_hotkey
from system.screenshot import capture_screen
from core.ocr_engine import extract_text_from_image
from ui.output_window import get_output_window

def run_tapguide():
    print("Hotkey triggered...")

    # Get the output window instance
    app = get_output_window()

    # Step 1: Capture screenshot
    image_path = capture_screen()
    print("Screenshot saved:", image_path)

    # Step 2: OCR
    text = extract_text_from_image(image_path)
    print("OCR TEXT:", text)

    if not text or "OCR Error" in text:
        app.show_message("OCR failed or no readable text detected.")
        return

    # Step 3: Show the extracted text in the popup.
    # The OutputWindow will handle getting the initial AI explanation.
    app.show_message(text)


if __name__ == '__main__':
    # Get the single instance of the output window
    app = get_output_window()

    # The hotkey listener needs to run in a separate thread
    # so it doesn't block the Tkinter main loop.
    hotkey_thread = threading.Thread(target=wait_for_hotkey, args=(run_tapguide,), daemon=True)
    hotkey_thread.start()

    print("Hotkey listener started in the background.")
    print("Press the hotkey to trigger the guide.")
    
    # Start the Tkinter main loop in the main thread
    app.run()