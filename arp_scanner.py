import scapy.all as scapy  # Importing the scapy library for packet manipulation
import threading  # Importing the threading library for concurrent execution

def arp_scan(ip_range):
    """
    Perform an ARP scan on the given IP range.
    
    Args:
        ip_range (str): The IP range to scan in CIDR notation (e.g., "192.168.1.1/24").
        
    Returns:
        list: A list of dictionaries containing IP and MAC addresses of discovered devices.
    """
    print(f"Starting ARP scan on IP range: {ip_range}")  # Debug statement
    
    # Create an ARP request packet for the specified IP range. pdst is the target IP address field in the ARP packet.
    arp_request = scapy.ARP(pdst=ip_range)
    
    # Create an Ethernet frame with a broadcast MAC address, meaning the packet will be sent to all devices on the local network.
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    
    # Combines the Ethernet frame and ARP request into a single packet.
    arp_request_broadcast = broadcast / arp_request
    
    # Send the packet and receive responses
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    
    # Initializes an empty list to store the details of discovered clients (IP and MAC addresses).
    clients_list = []
    
    for element in answered_list:
        client_info = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_info)
    
    print(f"Finished ARP scan on IP range: {ip_range}")  # Debug statement
    return clients_list  # Return the list of discovered clients

def thread_function(ip_range):
    """
    Thread function to scan a specific IP range.
    Args:
        ip_range (str): The IP range to scan.
    """
    print(f"Thread started for IP range: {ip_range}")  # Debug statement
    result = arp_scan(ip_range)  # Perform ARP scan on the given IP range
    
    # Print the IP and MAC addresses of discovered clients
    for client in result:
        print(f"IP: {client['ip']}, MAC: {client['mac']}")
    print(f"Thread finished for IP range: {ip_range}")  # Debug statement

def main():
    """
    Main function to initiate ARP scan using multithreading.
    """
    ip_ranges = ["192.168.1.1/24", "192.168.2.1/24"]  # List of IP ranges to scan
    threads = []  # List to store threads
    
    # Create and start threads for each IP range
    for ip_range in ip_ranges:
        thread = threading.Thread(target=thread_function, args=(ip_range,))
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()  # Call the main function to start the scan


# No Devices Responded to the ARP Requests:
# The specified IP ranges might not have active devices.
# Devices may be configured to ignore ARP requests from unknown sources.

# Network Configuration Issues:
# Ensure the IP ranges specified are correct and within the local network.
# Verify that your machine has the necessary permissions and network configuration to perform ARP scans.