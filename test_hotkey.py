from system.hotkey_listener import wait_for_hotkey
from system.screenshot import capture_screen
from ui.output_window import show_message

def hello():
    image = capture_screen()
    show_message("Screenshot captured!\n\nSaved as: " + image)

wait_for_hotkey(hello)


