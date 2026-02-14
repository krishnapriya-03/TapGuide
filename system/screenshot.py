import mss
import mss.tools

def capture_screen(path="capture.png"):
    with mss.mss() as sct:
        monitor = sct.monitors[1]
        screenshot = sct.grab(monitor)
        mss.tools.to_png(screenshot.rgb, screenshot.size, output=path)

    return path
