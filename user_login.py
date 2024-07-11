import tkinter as tk
from tkinter import messagebox # module from tkinter used to display message boxes.
import psycopg2 # PostgreSQL database adapter for Python.

# Function to check login credentials
def login():
    username = entry_username.get()
    password = entry_password.get()
# login(): This function handles the login process. It retrieves the entered username and password from the input fields.

    if username == "" or password == "":
        messagebox.showerror("Error", "Please enter both username and password")
        return
# This checks if the username or password fields are empty and displays an error message if either is empty.

    try:
        connection = psycopg2.connect(
            database="user_database",
            user="postgres",  # Default username
            password="yourpassword",
            host="127.0.0.1",
            port="5432"
        )

        cursor = connection.cursor() # Creates a cursor object to interact with the database.

        # Execute the SQL query to fetch the user details from the users table where the username and password match the input.
        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
        result = cursor.fetchone()

        if result:
            messagebox.showinfo("Success", "Login Successful")
        else:
            messagebox.showerror("Error", "Invalid Username or Password")

        cursor.close()
        connection.close() 
# Close the cursor and connection to the database.
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to reset input fields
def reset():
    entry_username.delete(0, tk.END)
    entry_password.delete(0, tk.END)

# Function to handle signup
def signup():
    username = entry_username.get()
    password = entry_password.get()

    if username == "" or password == "":
        messagebox.showerror("Error", "Please enter both username and password")
        return

    try:
        connection = psycopg2.connect(
            database="user_database",
            user="postgres",
            password="yourpassword",
            host="127.0.0.1",
            port="5432"
        )

        cursor = connection.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        connection.commit()
        
        messagebox.showinfo("Success", "Signup Successful")
        
        cursor.close()
        connection.close()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def create_login_window(): # Function to create the main window
    global entry_username, entry_password   # Declares the input fields as global variables to be accessed in the login() function.

    window = tk.Tk() # Initializes the main window.
    window.title("Login Page") # Sets the title of the window.
    window.geometry("400x400") # Sets the size of the window.
    window.resizable(0, 0) # Disables the resizing of the window.
    window.configure(bg="#f0f0f0") # Sets the background color of the window
    
    # Styling
    label_style = {"bg": "#2c3e50", "fg": "#ecf0f1", "font": ("Arial", 12)}
    entry_style = {"bg": "#ecf0f1", "fg": "#2c3e50", "font": ("Arial", 12)}
    button_style = {"bg": "#3498db", "fg": "#ecf0f1", "font": ("Arial", 12)}
    
    tk.Label(window, text="Username", **label_style).pack(pady=10)
    entry_username = tk.Entry(window, **entry_style)
    entry_username.pack(pady=5)
    entry_username.bind("<Return>", lambda event: entry_password.focus_set())  
# This binds the Enter key event to the username entry field. When Enter is pressed while the username entry field is focused, it automatically moves the focus to the password entry field using entry_password.focus_set().

# tk.Label(): Creates labels for the username and password fields.
    tk.Label(window, text="Password", **label_style).pack(pady=10)
    entry_password = tk.Entry(window, show="*", **entry_style)
    entry_password.pack(pady=5)
    entry_password.bind("<Return>", lambda event: login())  # Trigger login on Enter
# The show="*" parameter masks the password input.

    button_frame = tk.Frame(window, bg="#2c3e50")
    button_frame.pack(pady=20)
# Creates a frame for the buttons to be placed in.
    tk.Button(button_frame, text="Login", command=login, **button_style).grid(row=0, column=0, padx=5)
    tk.Button(button_frame, text="Reset", command=reset, **button_style).grid(row=0, column=1, padx=5)
    tk.Button(button_frame, text="Signup", command=signup, **button_style).grid(row=0, column=2, padx=5)

# Creates the "Login" button and binds it to the login() function. Similar for others as well
    window.mainloop()

# Run the login window
create_login_window()
