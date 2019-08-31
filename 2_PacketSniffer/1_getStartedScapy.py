from scapy.all import *

a = sniff(filter='tcp and port 443 or port 80', count=100)

for i in range(10):
	print(a[i].show())

