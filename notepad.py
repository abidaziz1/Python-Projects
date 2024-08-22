import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

# Initialize the main window
root = tk.Tk()
root.title("Notepad")
root.geometry("800x600")

# Global variable to hold the current file path
current_file = None

# Function to open a file
def open_file():
    global current_file
    current_file = filedialog.askopenfilename(defaultextension=".txt",
                                              filetypes=[("Text Files", "*.txt"),
                                                         ("All Files", "*.*")])
    if current_file:
        root.title(f"Notepad - {current_file}")
        with open(current_file, "r") as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())

# Function to save the current file
def save_file():
    global current_file
    if current_file:
        with open(current_file, "w") as file:
            file.write(text_area.get(1.0, tk.END))
        messagebox.showinfo("Notepad", "File Saved")
    else:
        save_as_file()

# Function to save the current file with a new name
def save_as_file():
    global current_file
    current_file = filedialog.asksaveasfilename(defaultextension=".txt",
                                                filetypes=[("Text Files", "*.txt"),
                                                           ("All Files", "*.*")])
    if current_file:
        with open(current_file, "w") as file:
            file.write(text_area.get(1.0, tk.END))
        root.title(f"Notepad - {current_file}")
        messagebox.showinfo("Notepad", "File Saved")

# Function to create a new file
def new_file():
    global current_file
    current_file = None
    text_area.delete(1.0, tk.END)
    root.title("Notepad")

# Function to exit the application
def exit_app():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

# Function to cut text
def cut_text():
    text_area.event_generate("<<Cut>>")

# Function to copy text
def copy_text():
    text_area.event_generate("<<Copy>>")

# Function to paste text
def paste_text():
    text_area.event_generate("<<Paste>>")

# Function to undo text
def undo_text():
    text_area.event_generate("<<Undo>>")

# Function to redo text
def redo_text():
    text_area.event_generate("<<Redo>>")

# Create a Menu bar
menu_bar = tk.Menu(root)

# Create File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open...", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As...", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)
menu_bar.add_cascade(label="File", menu=file_menu)

# Create Edit menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Undo", command=undo_text)
edit_menu.add_command(label="Redo", command=redo_text)
edit_menu.add_separator()
edit_menu.add_command(label="Cut", command=cut_text)
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_command(label="Paste", command=paste_text)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Add Help menu
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=lambda: messagebox.showinfo("Notepad", "Tkinter Notepad by OpenAI's ChatGPT"))
menu_bar.add_cascade(label="Help", menu=help_menu)

# Configure the menu
root.config(menu=menu_bar)

# Create the main text area
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, undo=True)
text_area.pack(fill=tk.BOTH, expand=True)

# Run the application
root.mainloop()
