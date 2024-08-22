import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Function to calculate age
def calculate_age():
    try:
        birth_date = datetime.strptime(dob_entry.get(), "%Y-%m-%d")
        today = datetime.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

        result_label.config(text=f"You are {age} years old.")
    except ValueError:
        messagebox.showerror("Invalid Date", "Please enter a valid date in YYYY-MM-DD format.")

# Function to clear the input
def clear_input():
    dob_entry.delete(0, tk.END)
    result_label.config(text="")

# Setting up the GUI
root = tk.Tk()
root.title("Age Calculator")
root.geometry("300x200")

# Label for Date of Birth
tk.Label(root, text="Enter your Date of Birth (YYYY-MM-DD):").pack(pady=10)

# Entry widget for Date of Birth
dob_entry = tk.Entry(root)
dob_entry.pack(pady=5)

# Button to Calculate Age
calculate_button = tk.Button(root, text="Calculate Age", command=calculate_age)
calculate_button.pack(pady=10)

# Button to Clear the Input
clear_button = tk.Button(root, text="Clear", command=clear_input)
clear_button.pack(pady=5)

# Label to display the result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the GUI event loop
root.mainloop()
