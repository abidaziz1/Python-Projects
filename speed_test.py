import tkinter as tk
from tkinter import messagebox
import speedtest
import threading

def test_speed():
    try:
        print("Starting speed test...")  # Debugging statement
        
        st = speedtest.Speedtest()
        st.get_best_server()
        download_speed = st.download() / 1_000_000  # Convert to Mbps
        upload_speed = st.upload() / 1_000_000  # Convert to Mbps
        ping = st.results.ping
        
        print(f"Download: {download_speed}, Upload: {upload_speed}, Ping: {ping}")  # Debugging statement
        
        app.after(0, update_labels, download_speed, upload_speed, ping)
        
    except Exception as e:
        print(f"Error: {e}")  # Debugging statement
        messagebox.showerror("Error", f"Failed to perform speed test: {e}")

def update_labels(download_speed, upload_speed, ping):
    download_label.config(text=f"Download Speed: {download_speed:.2f} Mbps")
    upload_label.config(text=f"Upload Speed: {upload_speed:.2f} Mbps")
    ping_label.config(text=f"Ping: {ping:.2f} ms")

def start_test():
    test_thread = threading.Thread(target=test_speed)
    test_thread.start()

# Set up the main application window
app = tk.Tk()
app.title("Internet Speed Test")
app.geometry("400x300")

# Heading
heading = tk.Label(app, text="Internet Speed Test", font=("Helvetica", 16))
heading.pack(pady=20)

# Buttons
test_button = tk.Button(app, text="Start Test", font=("Helvetica", 14), command=start_test)
test_button.pack(pady=10)

# Labels to display the results
download_label = tk.Label(app, text="Download Speed: -- Mbps", font=("Helvetica", 12))
download_label.pack(pady=5)

upload_label = tk.Label(app, text="Upload Speed: -- Mbps", font=("Helvetica", 12))
upload_label.pack(pady=5)

ping_label = tk.Label(app, text="Ping: -- ms", font=("Helvetica", 12))
ping_label.pack(pady=5)

# Run the application
app.mainloop()
