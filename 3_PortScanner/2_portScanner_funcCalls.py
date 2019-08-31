'''
ToDo: Create a PortScanner Using Nmap using nmap function calls

Output:
Host: <IP>(<HostName>)
Status: Up/Down
Services and Ports:
<Protocol> || <Port> || <Service>
...

Related Links: https://pypi.org/project/python-nmap/

Author: Qaidjohar Jawadwala

'''

import nmap #Importing the Library

nm = nmap.PortScanner()	#Initializing the Library

scanned = nm.scan('192.168.43.123-175','1-5000')	#Scanning through hosts and Ports range

#Looping through all the hosts(host is IP address)
for host in nm.all_hosts():
	print('Host:'+host + '('+nm[host].hostname()+')')	#printing IP and Host Name
	print('Status:'+nm[host].state())	#Printing of Host is Up or Down
	print('Services and Ports:')
	#Looping through the protocols of which ports are open (TCP|UDP...)
	for proto in nm[host].all_protocols():
		#Looping through ports of all the open services in the protocol
		for port in nm[host][proto].keys():
			#printing Protocol, Port and Product Name running on the port.
			print('%s\t||\t%s\t||\t%s' %(proto,port,nm[host][proto][port]['product']))
	print('')



