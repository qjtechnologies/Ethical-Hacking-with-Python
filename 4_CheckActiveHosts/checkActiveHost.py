'''
ToDo: Checking the Host Status if Up or Unreachable

Output:
192.168.43.1 is Up
192.168.43.2 is not reachable
192.168.43.3 is not reachable
192.168.43.4 is not reachable

Related Links: https://scapy.readthedocs.io/en/latest/

Author: Qaidjohar Jawadwala

'''

from scapy.all import *
#No useless data on the screen 
conf.verb = 0
TIMEOUT = 2

for i in range(1,10):
	ip = '192.168.43.'+str(i)
	#Creating a request Packet
	request = IP(dst=ip)/ICMP()
	#Sending data on the network and receiving the reply into reply variable
	reply = sr1(request,timeout=TIMEOUT,iface="wlan0")
	#If no reply is received, then host is down else host is up
	if(reply is None):
		print ip, "is not reachable"
	else:
		print reply.src, "is up"
