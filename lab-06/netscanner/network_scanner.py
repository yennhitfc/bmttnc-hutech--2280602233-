import requests
import socket
from scapy.all import ARP, Ether, srp

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # kết nối tới một địa chỉ giả để lấy IP nội bộ
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    finally:
        s.close()

def get_vendor_by_mac(mac):
    try:
        response = requests.get(f"https://api.macvendors.com/{mac}")
        if response.status_code == 200:
            return response.text
        else:
            return "Unknown Vendor"
    except Exception as e:
        print("Error fetching vendor:", e)
        return "Unknown Vendor"

def local_network_scan(ip_range):
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp
    result = srp(packet, timeout=3, verbose=0)[0]

    devices = []
    for sent, received in result:
        devices.append({
            'ip': received.psrc,
            'mac': received.hwsrc,
            'vendor': get_vendor_by_mac(received.hwsrc)
        })
    return devices

def main():
    local_ip = get_local_ip()
    subnet = ".".join(local_ip.split('.')[:3]) + ".1/24"  # VD: 192.168.1.1/24
    print(f"Scanning subnet: {subnet}")

    devices = local_network_scan(subnet)

    print("\nDevices found in the network:")
    if devices:
        for device in devices:
            print(f"IP: {device['ip']}, MAC: {device['mac']}, Vendor: {device['vendor']}")
    else:
        print("No devices found.")

if __name__ == '__main__':
    main()
