import socket
from termcolor import colored

def scan_ports(ip, ports):
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
            print(colored(f"Port {port} is open", "green"))
        else:
            print(colored(f"Port {port} is closed", "red"))
        sock.close()
    return open_ports

if __name__ == "__main__":
    print(colored("Port Scanner Tool", "blue"))
    print(colored("This tool is for educational purposes and created by Miraj Sankdecha.", "blue"))
    print(colored("=" * 50, "blue"))

    target_ips = input("Enter target IP addresses separated by comma: ").split(',')
    port_range = input("Enter port range (e.g., 1-100): ")
    start_port, end_port = map(int, port_range.split('-'))
    ports = range(start_port, end_port + 1)
    
    for ip in target_ips:
        print(colored(f"Scanning ports for {ip}:", "blue"))
        open_ports = scan_ports(ip.strip(), ports)
        if open_ports:
            print(colored("Open ports:", "green"), open_ports)
        else:
            print(colored("No open ports found", "red"))
