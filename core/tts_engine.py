# core/tts_engine.py
import pyttsx3
import threading

def speak(text):
    """
    Uses pyttsx3 to speak the given text in a separate thread.
    """
    def run():
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

    # Run in a separate thread to avoid blocking the GUI
    thread = threading.Thread(target=run)
    thread.daemon = True
    thread.start()

if __name__ == '__main__':
    speak("This is a test of the text-to-speech engine.")
    # Keep the main thread alive long enough for the speech to finish
    import time
    time.sleep(5)
