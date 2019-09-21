from scapy.all import *
conf.verb = 0

target_ip = "192.168.4.124"
reflect_ip = "192.168.4.177"
for port in range(1,100):
    spoofedPacket = IP(src=reflect_ip, dst=target_ip)/TCP(dport=port)
    send(spoofedPacket)
    print("Packet Sent from %s to %s on port %s" %(reflect_ip,target_ip,port))

#info@qjtechnologies.com