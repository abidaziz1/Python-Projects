import tkinter as tk
from tkinter import messagebox, filedialog
from textblob import TextBlob
from autocorrect import Speller
import pyttsx3

# Initialize autocorrect
spell = Speller()

# Function to check spelling
def check_spelling():
    input_text = text_entry.get("1.0", tk.END).strip()

    if not input_text:
        messagebox.showerror("Input Error", "Please enter text to check.")
        return

    # Use TextBlob for spelling correction
    blob = TextBlob(input_text)
    corrected_text = str(blob.correct())

    # Display corrected text
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, corrected_text)

    # Highlight spelling errors in original text
    original_words = input_text.split()
    corrected_words = corrected_text.split()

    text_entry.tag_remove("highlight", "1.0", tk.END)
    for i, word in enumerate(original_words):
        if i < len(corrected_words) and word != corrected_words[i]:
            start_index = f"1.0 + {input_text.index(word)}c"
            end_index = f"{start_index} + {len(word)}c"
            text_entry.tag_add("highlight", start_index, end_index)

    text_entry.tag_config("highlight", background="yellow")

# Function to get advanced suggestions using autocorrect
def advanced_suggestions():
    input_text = text_entry.get("1.0", tk.END).strip()

    if not input_text:
        messagebox.showerror("Input Error", "Please enter text to get suggestions.")
        return

    suggestions = spell(input_text)

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, suggestions)

# Function to speak the text
def speak_text():
    text_to_speak = output_text.get("1.0", tk.END).strip()
    if not text_to_speak:
        messagebox.showerror("Speak Error", "No text to speak.")
        return

    engine = pyttsx3.init()
    engine.say(text_to_speak)
    engine.runAndWait()

# Function to save corrected text
def save_corrected_text():
    corrected_text = output_text.get("1.0", tk.END).strip()
    if not corrected_text:
        messagebox.showerror("Save Error", "No corrected text to save.")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(corrected_text)
        messagebox.showinfo("Save Success", "Corrected text saved successfully.")

# Function to clear all text
def clear_text():
    text_entry.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)
    text_entry.tag_remove("highlight", "1.0", tk.END)

# Setting up the GUI
root = tk.Tk()
root.title("Spelling Checker App")

# Text entry for input
tk.Label(root, text="Enter Text:").pack(pady=5)
text_entry = tk.Text(root, height=10, width=50)
text_entry.pack(pady=5)

# Buttons for checking spelling, getting suggestions, and other actions
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

check_button = tk.Button(button_frame, text="Check Spelling", command=check_spelling)
check_button.pack(side=tk.LEFT, padx=5)

suggest_button = tk.Button(button_frame, text="Advanced Suggestions", command=advanced_suggestions)
suggest_button.pack(side=tk.LEFT, padx=5)

speak_button = tk.Button(button_frame, text="Speak Text", command=speak_text)
speak_button.pack(side=tk.LEFT, padx=5)

save_button = tk.Button(button_frame, text="Save Corrected Text", command=save_corrected_text)
save_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(button_frame, text="Clear Text", command=clear_text)
clear_button.pack(side=tk.LEFT, padx=5)

# Output corrected text
tk.Label(root, text="Corrected Text:").pack(pady=5)
output_text = tk.Text(root, height=10, width=50)
output_text.pack(pady=5)

# Start the GUI event loop
root.mainloop()
