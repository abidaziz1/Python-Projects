"""
Features:
File Selection:

The select_files() function uses filedialog.askopenfilenames() to allow the user to select multiple files.
The selected files are displayed in a Listbox.
Destination Selection:

The select_destination() function uses filedialog.askdirectory() to let the user choose a destination folder where the files will be copied.
The selected destination is shown on a label.
File Transfer:

The transfer_files() function performs the actual file transfer using shutil.copy().
A Progressbar is updated as files are transferred.
Error handling is in place to catch any issues during the file transfer.
Progress Bar:

The progress bar updates in real-time as files are copied, giving visual feedback to the user.
Status Label:

Provides information about the current state, including the selected destination folder.
"""

import tkinter as tk
from tkinter import filedialog, messagebox
import shutil
import os
from tkinter.ttk import Progressbar

# Initialize the main application window
root = tk.Tk()
root.title("File Transfer")
root.geometry("500x300")

# Global variables
files_to_transfer = []
destination_folder = ""

# Function to select files
def select_files():
    global files_to_transfer
    files = filedialog.askopenfilenames(title="Select Files")
    if files:
        files_to_transfer = list(files)
        file_listbox.delete(0, tk.END)
        for file in files_to_transfer:
            file_listbox.insert(tk.END, os.path.basename(file))

# Function to select destination folder
def select_destination():
    global destination_folder
    destination_folder = filedialog.askdirectory(title="Select Destination Folder")
    if destination_folder:
        destination_label.config(text=f"Destination: {destination_folder}")

# Function to transfer files
def transfer_files():
    if not files_to_transfer:
        messagebox.showwarning("No Files Selected", "Please select files to transfer.")
        return
    
    if not destination_folder:
        messagebox.showwarning("No Destination Selected", "Please select a destination folder.")
        return
    
    progress_bar['maximum'] = len(files_to_transfer)
    progress_bar['value'] = 0

    for i, file in enumerate(files_to_transfer):
        try:
            shutil.copy(file, destination_folder)
            progress_bar['value'] += 1
            root.update_idletasks()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to copy {os.path.basename(file)}. Error: {e}")
            return

    messagebox.showinfo("Transfer Complete", "All files have been transferred successfully.")
    progress_bar['value'] = 0

# Creating the UI components
# File selection
file_label = tk.Label(root, text="Selected Files:")
file_label.pack(pady=10)

file_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, width=50, height=10)
file_listbox.pack(pady=10)

select_files_button = tk.Button(root, text="Select Files", command=select_files)
select_files_button.pack(pady=5)

# Destination selection
destination_label = tk.Label(root, text="Destination: Not Selected")
destination_label.pack(pady=10)

select_destination_button = tk.Button(root, text="Select Destination", command=select_destination)
select_destination_button.pack(pady=5)

# Progress bar
progress_bar = Progressbar(root, orient=tk.HORIZONTAL, length=400, mode='determinate')
progress_bar.pack(pady=10)

# Transfer button
transfer_button = tk.Button(root, text="Transfer Files", command=transfer_files)
transfer_button.pack(pady=10)

# Run the main application loop
root.mainloop()
