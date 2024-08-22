import tkinter as tk
from tkinter import messagebox
import pyttsx3

# Function to convert text to speech
def text_to_speech():
    text = text_entry.get("1.0", tk.END).strip()

    if not text:
        messagebox.showerror("Input Error", "Please enter some text.")
        return

    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Set properties before speaking
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)

    # Convert the text to speech
    engine.say(text)
    engine.runAndWait()

# Function to clear the input
def clear_text():
    text_entry.delete("1.0", tk.END)

# Setting up the GUI
root = tk.Tk()
root.title("Text to Speech Converter")
root.geometry("400x300")

# Label for instructions
tk.Label(root, text="Enter text below and click 'Speak':").pack(pady=10)

# Text entry widget
text_entry = tk.Text(root, height=10, width=40)
text_entry.pack(pady=10)

# Button to convert text to speech
speak_button = tk.Button(root, text="Speak", command=text_to_speech)
speak_button.pack(pady=5)

# Button to clear text
clear_button = tk.Button(root, text="Clear", command=clear_text)
clear_button.pack(pady=5)

# Run the GUI event loop
root.mainloop()
