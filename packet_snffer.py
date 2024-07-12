from scapy.all import *  # Import all Scapy modules
from scapy.layers.inet import IP, TCP, UDP  # Import specific layers from Scapy
from scapy.layers.dns import DNS  # Import DNS layer from Scapy
from scapy.layers.http import HTTPRequest  # Import HTTPRequest layer from Scapy
import tkinter as tk  # Import Tkinter for GUI
from tkinter import filedialog  # Import filedialog from Tkinter for file saving
import threading  # Import threading for running sniffer in a separate thread

# Callback function to process each packet
def packet_callback(packet):
    if packet.haslayer(IP):  # Check if the packet has an IP layer
        ip_src = packet[IP].src  # Extract source IP address
        ip_dst = packet[IP].dst  # Extract destination IP address
        
        # Determine protocol
        if packet.haslayer(TCP):  # Check if the packet has a TCP layer
            protocol = "TCP"  # Set protocol to TCP
        elif packet.haslayer(UDP):  # Check if the packet has a UDP layer
            protocol = "UDP"  # Set protocol to UDP
        elif packet.haslayer(DNS):  # Check if the packet has a DNS layer
            protocol = "DNS"  # Set protocol to DNS
        elif packet.haslayer(HTTPRequest):  # Check if the packet has an HTTPRequest layer
            protocol = "HTTP"  # Set protocol to HTTP
        else:
            protocol = "OTHER"  # Set protocol to OTHER if none of the above
        
        # Print packet details
        print(f"IP Source: {ip_src} IP Destination: {ip_dst} Protocol: {protocol}")
        
        # Detailed packet information based on protocol
        if protocol == "TCP":
            print(f"TCP Source Port: {packet[TCP].sport} TCP Destination Port: {packet[TCP].dport}")
        elif protocol == "UDP":
            print(f"UDP Source Port: {packet[UDP].sport} UDP Destination Port: {packet[UDP].dport}")
        elif protocol == "DNS":
            print(f"DNS Query: {packet[DNS].qd.qname}")
        elif protocol == "HTTP":
            print(f"HTTP Method: {packet[HTTPRequest].Method.decode()} HTTP Host: {packet[HTTPRequest].Host.decode()} HTTP Path: {packet[HTTPRequest].Path.decode()}")

# Function to start sniffing packets based on the selected protocol
def start_sniffing(filter_protocol):
    if filter_protocol == "TCP":
        sniff(filter="tcp", prn=packet_callback, store=0, timeout=30, count=50)
    elif filter_protocol == "UDP":
        sniff(filter="udp", prn=packet_callback, store=0, timeout=30, count=50)
    elif filter_protocol == "DNS":
        sniff(filter="udp port 53", prn=packet_callback, store=0, timeout=30, count=50)
    elif filter_protocol == "HTTP":
        sniff(filter="tcp port 80", prn=packet_callback, store=0, timeout=30, count=50)
    else:
        sniff(prn=packet_callback, store=0, timeout=30, count=50)

# Function to save packets to a file
def save_packets(file_path, packets):
    wrpcap(file_path, packets)  # Write packets to a file in pcap format

# Function to run the sniffer in a separate thread
def run_sniffer():
    protocol = protocol_var.get().strip().upper()  # Get selected protocol from GUI
    start_sniffing(protocol)  # Start sniffing based on selected protocol

# Function to start sniffing on a new thread
def start_sniffing_thread():
    sniffer_thread = threading.Thread(target=run_sniffer)  # Create a new thread for the sniffer
    sniffer_thread.start()  # Start the sniffer thread

# Create GUI
root = tk.Tk()  # Create the main window
root.title("Packet Sniffer")  # Set the title of the window

# Protocol selection label and dropdown
tk.Label(root, text="Select Protocol:").pack()  # Label for protocol selection
protocol_var = tk.StringVar(value="TCP")  # String variable for selected protocol
protocol_dropdown = tk.OptionMenu(root, protocol_var, "TCP", "UDP", "DNS", "HTTP")  # Dropdown menu for protocol selection
protocol_dropdown.pack()  # Pack the dropdown menu

# Start sniffing button
start_button = tk.Button(root, text="Start Sniffing", command=start_sniffing_thread)  # Button to start sniffing
start_button.pack()  # Pack the start button

# Run the GUI loop
root.mainloop()  # Start the Tkinter event loop
