import tkinter as tk  # Import the tkinter module and assign it the alias "tk"
from tkinter import messagebox  # Import the messagebox module from tkinter

class Calculator(tk.Tk):  # Define a class Calculator that inherits from tk.Tk
    def __init__(self):  # Define the constructor method
        super().__init__()  # Call the constructor of the parent class (tk.Tk)
        self.title("Calculator")  # Set the title of the window to "Calculator"
        self.geometry("400x600")  # Set the size of the window to 400x600 pixels
        self.configure(bg="#2c3e50")  # Set the background color of the window to #2c3e50
        self.create_widgets()  # Call the create_widgets method to create the GUI widgets

    def create_widgets(self):  # Define a method to create the GUI widgets
        self.result_var = tk.StringVar()  # Create a StringVar object to store the result
        tk.Entry(self, textvariable=self.result_var, font=("Arial", 20), bd=10, insertwidth=2, width=14, borderwidth=4, bg="#ecf0f1").grid(row=0, column=0, columnspan=4)  # Create an Entry widget to display the result
        
        button_texts = [  # Define a list of button texts
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]
        
        row = 1  # Initialize the row variable to 1
        col = 0  # Initialize the column variable to 0
        for text in button_texts:  # Loop through the button texts
            self.create_button(text, row, col)  # Call the create_button method to create a button
            col += 1  # Increment the column variable
            if col > 3:  # If the column variable exceeds 3
                col = 0  # Reset the column variable to 0
                row += 1  # Increment the row variable
    
    def create_button(self, text, row, col):  # Define a method to create a button
        button_style = {"bg": "#3498db", "fg": "#ecf0f1", "font": ("Arial", 18), "width": 5, "height": 2}  # Define a dictionary of button styles
        if text == "=":  # If the button text is "="
            tk.Button(self, text=text, command=self.calculate_result, **button_style).grid(row=row, column=col, padx=5, pady=5)  # Create a button with the calculate_result method as its command
        elif text == "C":  # If the button text is "C"
            tk.Button(self, text=text, command=self.clear, **button_style).grid(row=row, column=col, padx=5, pady=5)  # Create a button with the clear method as its command
        else:
            tk.Button(self, text=text, command=lambda t=text: self.on_button_click(t), **button_style).grid(row=row, column=col, padx=5, pady=5)  # Create a button with the on_button_click method as its command
    
    def on_button_click(self, char):  # Define a method to handle button clicks
        current_text = self.result_var.get()  # Get the current text in the result variable
        new_text = current_text + char  # Append the clicked character to the current text
        self.result_var.set(new_text)  # Set the result variable to the new text
    
    def calculate_result(self):  # Define a method to calculate the result
        try:
            result = eval(self.result_var.get())  # Evaluate the expression in the result variable
            self.result_var.set(result)  # Set the result variable to the calculated result
        except Exception as e:  # Catch any exceptions
            messagebox.showerror("Error", "Invalid Input")  # Show an error message
            self.result_var.set("")  # Clear the result variable
    
    def clear(self):  # Define a method to clear the result
        self.result_var.set("")  # Clear the result variable

if __name__ == "__main__":  # Check if the script is being run directly (not being imported as a module)
    calculator = Calculator()  # Create an instance of the Calculator class
    calculator.mainloop()  # Start the GUI event loop