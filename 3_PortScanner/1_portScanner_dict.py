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

import nmap

nm = nmap.PortScanner()
scanData = nm.scan('192.168.43.120-180','1-5000')

#print(scanData)
for hostip in scanData['scan']:
	print("Host:"+hostip + '('+scanData['scan'][hostip]['hostnames'][0]['name']+')')
	print('Status:'+scanData['scan'][hostip]['status']['state'])
	
	print('Ports:')
	for proto in nm[hostip].all_protocols():
		
		#print(proto)
		#port = nm[hostip][proto].keys()
		for port in nm[hostip][proto].keys():
			print(str(port) + ' ' + proto + ' ' + nm[hostip][proto][port]['product'])
	print('\n')
			#print(port)
			#print(nm[hostip][proto][port]['product'])
		#protocol = nm[hostip].all_protocols()[0]
		#port = nm[hostip][protocol].keys()[0]
		#product = nm[hostip][protocol][port]['product']
		#print(str(port) + ' ' + protocol + ' ' + product)

'''
Host: <IP Address>(<hostname>)
Status: Up/Down
Ports:
Number-tcp/udp-Service
Number-tcp/udp-Service
Number-tcp/udp-Service

'''
