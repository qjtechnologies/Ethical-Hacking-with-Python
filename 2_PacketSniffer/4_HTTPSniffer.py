from scapy.all import *

def scapy_callback(pkt):
	if(pkt[TCP].sport == 80):
		#print("Source: %s:%s\t<-->\tDest: %s:%s" %(pkt[IP].src,pkt[TCP].sport,pkt[IP].dst,pkt[TCP].dport))
		#pkt.show()
		print("\n\n\nSource: %s: <-->Dest: %s \n Payload:" %(pkt[IP].src,pkt[IP].dst))
		print(str(bytes(pkt[TCP].payload)))


sniff(filter='tcp port 80', prn=scapy_callback)
