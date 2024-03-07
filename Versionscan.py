import nmap
import subprocess
from termcolor import colored

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
    scanner = nmap.PortScanner()
    arguments = f'-sV -p {port_range}'
    scanner.scan(hosts=targets, arguments=arguments)

    for host in scanner.all_hosts():
        print(f"Host: {host}")
        for proto in scanner[host].all_protocols():
            print(f"Protocol: {proto}")
            ports = scanner[host][proto].keys()
            for port in ports:
                service = scanner[host][proto][port]
                port_status = colored(service['state'], 'green' if service['state'] == 'open' else 'red')
                service_name = colored(service['name'], 'cyan')
                print(f"Port: {port}\tState: {port_status}\tService: {service_name}\tVersion: {service.get('version', '')}")

if __name__ == "__main__":
    list_ips()
    targets = input("\nEnter the target host(s) (separated by comma if multiple): ").split(',')
    port_range = input("Enter the range of ports to scan (e.g., '1-1000'): ")
    scan_ports(targets, port_range)
