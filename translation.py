import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from translate import Translator
from langdetect import detect
import pyttsx3
import speech_recognition as sr

# Function to detect the language of the input text
def detect_language(text):
    return detect(text)

# Function to translate the text
def translate_text():
    source_lang = source_lang_combo.get()
    target_lang = target_lang_combo.get()
    text_to_translate = input_text.get("1.0", tk.END).strip()

    if not text_to_translate:
        messagebox.showerror("Input Error", "Please enter text to translate.")
        return

    try:
        if source_lang == "Detect Language":
            source_lang = detect_language(text_to_translate)

        translator = Translator(from_lang=source_lang, to_lang=target_lang)
        translation = translator.translate(text_to_translate)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translation)
    except Exception as e:
        messagebox.showerror("Translation Error", str(e))

# Function to save the translation to a file
def save_translation():
    translated_text = output_text.get("1.0", tk.END).strip()
    if not translated_text:
        messagebox.showerror("Save Error", "No translated text to save.")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(translated_text)
        messagebox.showinfo("Save Success", "Translation saved successfully.")

# Function to speak the translated text
def speak_translation():
    translated_text = output_text.get("1.0", tk.END).strip()
    if not translated_text:
        messagebox.showerror("Speak Error", "No translated text to speak.")
        return

    engine = pyttsx3.init()
    engine.say(translated_text)
    engine.runAndWait()

# Function to get voice input and translate
def voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        messagebox.showinfo("Voice Input", "Please speak now...")
        audio = recognizer.listen(source)

    try:
        text_to_translate = recognizer.recognize_google(audio)
        input_text.delete("1.0", tk.END)
        input_text.insert(tk.END, text_to_translate)
        translate_text()
    except sr.UnknownValueError:
        messagebox.showerror("Voice Input Error", "Could not understand the audio.")
    except sr.RequestError as e:
        messagebox.showerror("Voice Input Error", f"Could not request results; {e}")

# Setting up the GUI
root = tk.Tk()
root.title("Advanced Language Translator")

# Source Language Selection
tk.Label(root, text="Source Language:").pack(pady=5)
source_lang_combo = ttk.Combobox(root, values=["Detect Language", "en", "fr", "es", "de", "it", "ja", "ko", "zh", "ar", "ru", "pt", "hi"])
source_lang_combo.pack(pady=5)
source_lang_combo.current(0)  # Set default value to 'Detect Language'

# Target Language Selection
tk.Label(root, text="Target Language:").pack(pady=5)
target_lang_combo = ttk.Combobox(root, values=["en", "fr", "es", "de", "it", "ja", "ko", "zh", "ar", "ru", "pt", "hi"])
target_lang_combo.pack(pady=5)
target_lang_combo.current(1)  # Set default value to 'fr' (French)

# Text Entry for Input
tk.Label(root, text="Enter Text:").pack(pady=5)
input_text = tk.Text(root, height=10, width=50)
input_text.pack(pady=5)

# Translate Button
translate_button = tk.Button(root, text="Translate", command=translate_text)
translate_button.pack(pady=10)

# Voice Input Button
voice_button = tk.Button(root, text="Voice Input", command=voice_input)
voice_button.pack(pady=5)

# Output Translated Text
tk.Label(root, text="Translated Text:").pack(pady=5)
output_text = tk.Text(root, height=10, width=50)
output_text.pack(pady=5)

# Save Translation Button
save_button = tk.Button(root, text="Save Translation", command=save_translation)
save_button.pack(pady=5)

# Speak Translation Button
speak_button = tk.Button(root, text="Speak Translation", command=speak_translation)
speak_button.pack(pady=5)

# Start the GUI event loop
root.mainloop()
