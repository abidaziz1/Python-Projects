"""
Features Explained:
Canvas Setup:

A Canvas widget is used for drawing. It is packed to fill the window both horizontally and vertically.
Drawing Functions:

start_draw(event): Records the starting position when the mouse is clicked.
draw(event): Draws a line from the last recorded position to the current position, following the mouse movement.
Color Picker:

select_color(): Opens a color chooser dialog to select the pen color.
Clear Canvas:

clear_canvas(): Deletes all drawings on the canvas.
Saving the Drawing:

save_drawing(): Captures the canvas area as an image and saves it to the selected file path.
Pen Size Selection:

Buttons in the toolbar allow switching between different pen sizes (small, medium, large).
GUI Layout:

The toolbar is created at the top of the window for easy access to tools like color selection, pen size, and save/clear actions.

"""


import tkinter as tk
from tkinter import colorchooser, filedialog
import PIL.ImageGrab as ImageGrab

# Initialize the main application window
root = tk.Tk()
root.title("Digital Whiteboard")
root.geometry("800x600")

# Global variables for drawing
current_x, current_y = 0, 0
color = "black"
pen_size = 5

# Function to start drawing
def start_draw(event):
    global current_x, current_y
    current_x, current_y = event.x, event.y

# Function to draw on the canvas
def draw(event):
    global current_x, current_y
    canvas.create_line(current_x, current_y, event.x, event.y, fill=color, width=pen_size, capstyle=tk.ROUND, smooth=True)
    current_x, current_y = event.x, event.y

# Function to select color
def select_color():
    global color
    color = colorchooser.askcolor()[1]

# Function to clear the canvas
def clear_canvas():
    canvas.delete("all")

# Function to save the drawing
def save_drawing():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
    if file_path:
        x = root.winfo_rootx() + canvas.winfo_x()
        y = root.winfo_rooty() + canvas.winfo_y()
        x1 = x + canvas.winfo_width()
        y1 = y + canvas.winfo_height()
        ImageGrab.grab().crop((x, y, x1, y1)).save(file_path)

# Function to change the pen size
def change_pen_size(size):
    global pen_size
    pen_size = size

# Creating the canvas widget for drawing
canvas = tk.Canvas(root, bg="white", cursor="cross")
canvas.pack(fill=tk.BOTH, expand=True)

# Binding mouse events for drawing
canvas.bind("<Button-1>", start_draw)
canvas.bind("<B1-Motion>", draw)

# Creating the toolbar frame
toolbar = tk.Frame(root, bg="lightgray")
toolbar.pack(side=tk.TOP, fill=tk.X)

# Adding buttons to the toolbar
color_button = tk.Button(toolbar, text="Color", command=select_color)
color_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(toolbar, text="Clear", command=clear_canvas)
clear_button.pack(side=tk.LEFT, padx=5)

save_button = tk.Button(toolbar, text="Save", command=save_drawing)
save_button.pack(side=tk.LEFT, padx=5)

# Adding pen size options to the toolbar
pen_size_label = tk.Label(toolbar, text="Pen Size:")
pen_size_label.pack(side=tk.LEFT, padx=5)

pen_size_small = tk.Button(toolbar, text="Small", command=lambda: change_pen_size(2))
pen_size_small.pack(side=tk.LEFT, padx=5)

pen_size_medium = tk.Button(toolbar, text="Medium", command=lambda: change_pen_size(5))
pen_size_medium.pack(side=tk.LEFT, padx=5)

pen_size_large = tk.Button(toolbar, text="Large", command=lambda: change_pen_size(8))
pen_size_large.pack(side=tk.LEFT, padx=5)

# Running the main application loop
root.mainloop()
