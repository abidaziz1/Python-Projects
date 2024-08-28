"""
Features:
Unit Selection:

Users can select between "Metric" (kilograms and centimeters) and "Imperial" (pounds and inches) units.
The BMI calculation adjusts based on the selected unit.
Input Fields:

Weight and height fields are provided.
The weight and height inputs dynamically adjust depending on the selected unit.
BMI Calculation:

For Metric units:
The height is converted from centimeters to meters.
BMI is calculated using the formula: 
BMI
=
Weight (kg)
Height (m)
2
BMI= 
Height (m) 
2
 
Weight (kg)
​
 
For Imperial units:
BMI is calculated using the formula: 
BMI
=
Weight (lbs)
Height (inches)
2
×
703
BMI= 
Height (inches) 
2
 
Weight (lbs)
​
 ×703
Error Handling:

If the user enters non-positive numbers or other invalid input, an error message is displayed.
BMI Result Display:

The calculated BMI is displayed with appropriate units.
A message box shows the BMI category (underweight, normal weight, overweight, obesity).
GUI Layout:

The layout is clean and user-friendly, with clear labels, radio buttons for unit selection, and buttons for calculation.

"""
import tkinter as tk
from tkinter import messagebox


class BMICalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced BMI Calculator")
        self.root.geometry("400x500")
        
        # Variables to store user input
        self.weight_var = tk.DoubleVar()
        self.height_var = tk.DoubleVar()
        self.bmi_var = tk.StringVar()
        self.unit_var = tk.StringVar(value="Metric")  # Default to Metric

        self.create_widgets()

    def create_widgets(self):
        # Unit selection
        tk.Label(self.root, text="Select Unit:", font=('Arial', 12)).pack(pady=10)
        tk.Radiobutton(self.root, text="Metric (kg, cm)", variable=self.unit_var, value="Metric", font=('Arial', 12)).pack()
        tk.Radiobutton(self.root, text="Imperial (lbs, inches)", variable=self.unit_var, value="Imperial", font=('Arial', 12)).pack()

        # Create and place widgets for weight
        tk.Label(self.root, text="Enter Weight:", font=('Arial', 12)).pack(pady=10)
        tk.Entry(self.root, textvariable=self.weight_var, font=('Arial', 12)).pack(pady=10)

        # Create and place widgets for height
        tk.Label(self.root, text="Enter Height:", font=('Arial', 12)).pack(pady=10)
        tk.Entry(self.root, textvariable=self.height_var, font=('Arial', 12)).pack(pady=10)

        # Button to calculate BMI
        tk.Button(self.root, text="Calculate BMI", command=self.calculate_bmi, font=('Arial', 12)).pack(pady=20)

        # Label to display BMI result
        tk.Label(self.root, text="Your BMI is:", font=('Arial', 12)).pack(pady=10)
        tk.Label(self.root, textvariable=self.bmi_var, font=('Arial', 14, 'bold')).pack(pady=10)

    def calculate_bmi(self):
        try:
            weight = self.weight_var.get()
            height = self.height_var.get()
            unit = self.unit_var.get()

            if weight <= 0 or height <= 0:
                raise ValueError("Height and Weight must be greater than 0")

            if unit == "Metric":
                height = height / 100  # Convert height from cm to meters
                bmi = weight / (height ** 2)
            else:
                bmi = (weight / (height ** 2)) * 703  # BMI formula for imperial units

            bmi = round(bmi, 2)
            self.bmi_var.set(f"{bmi} kg/m²")

            self.show_bmi_category(bmi)
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))

    def show_bmi_category(self, bmi):
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"

        messagebox.showinfo("BMI Category", f"Your BMI indicates that you are {category}.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BMICalculator(root)
    root.mainloop()
