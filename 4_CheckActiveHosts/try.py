'''from scapy.all import *

ip = '192.168.43.1'

request = IP(dst=ip)/ICMP()

reply = sr1(request,timeout=2,iface="eth0")
print(reply.show())
'''
#!/usr/bin/python
from scapy.all import *

TIMEOUT = 2
conf.verb = 0
for ip in range(1, 255):
    packet = IP(dst="192.168.43." + str(ip), ttl=20)/ICMP()
    reply = sr1(packet, timeout=TIMEOUT)
    if not (reply is None):
         print reply.dst, "is online"
    else:
         print "Timeout waiting for %s" % packet[IP].dst
