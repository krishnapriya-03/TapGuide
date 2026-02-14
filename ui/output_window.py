import tkinter as tk

def show_message(text):
    window = tk.Tk()
    window.title("TapGuide")
    window.geometry("600x500")  # Bigger window for AI content
    window.configure(bg="#1e1e1e")

    label = tk.Label(
        window,
        text=text,
        wraplength=550,
        justify="left",
        font=("Segoe UI", 11),
        fg="#00ffcc",
        bg="#1e1e1e"
    )

    label.pack(padx=20, pady=20)

    window.mainloop()
