from scapy.all import *

def scapy_callback(pkt):
	pkt.show()


sniff(filter='tcp', prn=scapy_callback)

#for i in range(10):
#	print(a[i].show())
