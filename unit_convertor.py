import tkinter as tk  # Import the tkinter library and assign it the alias "tk"
from tkinter import ttk, messagebox  # Import additional tkinter modules for themed widgets and message boxes

class UnitConverter(tk.Tk):  # Define a class UnitConverter that inherits from tk.Tk
    def __init__(self):  # Initialize the UnitConverter class
        super().__init__()  # Call the constructor of the parent class (tk.Tk)
        self.title("Unit Converter")  # Set the title of the window to "Unit Converter"
        self.geometry("400x400")  # Set the size of the window to 400x400 pixels
        self.configure(bg="#2c3e50")  # Set the background color of the window to a dark blue-gray
        self.create_widgets()  # Call the create_widgets method to create the GUI widgets

    def create_widgets(self):  # Define a method to create the GUI widgets
        self.value_var = tk.StringVar()  # Create a StringVar to store the input value
        self.result_var = tk.StringVar()  # Create a StringVar to store the result
        self.unit_from_var = tk.StringVar(value="Select Unit")  # Create a StringVar to store the "from" unit, initialized to "Select Unit"
        self.unit_to_var = tk.StringVar(value="Select Unit")  # Create a StringVar to store the "to" unit, initialized to "Select Unit"
        
        units = ["Meters", "Kilometers", "Centimeters", "Millimeters", "Inches", "Feet"]  # Define a list of units
        
        tk.Entry(self, textvariable=self.value_var, font=("Arial", 20), bd=10, insertwidth=2, width=14, borderwidth=4, bg="#ecf0f1").pack(pady=10)  # Create an Entry widget for inputting the value
        # The Entry widget is configured with a font, border, and background color
        
        tk.Label(self, text="From", bg="#2c3e50", fg="#ecf0f1", font=("Arial", 14)).pack(pady=5)  # Create a Label widget for the "From" label
        # The Label widget is configured with a background color, foreground color, and font
        
        ttk.Combobox(self, textvariable=self.unit_from_var, values=units, font=("Arial", 14)).pack(pady=5)  # Create a Combobox widget for selecting the "from" unit
        # The Combobox widget is configured with a font and a list of values
        
        tk.Label(self, text="To", bg="#2c3e50", fg="#ecf0f1", font=("Arial", 14)).pack(pady=5)  # Create a Label widget for the "To" label
        # The Label widget is configured with a background color, foreground color, and font
        
        ttk.Combobox(self, textvariable=self.unit_to_var, values=units, font=("Arial", 14)).pack(pady=5)  # Create a Combobox widget for selecting the "to" unit
        # The Combobox widget is configured with a font and a list of values
        
        tk.Button(self, text="Convert", command=self.convert, bg="#3498db", fg="#ecf0f1", font=("Arial", 14)).pack(pady=20)  # Create a Button widget for converting the units
        # The Button widget is configured with a command to call the convert method, and a background color, foreground color, and font
        
        tk.Label(self, text="Result", bg="#2c3e50", fg="#ecf0f1", font=("Arial", 14)).pack(pady=5)  # Create a Label widget for the "Result" label
        # The Label widget is configured with a background color, foreground color, and font
        
        tk.Entry(self, textvariable=self.result_var, font=("Arial", 20), bd=10, insertwidth=2, width=14, borderwidth=4, bg="#ecf0f1", state="readonly").pack(pady=10)  # Create an Entry widget for displaying the result
        # The Entry widget is configured with a font, border, and background color, and is set to read-only

    def convert(self):
        """Convert the input value from one unit to another."""
        try:
            value = float(self.value_var.get())  # Get the input value as a float
            unit_from = self.unit_from_var.get()  # Get the "from" unit
            unit_to = self.unit_to_var.get()  # Get the "to" unit
            
            if unit_from == "Select Unit" or unit_to == "Select Unit":  # Check if either unit is still set to "Select Unit"
                messagebox.showerror("Error", "Please select both units")  # Show an error message if so
                return  # Exit the method
            
            conversion_factors = {  # Define a dictionary of conversion factors
                ("Meters", "Kilometers"): 0.001,
                ("Meters", "Centimeters"): 100,
                ("Meters", "Millimeters"): 1000,
                ("Meters", "Inches"): 39.3701,
                ("Meters", "Feet"): 3.28084,
                # Add more conversion factors here
            }
            
            if unit_from == unit_to:  # If the units are the same, no conversion is needed
                self.result_var.set(value)  # Set the result to the original value
            else:
                factor = conversion_factors.get((unit_from, unit_to))  # Get the conversion factor from the dictionary
                if factor is None:  # If the factor is not found, try the reverse conversion
                    factor = 1 / conversion_factors.get((unit_to, unit_from))
                result = value * factor  # Perform the conversion
                self.result_var.set(result)  # Set the result
        except ValueError:  # Catch any ValueError exceptions (e.g. if the input is not a number)
            messagebox.showerror("Error", "Invalid Input")  # Show an error message
            self.value_var.set("")  # Clear the input field
            self.result_var.set("")  # Clear the result field

if __name__ == "__main__":
    converter = UnitConverter()  # Create an instance of the UnitConverter class
    converter.mainloop()  # Start the GUI event loop
