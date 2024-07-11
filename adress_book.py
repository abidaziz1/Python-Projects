import tkinter as tk  # Import the tkinter library and assign it the alias "tk"
from tkinter import messagebox  # Import the messagebox module from tkinter

class AddressBook(tk.Tk):  # Define a class AddressBook that inherits from tk.Tk
    def __init__(self):  # Define the constructor method
        super().__init__()  # Call the constructor of the parent class (tk.Tk)
        self.title("Address Book")  # Set the title of the window to "Address Book"
        self.geometry("400x600")  # Set the size of the window to 400x600 pixels
        self.configure(bg="#2c3e50")  # Set the background color of the window to a dark blue-gray color
        self.create_widgets()  # Call the create_widgets method to create the GUI widgets

    def create_widgets(self):  # Define a method to create the GUI widgets
        self.name_var = tk.StringVar()  # Create a StringVar object to store the name input
        self.phone_var = tk.StringVar()  # Create a StringVar object to store the phone input
        self.email_var = tk.StringVar()  # Create a StringVar object to store the email input

        tk.Label(self, text="Name", bg="#2c3e50", fg="#ecf0f1", font=("Arial", 14)).pack(pady=5)  # Create a Label widget with the text "Name" and pack it into the window
        tk.Entry(self, textvariable=self.name_var, font=("Arial", 14), bg="#ecf0f1", fg="#2c3e50").pack(pady=5)  # Create an Entry widget to input the name and pack it into the window

        tk.Label(self, text="Phone", bg="#2c3e50", fg="#ecf0f1", font=("Arial", 14)).pack(pady=5)  # Create a Label widget with the text "Phone" and pack it into the window
        tk.Entry(self, textvariable=self.phone_var, font=("Arial", 14), bg="#ecf0f1", fg="#2c3e50").pack(pady=5)  # Create an Entry widget to input the phone number and pack it into the window

        tk.Label(self, text="Email", bg="#2c3e50", fg="#ecf0f1", font=("Arial", 14)).pack(pady=5)  # Create a Label widget with the text "Email" and pack it into the window
        tk.Entry(self, textvariable=self.email_var, font=("Arial", 14), bg="#ecf0f1", fg="#2c3e50").pack(pady=5)  # Create an Entry widget to input the email and pack it into the window

        tk.Button(self, text="Add Contact", command=self.add_contact, bg="#3498db", fg="#ecf0f1", font=("Arial", 14)).pack(pady=10)  # Create a Button widget with the text "Add Contact" and pack it into the window

        self.contacts_listbox = tk.Listbox(self, font=("Arial", 14), bg="#ecf0f1", fg="#2c3e50")  # Create a Listbox widget to display the contacts
        self.contacts_listbox.pack(fill=tk.BOTH, expand=True, pady=10)  # Pack the Listbox widget into the window and set it to fill both horizontally and vertically

        tk.Button(self, text="Remove Contact", command=self.remove_contact, bg="#e74c3c", fg="#ecf0f1", font=("Arial", 14)).pack(pady=5)  # Create a Button widget with the text "Remove Contact" and pack it into the window

    def add_contact(self):  # Define a method to add a contact
        name = self.name_var.get()  # Get the input value from the name Entry widget
        phone = self.phone_var.get()  # Get the input value from the phone Entry widget
        email = self.email_var.get()  # Get the input value from the email Entry widget

        if name and phone and email:  # Check if all fields are filled
            contact_info = f"{name} - {phone} - {email}"  # Create a string to display the contact information
            self.contacts_listbox.insert(tk.END, contact_info)  # Insert the contact information into the Listbox widget
            self.name_var.set("")  # Clear the name Entry widget
            self.phone_var.set("")  # Clear the phone Entry widget
            self.email_var.set("")  # Clear the email Entry widget
        else:
            messagebox.showwarning("Warning", "Please fill all fields")
    def remove_contact(self):
        try:
            selected_contact_index = self.contacts_listbox.curselection()[0]
            self.contacts_listbox.delete(selected_contact_index)
        except IndexError:
            messagebox.showwarning("Warning", "Please select a contact to remove")

if __name__ == "__main__":
    address_book = AddressBook()
    address_book.mainloop()
