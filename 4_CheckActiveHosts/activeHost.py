from scapy.all import *
import sys
conf.verb = 0
interface = "eth0"

print(sys.argv)
for i in range(120,200):
    dst_ip = "192.168.4."+str(i)
    request = IP(dst=dst_ip)/ICMP()
    reply = sr1(request,timeout=2,iface=interface)
    if(reply is None):
        print dst_ip, " is not reachable"
    else:
        print dst_ip, " is Up"