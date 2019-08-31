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

import nmap	#import nmap library For Installation: #pip install python-nmap

nm = nmap.PortScanner()	#Initialize object for port scanner 
scanData = nm.scan('192.168.43.120-190','1-5000')	#Scanning Hosts and Ports

#Looping through the scanned hosts (IP Address)
for hostip in scanData['scan']:
	#Printing host IP and host name
	print("Host:"+hostip + '('+scanData['scan'][hostip]['hostnames'][0]['name']+')')
	#Printing Host Status of Up/Down
	print('Status:'+scanData['scan'][hostip]['status']['state'])
	
	print('Services and Ports:')
	#assigning the protocol i.e. TCP / UDP
	proto = scanData['scan'][hostip].keys()[-1]
	#looping through the ports for getting the service names of all products
	for port in scanData['scan'][hostip][proto].keys():
		print('%s\t||\t%s\t||\t%s' %(proto,port,nm[hostip][proto][port]['product']))

	print('')
