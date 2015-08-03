from netaddr import IPNetwork, IPAddress


def countInRange(ipList):
	counter = 0
	with open(ipList, 'r') as cidrList:
		for line in cidrList:
			paramList = (line.rstrip()).split(' ')
			if IPAddress(paramList[1]) in IPNetwork(paramList[0]):
				counter+=1
	return counter
		
	
print countInSubnet('iplist.txt')
