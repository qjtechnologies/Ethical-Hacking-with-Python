import nmap

#Defining an object for Scanning Port
nm = nmap.PortScanner()

#Scanning Port as provided in arguments
#nm.scan('11.11.3.200-220','1-100')
nm.scan('192.168.43.140-150','1-100')


print(nm.all_hosts())


for host in nm.all_hosts():
	print('----------------------------------------------------')
	print('Host : %s (%s)' % (host, nm[host].hostname()))
	print('State : %s' % nm[host].state())

	for proto in nm[host].all_protocols():
		print('----------')
		print('Protocol : %s' % proto)
		
		lport = nm[host][proto].keys()
		lport.sort()
		for port in lport:
			print('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))



