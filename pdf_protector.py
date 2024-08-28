"""
Explanation
GUI Setup: The Tkinter GUI is set up with labels, buttons, and an entry field for the password.

Selecting PDF File: The select_pdf method allows users to select a PDF file from their system using a file dialog.

Password Protection: The protect_pdf method reads the selected PDF, applies the entered password, and saves it as a new protected PDF.

File Handling: The user is prompted to select a location to save the protected PDF.

Error Handling: Basic error handling is included to manage user input and file operations.


"""

import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfReader, PdfWriter


class PDFProtectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Protector")
        self.root.geometry("400x200")
        
        self.filename = ""
        
        # Create GUI elements
        self.label = tk.Label(root, text="Select PDF to Protect", font=("Arial", 12))
        self.label.pack(pady=10)
        
        self.select_button = tk.Button(root, text="Browse", command=self.select_pdf)
        self.select_button.pack(pady=5)
        
        self.password_label = tk.Label(root, text="Enter Password", font=("Arial", 12))
        self.password_label.pack(pady=10)
        
        self.password_entry = tk.Entry(root, show="*", width=30)
        self.password_entry.pack(pady=5)
        
        self.protect_button = tk.Button(root, text="Protect PDF", command=self.protect_pdf)
        self.protect_button.pack(pady=20)
    
    def select_pdf(self):
        self.filename = filedialog.askopenfilename(
            title="Select PDF",
            filetypes=(("PDF Files", "*.pdf"),)
        )
        if self.filename:
            self.label.config(text=f"Selected: {os.path.basename(self.filename)}")
    
    def protect_pdf(self):
        if not self.filename:
            messagebox.showwarning("No File", "Please select a PDF file first.")
            return
        
        password = self.password_entry.get()
        if not password:
            messagebox.showwarning("No Password", "Please enter a password.")
            return
        
        try:
            # Read the original PDF
            pdf_reader = PdfReader(self.filename)
            pdf_writer = PdfWriter()
            
            for page in pdf_reader.pages:
                pdf_writer.add_page(page)
            
            # Encrypt with the password
            pdf_writer.encrypt(password)
            
            # Save the protected PDF
            protected_filename = filedialog.asksaveasfilename(
                defaultextension=".pdf",
                filetypes=[("PDF Files", "*.pdf")],
                title="Save Protected PDF"
            )
            
            if protected_filename:
                with open(protected_filename, "wb") as out_file:
                    pdf_writer.write(out_file)
                messagebox.showinfo("Success", "PDF protected successfully!")
            else:
                messagebox.showwarning("Cancelled", "Save operation was cancelled.")
        
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = PDFProtectorApp(root)
    root.mainloop()
