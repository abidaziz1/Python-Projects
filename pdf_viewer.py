import fitz  # PyMuPDF
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

# Function to open and display a PDF
def open_pdf():
    # Get the file path of the PDF to open
    filepath = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])

    if not filepath:
        messagebox.showerror("Input Error", "Please select a PDF file.")
        return

    try:
        # Open the PDF
        pdf_document = fitz.open(filepath)
        render_page(pdf_document, 0)  # Render the first page initially
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open PDF: {e}")

# Function to render a specific page of the PDF
def render_page(pdf_document, page_number):
    if 0 <= page_number < pdf_document.page_count:
        page = pdf_document.load_page(page_number)  # Load the page
        pix = page.get_pixmap()  # Render the page to an image
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

        img_tk = ImageTk.PhotoImage(img)
        img_label.config(image=img_tk)
        img_label.image = img_tk

        global current_page
        current_page = page_number
    else:
        messagebox.showinfo("Navigation", "No more pages.")

# Function to go to the next page
def next_page():
    if pdf_document and current_page < pdf_document.page_count - 1:
        render_page(pdf_document, current_page + 1)

# Function to go to the previous page
def previous_page():
    if pdf_document and current_page > 0:
        render_page(pdf_document, current_page - 1)

# Setting up the GUI
root = tk.Tk()
root.title("PDF Viewer")
root.geometry("600x700")

# PDF image display area
img_label = tk.Label(root)
img_label.pack()

# Navigation buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

prev_btn = tk.Button(btn_frame, text="Previous", command=previous_page)
prev_btn.grid(row=0, column=0, padx=10)

next_btn = tk.Button(btn_frame, text="Next", command=next_page)
next_btn.grid(row=0, column=1, padx=10)

# Open PDF button
open_btn = tk.Button(root, text="Open PDF", command=open_pdf)
open_btn.pack(pady=20)

# Global variables
pdf_document = None
current_page = 0

# Run the GUI event loop
root.mainloop()
