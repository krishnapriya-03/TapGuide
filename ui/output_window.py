import tkinter as tk

def show_message(text):
    window = tk.Tk()
    window.title("TapGuide")
    window.geometry("400x200")
    window.configure(bg="#1e1e1e")  # dark background

    label = tk.Label(
        window,
        text=text,
        wraplength=350,
        justify="left",
        font=("Segoe UI", 12, "bold"),
        fg="#00ffcc",      # text color (neon cyan)
        bg="#1e1e1e"       # same as background
    )

    label.pack(padx=20, pady=40)

    window.mainloop()

