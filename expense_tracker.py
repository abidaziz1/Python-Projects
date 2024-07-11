# Import the tkinter library and assign it the alias "tk"
import tkinter as tk
# Import the messagebox module from tkinter
from tkinter import messagebox

# Define a class ExpenseTracker that inherits from tk.Tk
class ExpenseTracker(tk.Tk):
    # Define the constructor method
    def __init__(self):
        # Call the constructor of the parent class (tk.Tk)
        super().__init__()
        # Set the title of the window
        self.title("Expense Tracker")
        # Set the size of the window
        self.geometry("500x500")
        # Set the background color of the window
        self.configure(bg="#2c3e50")
        # Call the create_widgets method to create the GUI widgets
        self.create_widgets()
        # Initialize an empty list to store the expenses
        self.expenses = []
    
    # Define a method to create the GUI widgets
    def create_widgets(self):
        # Create a StringVar object to store the item name
        self.item_var = tk.StringVar()
        # Create a DoubleVar object to store the amount
        self.amount_var = tk.DoubleVar()
        
        # Create a label for the item name
        tk.Label(self, text="Item", bg="#2c3e50", fg="#ecf0f1", font=("Arial", 14)).pack(pady=5)
        # Create an entry field for the item name
        tk.Entry(self, textvariable=self.item_var, font=("Arial", 14), bg="#ecf0f1", fg="#2c3e50").pack(pady=5)
        
        # Create a label for the amount
        tk.Label(self, text="Amount", bg="#2c3e50", fg="#ecf0f1", font=("Arial", 14)).pack(pady=5)
        # Create an entry field for the amount
        tk.Entry(self, textvariable=self.amount_var, font=("Arial", 14), bg="#ecf0f1", fg="#2c3e50").pack(pady=5)
        
        # Create a button to add an expense
        tk.Button(self, text="Add Expense", command=self.add_expense, bg="#3498db", fg="#ecf0f1", font=("Arial", 14)).pack(pady=10)
        # Create a button to clear all expenses
        tk.Button(self, text="Clear All Expenses", command=self.clear_expenses, bg="#e74c3c", fg="#ecf0f1", font=("Arial", 14)).pack(pady=5)
        
        # Create a listbox to display the expenses
        self.expense_listbox = tk.Listbox(self, font=("Arial", 14), bg="#ecf0f1", fg="#2c3e50")
        # Pack the listbox to fill the available space
        self.expense_listbox.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Create a label to display the total amount
        self.total_label = tk.Label(self, text="Total: $0.00", bg="#2c3e50", fg="#ecf0f1", font=("Arial", 14))
        # Pack the label
        self.total_label.pack(pady=5)
    
    # Define a method to add an expense
    def add_expense(self):
        # Get the item name from the entry field
        item = self.item_var.get()
        # Get the amount from the entry field
        amount = self.amount_var.get()
        
        # Check if both fields are filled
        if item and amount:
            # Add the expense to the list
            self.expenses.append((item, amount))
            # Update the listbox and total label
            self.update_expense_list()
            # Clear the item name entry field
            self.item_var.set("")
            # Clear the amount entry field
            self.amount_var.set(0.0)
        else:
            # Show a warning message if either field is empty
            messagebox.showwarning("Warning", "Please fill both fields")
    
    # Define a method to clear all expenses
    def clear_expenses(self):
        # Clear the expenses list
        self.expenses = []
        # Update the listbox and total label
        self.update_expense_list()
    
    # Define a method to update the listbox and total label
    # Define a method to update the listbox and total label
    def update_expense_list(self):
    # Clear the listbox
        self.expense_listbox.delete(0, tk.END)
    # Initialize the total amount
        total = 0.0
    # Iterate over the expenses list
        for item, amount in self.expenses:
        # Add each expense to the listbox
            self.expense_listbox.insert(tk.END, f"{item}: ${amount:.2f}")
        # Add the amount to the total
            total += amount
    # Update the total label
        self.total_label.config(text=f"Total: ${total:.2f}")
if __name__ == "__main__":
    # Create an instance of the ExpenseTracker class
    expense_tracker = ExpenseTracker()
    # Start the main event loop
    expense_tracker.mainloop()