import tkinter as tk
from tkinter import messagebox

# Caesar Cipher Encryption
def encrypt_message(message, key):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            encrypted_message += chr((ord(char) - shift + key) % 26 + shift)
        else:
            encrypted_message += char
    return encrypted_message

# Caesar Cipher Decryption
def decrypt_message(encrypted_message, key):
    return encrypt_message(encrypted_message, -key)

# Function to handle encryption
def handle_encrypt():
    message = message_entry.get("1.0", tk.END).strip()
    key = key_entry.get().strip()

    if not key.isdigit():
        messagebox.showerror("Invalid Key", "Key must be a number.")
        return

    encrypted_message = encrypt_message(message, int(key))
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, encrypted_message)

# Function to handle decryption
def handle_decrypt():
    encrypted_message = message_entry.get("1.0", tk.END).strip()
    key = key_entry.get().strip()

    if not key.isdigit():
        messagebox.showerror("Invalid Key", "Key must be a number.")
        return

    decrypted_message = decrypt_message(encrypted_message, int(key))
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, decrypted_message)

# Setting up the GUI
root = tk.Tk()
root.title("Secret Message Encryption and Decryption Tool")

# Message Entry
tk.Label(root, text="Enter your message:").pack(pady=10)
message_entry = tk.Text(root, height=5, width=50)
message_entry.pack()

# Key Entry
tk.Label(root, text="Enter the key (number):").pack(pady=10)
key_entry = tk.Entry(root)
key_entry.pack()

# Buttons for Encrypt and Decrypt
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

encrypt_button = tk.Button(button_frame, text="Encrypt", command=handle_encrypt)
encrypt_button.pack(side=tk.LEFT, padx=5)

decrypt_button = tk.Button(button_frame, text="Decrypt", command=handle_decrypt)
decrypt_button.pack(side=tk.LEFT, padx=5)

# Result Display
tk.Label(root, text="Result:").pack(pady=10)
result_text = tk.Text(root, height=5, width=50)
result_text.pack()

# Start the GUI event loop
root.mainloop()
