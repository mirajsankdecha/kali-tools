import socket
from concurrent.futures import ThreadPoolExecutor
from termcolor import colored

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(colored(f"Port {port} is open", "green"))
            return port
        else:
            print(colored(f"Port {port} is closed", "red"))
        sock.close()
    except Exception as e:
        print(colored(f"Error occurred while scanning port {port}: {str(e)}", "red"))
    return None

def scan_ports(ip, ports):
    open_ports = []
    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = [executor.submit(scan_port, ip, port) for port in ports]
        for future in futures:
            result = future.result()
            if result:
                open_ports.append(result)
    return open_ports

def get_port_range():
    while True:
        port_range = input("Enter port range (e.g., 1-100): ")
        if '-' in port_range:
            try:
                start_port, end_port = map(int, port_range.split('-'))
                return start_port, end_port
            except ValueError:
                print(colored("Invalid port range format. Please try again.", "red"))
        else:
            print(colored("Port range should be in the format of 'start_port-end_port'. Please try again.", "red"))

if __name__ == "__main__":
    print(colored("Port Scanner Tool", "blue"))
    print(colored("This tool is for educational purposes and created by Miraj Sankdecha.", "blue"))
    print(colored("=" * 50, "blue"))

    try:
        target_ips = input("Enter target IP addresses separated by comma (press Enter to skip): ").strip()
        if target_ips:
            target_ips = target_ips.split(',')
        else:
            target_ips = []

        start_port, end_port = get_port_range()
        ports = range(start_port, end_port + 1)

        if not target_ips:
            print(colored("No target IP addresses provided. Exiting.", "yellow"))
        else:
            for ip in target_ips:
                print(colored(f"Scanning ports for {ip}:", "blue"))
                open_ports = scan_ports(ip.strip(), ports)
                if open_ports:
                    print(colored("Open ports:", "green"), open_ports)
                else:
                    print(colored("No open ports found", "red"))
    except Exception as e:
        print(colored(f"An error occurred: {str(e)}", "red"))
