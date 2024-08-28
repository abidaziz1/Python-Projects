import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
import subprocess
import os

class SimplePythonIDE:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Python IDE")

        # Create menu
        self.create_menu()

        # Create text area for code editing
        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, undo=True)
        self.text_area.pack(expand=True, fill='both')

        # Create output area for code execution results
        self.output_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=10, bg="light gray", state='disabled')
        self.output_area.pack(expand=True, fill='both')

    def create_menu(self):
        # Create menu bar
        menu_bar = tk.Menu(self.root)

        # File menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # Run menu
        run_menu = tk.Menu(menu_bar, tearoff=0)
        run_menu.add_command(label="Run", command=self.run_code)
        menu_bar.add_cascade(label="Run", menu=run_menu)

        # Help menu
        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        menu_bar.add_cascade(label="Help", menu=help_menu)

        # Set the menu to root window
        self.root.config(menu=menu_bar)

    def new_file(self):
        # Clear the text area for a new file
        self.text_area.delete(1.0, tk.END)
        self.root.title("New File - Simple Python IDE")

    def open_file(self):
        # Open an existing file
        file_path = filedialog.askopenfilename(defaultextension=".py",
                                               filetypes=[("Python Files", "*.py"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, content)
            self.root.title(f"{os.path.basename(file_path)} - Simple Python IDE")

    def save_file(self):
        # Save the current content to a file
        file_path = filedialog.asksaveasfilename(defaultextension=".py",
                                                 filetypes=[("Python Files", "*.py"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                content = self.text_area.get(1.0, tk.END)
                file.write(content)
            self.root.title(f"{os.path.basename(file_path)} - Simple Python IDE")

    def run_code(self):
        # Save the current code to a temporary file and run it
        code = self.text_area.get(1.0, tk.END)
        temp_file = "temp_code.py"

        with open(temp_file, 'w') as file:
            file.write(code)

        # Run the code using subprocess and capture the output
        try:
            output = subprocess.check_output(['python', temp_file], stderr=subprocess.STDOUT, text=True)
        except subprocess.CalledProcessError as e:
            output = e.output

        # Display the output in the output area
        self.output_area.config(state='normal')
        self.output_area.delete(1.0, tk.END)
        self.output_area.insert(tk.END, output)
        self.output_area.config(state='disabled')

        # Remove the temporary file
        os.remove(temp_file)

    def show_about(self):
        # Show information about the IDE
        messagebox.showinfo("About", "Simple Python IDE\nBuilt with Tkinter")

if __name__ == "__main__":
    root = tk.Tk()
    ide = SimplePythonIDE(root)
    root.mainloop()
