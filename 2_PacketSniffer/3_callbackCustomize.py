from scapy.all import *

def scapy_callback(pkt):
	#a[0][IP].src
	#print("Source IP: %s <--> Dest IP: %s" %(pkt[IP].src,pkt[IP].dst))
	print("Source: %s:%s\t<-->\tDest: %s:%s" %(pkt[IP].src,pkt[TCP].sport,pkt[IP].dst,pkt[TCP].dport))


sniff(filter='tcp port 80', prn=scapy_callback)
