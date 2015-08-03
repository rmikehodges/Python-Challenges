import re
from netaddr import IPNetwork, IPAddress
subnets = {
    '22.63.0.0/18': 0,
    '23.63.5.0/24': 0,
    '23.63.10.0/26': 0,
    '23.63.100.0/22': 0,
    '23.63.192.0/18': 0}
  


def countInSubnet(ipList):
	counter = 0
	with open(ipList) as subnetList:
		data = subnetList.read()
		ipList = re.split('[\[, \"]+', data)
		ipList.pop(0)
		ipList.pop(len(ipList)-1)
		for ip in ipList:
			for subnet in subnets:
				if IPAddress(ip) in IPNetwork(subnet):
					subnets[subnet]+=1
	return subnets

print countInSubnet('ipaddr.json')
	
