import subprocess
from scapy.all import *

def get_interfaces():
    result = subprocess.run(['netsh', 'interface', 'show', 'interface'], capture_output=True, text=True)
    output_lines = result.stdout.splitlines()[3:]
    interfaces = [line.split()[3] for line in output_lines if len(line.split()) >= 4]
    return interfaces

def packet_handler(packet):
    if packet.haslayer(Raw):
        print("Captured Packet:")
        print(str(packet))
        
interfaces = get_interfaces()

print("Danh sach cac giao dien mang:")
for i, iface in enumerate(interfaces, start=1):
    print(f"{i}. {iface}")
    
choice = int(input("Chon giao dien de bat dau bat goi: "))
selected_iface = interfaces[choice - 1]

sniff(iface=selected_iface, prn=packet_handler, filter="tcp")

        