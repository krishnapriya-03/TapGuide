import ctypes
from ctypes import wintypes

user32 = ctypes.windll.user32

MOD_CONTROL = 0x0002
MOD_SHIFT = 0x0004
VK_SPACE = 0x20

def wait_for_hotkey(callback):
    print("Program running... Press CTRL + SHIFT + SPACE")

    # Register hotkey
    if not user32.RegisterHotKey(None, 1, MOD_CONTROL | MOD_SHIFT, VK_SPACE):
        print("Failed to register hotkey")
        return

    try:
        msg = wintypes.MSG()
        while True:
            if user32.GetMessageA(ctypes.byref(msg), None, 0, 0) != 0:
                if msg.message == 0x0312:  # WM_HOTKEY
                    callback()
    finally:
        user32.UnregisterHotKey(None, 1)
