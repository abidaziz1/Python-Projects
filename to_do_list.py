import tkinter as tk  # Import the tkinter module and assign it the alias "tk"
from tkinter import messagebox  # Import the messagebox module from tkinter

class ToDoList(tk.Tk):  # Define a class ToDoList that inherits from tk.Tk
    def __init__(self):  # Define the constructor method
        super().__init__()  # Call the constructor of the parent class (tk.Tk)
        self.title("To-Do List")  # Set the title of the window
        self.geometry("400x400")  # Set the size of the window
        self.configure(bg="#2c3e50")  # Set the background color of the window
        self.create_widgets()  # Call the create_widgets method to create the GUI widgets

    def create_widgets(self):  # Define a method to create the GUI widgets
        self.task_var = tk.StringVar()  # Create a StringVar object to store the task input
        
        # Create an Entry widget to input tasks
        tk.Entry(self, textvariable=self.task_var, font=("Arial", 20), bg="#ecf0f1", fg="#2c3e50").pack(pady=10)
        
        # Create a Button widget to add tasks
        tk.Button(self, text="Add Task", command=self.add_task, bg="#3498db", fg="#ecf0f1", font=("Arial", 14)).pack(pady=5)
        
        # Create a Button widget to remove tasks
        tk.Button(self, text="Remove Task", command=self.remove_task, bg="#e74c3c", fg="#ecf0f1", font=("Arial", 14)).pack(pady=5)
        
        # Create a Button widget to clear all tasks
        tk.Button(self, text="Clear All Tasks", command=self.clear_tasks, bg="#f39c12", fg="#ecf0f1", font=("Arial", 14)).pack(pady=5)
        
        # Create a Listbox widget to display tasks
        self.task_listbox = tk.Listbox(self, selectmode=tk.SINGLE, font=("Arial", 14), bg="#ecf0f1", fg="#2c3e50")
        self.task_listbox.pack(fill=tk.BOTH, expand=True, pady=10)
    
    def add_task(self):  # Define a method to add tasks
        task = self.task_var.get()  # Get the input task from the Entry widget
        if task:  # Check if the task is not empty
            self.task_listbox.insert(tk.END, task)  # Add the task to the Listbox widget
            self.task_var.set("")  # Clear the Entry widget
        else:
            messagebox.showwarning("Warning", "Please enter a task")  # Show a warning message if no task is entered
    
    def remove_task(self):  # Define a method to remove tasks
        try:
            selected_task_index = self.task_listbox.curselection()[0]  # Get the index of the selected task
            self.task_listbox.delete(selected_task_index)  # Remove the selected task from the Listbox widget
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to remove")  # Show a warning message if no task is selected
    
    def clear_tasks(self):  # Define a method to clear all tasks
        self.task_listbox.delete(0, tk.END)  # Clear all tasks from the Listbox widget

if __name__ == "__main__":  # Check if the script is run directly (not imported as a module)
    todo_app = ToDoList()  # Create an instance of the ToDoList class
    todo_app.mainloop()  # Start the GUI event loop