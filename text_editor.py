import tkinter as tk  # Import the tkinter module and assign it the alias "tk"
from tkinter import filedialog, messagebox  # Import the filedialog and messagebox modules from tkinter

class TextEditor(tk.Tk):  # Define a class TextEditor that inherits from tk.Tk
    def __init__(self):  # Define the constructor method
        super().__init__()  # Call the constructor of the parent class (tk.Tk)
        self.title("Text Editor")  # Set the title of the window to "Text Editor"
        self.geometry("600x600")  # Set the size of the window to 600x600 pixels
        self.configure(bg="#2c3e50")  # Set the background color of the window to #2c3e50
        self.create_widgets()  # Call the create_widgets method to create the GUI widgets

    def create_widgets(self):  # Define a method to create the GUI widgets
        self.text_area = tk.Text(self, wrap=tk.WORD, font=("Arial", 14), bg="#ecf0f1", fg="#2c3e50")  # Create a Text widget with specified font and colors
        self.text_area.pack(fill=tk.BOTH, expand=True)  # Add the Text widget to the window and make it expand to fill the available space
        self.create_menu()  # Call the create_menu method to create the menu

    def create_menu(self):  # Define a method to create the menu
        menu_bar = tk.Menu(self)  # Create a Menu widget

        file_menu = tk.Menu(menu_bar, tearoff=0)  # Create a submenu for the "File" menu
        file_menu.add_command(label="New", command=self.new_file)  # Add a "New" menu item that calls the new_file method when clicked
        file_menu.add_command(label="Open", command=self.open_file)  # Add an "Open" menu item that calls the open_file method when clicked
        file_menu.add_command(label="Save", command=self.save_file)  # Add a "Save" menu item that calls the save_file method when clicked
        file_menu.add_separator()  # Add a separator to the menu
        file_menu.add_command(label="Exit", command=self.quit)  # Add an "Exit" menu item that calls the quit method when clicked

        menu_bar.add_cascade(label="File", menu=file_menu)  # Add the "File" menu to the menu bar
        self.config(menu=menu_bar)  # Set the menu bar for the window

    def new_file(self):  # Define a method to create a new file
        self.text_area.delete(1.0, tk.END)  # Clear the text area

    def open_file(self):  # Define a method to open a file
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])  # Open a file dialog to select a file
        if file_path:  # If a file is selected
            try:
                with open(file_path, "r") as file:  # Open the file in read mode
                    content = file.read()  # Read the file content
                    self.text_area.delete(1.0, tk.END)  # Clear the text area
                    self.text_area.insert(tk.END, content)  # Insert the file content into the text area
            except Exception as e:  # Catch any exceptions that occur
                messagebox.showerror("Error", f"Could not open file: {e}")  # Show an error message

    def save_file(self):  # Define a method to save a file
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])  # Open a file dialog to select a file
        if file_path:  # If a file is selected
            try:
                with open(file_path, "w") as file:  # Open the file in write mode
                    content = self.text_area.get(1.0, tk.END)  # Get the content of the text area
                    file.write(content)  # Write the content to the file
            except Exception as e:  # Catch any exceptions that occur
                messagebox.showerror("Error", f"Could not save file: {e}")  # Show an error message

if __name__ == "__main__":  # Check if the script is being run directly (not being imported as a module)
    text_editor = TextEditor()  # Create an instance of the TextEditor class
    text_editor.mainloop()  # Start the GUI event loop