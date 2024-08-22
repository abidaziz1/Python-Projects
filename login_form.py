import tkinter as tk
from tkinter import messagebox

# Function to validate login credentials
def validate_login():
    username = username_entry.get()
    password = password_entry.get()

    # Hardcoded credentials for demonstration purposes
    if username == "admin" and password == "password123":
        messagebox.showinfo("Login Successful", f"Welcome {username}!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

# Function to clear the form
def clear_form():
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# Setting up the GUI
root = tk.Tk()
root.title("Login Form")
root.geometry("300x200")

# Username Label and Entry
tk.Label(root, text="Username:").pack(pady=10)
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

# Password Label and Entry
tk.Label(root, text="Password:").pack(pady=10)
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

# Login Button
login_button = tk.Button(root, text="Login", command=validate_login)
login_button.pack(pady=10)

# Clear Button
clear_button = tk.Button(root, text="Clear", command=clear_form)
clear_button.pack(pady=5)

# Run the GUI event loop
root.mainloop()
