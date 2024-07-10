import socket  # Provides low-level networking interface for creating network connections.
from threading import Thread  #  Enables concurrent execution by using threads.
from queue import Queue  # Provides a thread-safe queue for managing tasks.

# Define a function to scan a single port
def port_scan(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"Port {port}: Open")
        sock.close()
    except socket.error as e:
        print(f"Error scanning port {port}: {e}")
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM): Creates a socket object for IPv4 and TCP.
# sock.settimeout(1): Sets a timeout of 1 second for connection attempts.
# result = sock.connect_ex((host, port)): Attempts to connect to the specified host and port. Returns 0 if the port is open.
# if result == 0: Checks if the port is open.
# sock.close(): Closes the socket connection.
# except socket.error as e: Catches and prints any socket errors.

def threader():
    while True:
        worker = q.get()
        port_scan(host, worker)
        q.task_done()
# worker = q.get(): Retrieves a port number from the queue.
# port_scan(host, worker): Calls the port scanning function with the retrieved port.
# q.task_done(): Marks the task as completed.


def main():
    global host, q
    host = input("Enter the host to be scanned (IP address or hostname): ")
    port_range = input("Enter the range of ports to scan (e.g., 1-1000): ")
    port_start, port_end = map(int, port_range.split('-'))    
    q = Queue()    
    for x in range(100):
        t = Thread(target=threader)
        t.daemon = True
        t.start()    
    for port in range(port_start, port_end + 1):
        q.put(port)    
    q.join()
# host = input(...): Gets the target host from the user.
# port_range = input(...): Gets the range of ports to scan from the user.
# port_start, port_end = map(int, port_range.split('-')): Splits the port range and converts them to integers.
# q = Queue(): Creates a queue for managing ports.
# for x in range(100): Creates 100 threads to perform the scanning.
# for port in range(port_start, port_end + 1): Adds each port in the range to the queue.
# q.join(): Waits for all tasks in the queue to be completed.

if __name__ == "__main__":
    main()
# Ensures the main function is called only when the script is executed directly.