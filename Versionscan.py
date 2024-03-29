import nmap
import subprocess
import socket
from termcolor import colored
from tabulate import tabulate

def get_local_ip():
    try:
        host_name = socket.gethostname()
        local_ip = socket.gethostbyname(host_name)
        return local_ip
    except Exception as e:
        print("Error occurred while fetching local IP address:", e)
        return None

def list_ips():
    try:
        arp_output = subprocess.check_output(['arp', '-a']).decode('utf-8')
        print("List of IP addresses on the network:")
        for line in arp_output.splitlines():
            parts = line.split()
            if len(parts) >= 2:
                ip_address = parts[1]
                print(ip_address)
    except Exception as e:
        print("Error occurred while listing IP addresses:", e)

def scan_ports(targets, port_range):
    scan_results = []
    scanner = nmap.PortScanner()
    arguments = f'-sV -p {port_range}'
    scanner.scan(hosts=targets, arguments=arguments)

    for host in scanner.all_hosts():
        for proto in scanner[host].all_protocols():
            ports = scanner[host][proto].keys()
            for port in ports:
                service = scanner[host][proto][port]
                port_status = colored(service['state'], 'green' if service['state'] == 'open' else 'red')
                service_name = colored(service['name'], 'cyan')
                scan_results.append([host, proto, port, port_status, service_name, service.get('version', '')])

    return scan_results

if __name__ == "__main__":
    print("""
  _______   _______   _______   _______  
 /  ___  \ /  ___  \ /  ___  \ /  ___  \ 
|  (__ \  |  (__ \  |  (__ \  |  (__ \  |
 \______ / \______ / \______ / \______ / 
    """)
    print("Script created by: Miraj Sankdecha")
    print("For educational purposes only.\n")
    
    print("Your Local IP Address:", get_local_ip())
    list_ips()
    targets = input("\nEnter the target host(s) (separated by comma if multiple): ").split(',')
    port_range = input("Enter the range of ports to scan (e.g., '1-1000'): ")
    scan_results = scan_ports(targets, port_range)
    
    headers = ["Host", "Protocol", "Port", "State", "Service", "Version"]
    print(tabulate(scan_results, headers=headers, tablefmt="grid"))
