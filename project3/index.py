import tkinter as tk

class VoiceAssistant:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Assistant")
        self.root.geometry("300x200")
        self.label = tk.Label(root, text="Press the button and speak", font=("Helvetica", 14))
        self.label.pack(pady=20)
        self.button = tk.Button(root, text="Speak", command=self.on_button_click)
        self.button.pack(pady=20)

    def on_button_click(self):
        pass  # This will trigger the voice assistant function
