from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to compress the image
def compress_image():
    # Get the file path of the image to be compressed
    filepath = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    
    if not filepath:
        messagebox.showerror("Input Error", "Please select an image file.")
        return

    # Open the image
    img = Image.open(filepath)

    # Define the output file path
    output_path = filedialog.asksaveasfilename(
        defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg"), ("All files", "*.*")])

    if not output_path:
        messagebox.showerror("Output Error", "Please select a location to save the compressed image.")
        return

    # Compress the image
    img.save(output_path, "JPEG", quality=60)  # You can adjust the quality from 0 (worst) to 100 (best)

    messagebox.showinfo("Success", f"Image compressed and saved at {output_path}")

# Setting up the GUI
root = tk.Tk()
root.title("Image Compressor")
root.geometry("300x150")

# Button to start compression
compress_button = tk.Button(root, text="Compress Image", command=compress_image)
compress_button.pack(pady=20)

# Run the GUI event loop
root.mainloop()
