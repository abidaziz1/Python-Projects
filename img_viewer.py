# Import the tkinter module, which is a Python binding to the Tk GUI toolkit
import tkinter as tk

# Import the filedialog module from tkinter, which provides a way to open file dialogs
from tkinter import filedialog

# Import the Image and ImageTk modules from the PIL (Python Imaging Library)
from PIL import Image, ImageTk

# Define a class called ImageViewer that inherits from tkinter's Tk class
class ImageViewer(tk.Tk):
    # Initialize the ImageViewer class
    def __init__(self):
        # Call the constructor of the parent class (tk.Tk)
        super().__init__()
        
        # Set the title of the window to "Image Viewer"
        self.title("Image Viewer")
        
        # Set the initial size of the window to 800x600 pixels
        self.geometry("800x600")
        
        # Set the background color of the window to a dark blue-gray color (#2c3e50)
        self.configure(bg="#2c3e50")
        
        # Call the create_widgets method to create the GUI widgets
        self.create_widgets()
    
    # Define a method to create the GUI widgets
    def create_widgets(self):
        # Create a Label widget with a dark blue-gray background color
        self.label = tk.Label(self, bg="#2c3e50")
        
        # Pack the Label widget into the window, making it fill both horizontally and vertically
        self.label.pack(fill=tk.BOTH, expand=True)
        
        # Create a Button widget with the text "Open Image", a blue background color, white text color, and a font size of 14
        tk.Button(self, text="Open Image", command=self.open_image, bg="#3498db", fg="#ecf0f1", font=("Arial", 14)).pack(pady=20)
    
    # Define a method to open an image file
    def open_image(self):
        # Open a file dialog to select an image file
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif"), ("All files", "*.*")])
        
        # If a file path is selected
        if file_path:
            # Open the image file using PIL
            image = Image.open(file_path)
            
            # Resize the image to fit the window size (800x600) using LANCZOS resampling filter
            image = image.resize((800, 600), Image.LANCZOS)
            
            # Convert the PIL image to a PhotoImage object that can be used in tkinter
            photo = ImageTk.PhotoImage(image)
            
            # Configure the Label widget to display the image
            self.label.config(image=photo)
            
            # Keep a reference to the PhotoImage object to prevent it from being garbage collected
            self.label.image = photo

# If this script is run directly (not imported as a module)
if __name__ == "__main__":
    # Create an instance of the ImageViewer class
    image_viewer = ImageViewer()
    
    # Start the main event loop of the GUI
    image_viewer.mainloop()