import tkinter as tk
from tkinter import scrolledtext, Entry, Button
from core.tts_engine import speak
from core.ai_engine import generate_explanation # Will be modified for conversation
import threading

class OutputWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.overrideredirect(True) # Remove the default title bar
        self.window.geometry("600x550")
        self.window.configure(bg="#1e1e1e")
        self.window.attributes('-topmost', True)

        # Custom Title Bar
        self.title_bar = tk.Frame(self.window, bg="#2a2a2a", relief="raised", bd=0, height=30)
        self.title_bar.pack(expand=0, fill="x")

        self.title_label = tk.Label(self.title_bar, text="TapGuide", bg="#2a2a2a", fg="white")
        self.title_label.pack(side="left", padx=10)

        self.close_button = Button(self.title_bar, text="X", bg="#2a2a2a", fg="white", command=self.hide, relief="flat", activebackground="red")
        self.close_button.pack(side="right")
        
        self.tts_button = Button(self.title_bar, text="Speak", bg="#2a2a2a", fg="white", command=self.speak_text, relief="flat")
        self.tts_button.pack(side="right")

        self.text_widget = scrolledtext.ScrolledText(
            self.window,
            wrap="word",
            font=("Segoe UI", 11),
            fg="#00ffcc",
            bg="#1e1e1e",
            insertbackground="#00ccff",
            borderwidth=0,
            highlightthickness=0,
        )
        self.text_widget.pack(padx=20, pady=(10, 10), fill="both", expand=True)

        self.input_entry = Entry(
            self.window,
            font=("Segoe UI", 11),
            fg="white",
            bg="#2a2a2a",
            insertbackground="white",
            borderwidth=0,
            highlightthickness=1,
            highlightcolor="#00ccff",
            highlightbackground="#1e1e1e"
        )
        self.input_entry.pack(padx=20, pady=(0, 10), fill="x")
        self.input_entry.bind("<Return>", self.submit)


        self.submit_button = Button(
            self.window,
            text="Submit",
            font=("Segoe UI", 10, "bold"),
            fg="#1e1e1e",
            bg="#00ccff",
            activebackground="#00b38f",
            activeforeground="#1e1e1e",
            command=self.submit,
            relief=tk.FLAT,
            padx=10,
            pady=5
        )
        self.submit_button.pack(padx=20, pady=(0, 20))
        
        # Grip for resizing
        self.grip = tk.Label(self.window, bitmap="gray25", bg='#1e1e1e')
        self.grip.place(relx=1.0, rely=1.0, anchor='se')
        self.grip.bind("<B1-Motion>", self.resize_window)


        # Dragging functionality
        self.title_bar.bind("<ButtonPress-1>", self.start_move)
        self.title_bar.bind("<ButtonRelease-1>", self.stop_move)
        self.title_bar.bind("<B1-Motion>", self.do_move)

        self.title_label.bind("<ButtonPress-1>", self.start_move)
        self.title_label.bind("<ButtonRelease-1>", self.stop_move)
        self.title_label.bind("<B1-Motion>", self.do_move)

        self.conversation_history = []
        self.window.withdraw()

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def stop_move(self, event):
        self.x = None
        self.y = None

    def do_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.window.winfo_x() + deltax
        y = self.window.winfo_y() + deltay
        self.window.geometry(f"+{x}+{y}")
        
    def resize_window(self, event):
        x = self.window.winfo_pointerx() - self.window.winfo_rootx()
        y = self.window.winfo_pointery() - self.window.winfo_rooty()
        self.window.geometry(f"{x}x{y}")


    def show_message(self, text, is_initial=True):
        if is_initial:
            self.conversation_history = []
            self.text_widget.configure(state="normal")
            self.text_widget.delete("1.0", tk.END)
            # Initial prompt for the AI is the OCR'd text, but we only show the AI's response.
            self.conversation_history.append({"role": "system", "content": """You are an assistant. Provide a very brief and direct explanation (under 20 words)."""})
            self.conversation_history.append({"role": "user", "content": text})
            # Run AI in a thread to avoid blocking GUI
            self.text_widget.insert(tk.END, "AI Assistant is thinking...\n\n")
            self.text_widget.configure(state="disabled")
            threading.Thread(target=self.get_ai_response, daemon=True).start()
        else:
            self.text_widget.configure(state="normal")
            self.text_widget.insert(tk.END, "AI Assistant:\n" + text + "\n\n")

        self.text_widget.configure(state="disabled")
        self.text_widget.see(tk.END)
        self.window.after(0, self.window.deiconify)
        self.window.lift()
        self.window.focus_force()
        self.input_entry.focus_set()
        
    def speak_text(self):
        text_to_speak = self.text_widget.get("1.0", tk.END)
        last_response = text_to_speak.strip().split("AI Assistant:\n")[-1].split("You:\n")[0]
        speak(last_response)
        
    def hide(self):
        self.window.withdraw()

    def submit(self, event=None):
        user_input = self.input_entry.get()
        if not user_input:
            return

        self.text_widget.configure(state="normal")
        self.text_widget.insert(tk.END, "You:\n" + user_input + "\n\n")
        self.text_widget.configure(state="disabled")
        self.text_widget.see(tk.END)
        
        self.input_entry.delete(0, tk.END)
        self.conversation_history.append({"role": "user", "content": user_input})

        self.text_widget.configure(state="normal")
        self.text_widget.insert(tk.END, "AI Assistant is thinking...\n\n")
        self.text_widget.configure(state="disabled")
        self.text_widget.see(tk.END)

        threading.Thread(target=self.get_ai_response, daemon=True).start()

    def get_ai_response(self):
        # Schedule the removal of the "thinking" message and the insertion of the "AI Assistant:" prefix
        self.window.after(0, self.prepare_for_streaming)
        
        full_response = []
        try:
            for chunk in generate_explanation(self.conversation_history):
                full_response.append(chunk)
                # Schedule each chunk to be inserted in the UI
                self.window.after(0, self.update_ui_with_chunk, chunk)

            # After streaming is complete, schedule the final UI update
            self.window.after(0, self.finalize_response, "".join(full_response))
        except Exception as e:
            # Handle any exceptions that occur during generation
            error_message = f"An error occurred: {str(e)}"
            self.window.after(0, self.update_ui_with_chunk, error_message)
            self.window.after(0, self.finalize_response, "".join(full_response))


    def prepare_for_streaming(self):
        self.text_widget.configure(state="normal")
        # Find and replace "AI Assistant is thinking..."
        pos = self.text_widget.search("AI Assistant is thinking...", "1.0", stopindex=tk.END, backwards=True)
        if pos:
            self.text_widget.delete(pos, f"{pos} + 1 line end")
        self.text_widget.insert(tk.END, "AI Assistant:\n")

    def update_ui_with_chunk(self, chunk):
        self.text_widget.insert(tk.END, chunk)
        self.text_widget.see(tk.END)

    def finalize_response(self, full_response):
        self.text_widget.insert(tk.END, "\n\n")
        self.text_widget.configure(state="disabled")
        self.text_widget.see(tk.END)
        # Avoid adding empty or error responses to history
        if full_response and "AI processing error" not in full_response:
            self.conversation_history.append({"role": "assistant", "content": full_response})


    def run(self):
        self.window.mainloop()

_output_window_instance = None
def get_output_window():
    global _output_window_instance
    if _output_window_instance is None:
        _output_window_instance = OutputWindow()
    return _output_window_instance

def show_message(text):
    win = get_output_window()
    win.show_message(text)
