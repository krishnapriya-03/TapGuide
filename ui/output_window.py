import tkinter as tk
from tkinter import scrolledtext

def show_message(text):
    window = tk.Tk()
    window.title("TapGuide")
    window.geometry("600x500")  # Bigger window for AI content
    window.configure(bg="#1e1e1e")

    # Make the window topmost and lift it to the front
    window.attributes('-topmost', True)
    window.lift()

    # Create a ScrolledText widget
    text_widget = scrolledtext.ScrolledText(
        window,
        wrap="word",  # Wrap lines at word boundaries
        font=("Segoe UI", 11),
        fg="#00ffcc",
        bg="#1e1e1e",
        insertbackground="#00ffcc", # Cursor color
        borderwidth=0,
        highlightthickness=0, # Remove border
        state="normal" # Start in normal state to insert text
    )

    text_widget.insert(tk.END, text)
    text_widget.configure(state="disabled") # Set to disabled (read-only) after inserting text

    text_widget.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

    # Process events to show the window and then destroy it after a delay
    window.update_idletasks()
    window.update()
    window.after(10000, window.destroy) # Destroy after 10 seconds

    # If you want it to stay until closed manually by user, remove the window.after line
    # and you would need a more sophisticated event handling mechanism
    # like running the hotkey listener in a separate thread and managing the Tkinter loop carefully.
    # For now, this makes it pop up and then disappear.
