
from scapy.all import sniff, TCP
import time

start = time.time()

def timer(x):
	if time.time() - start >= 1000:
		return True
	else:
		return False

def mainfunc(x):
	if x.haslayer(TCP):
		return True
	else:
		return False

def postLogsToServer():
	hostname, ip = getSystemInfo()
	url = "http://localhost:8000/recordlogs/"

	params = {
		'hostname'	:	hostname,
		'ip'		:	ip,
		'clientStatus':	clientStatus,
		'usbDetected':	usb,
		'internetDetected': internet,
		'lanDetected':	lan,
	}

	r = requests.post(url = url, data = params)

def getSystemInfo():
	hostname = socket.gethostname()
	ip = socket.gethostbyname(hostname)
	return (hostname, ip)
	
sniff(filter="ip",\
	# prn=lambda x:x.sprintf("{IP:%IP.src% -> %IP.dst%\n}"),\
	prn = mainfunc,
	count = 0,
	stop_filter = timer)
	


# # # import socket
 
# # # #create an INET, raw socket
# # # s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
 
# # # # receive a packet
# # # while True:

# # #    # print output on terminal
# # #    print s.recvfrom(65565)


# # import socket
# # # from struct import *

# # # def eth_addr(a):
# # # 	b = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(a[0]) , ord(a[1]) , ord(a[2]), ord(a[3]), ord(a[4]) , ord(a[5]))
# # # 	return b

# # s=socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
# # port_num = 65565
# # print("port_num = " + str(port_num))

# # while True:
# # 	packet = s.recvfrom(port_num)
# # 	print(packet)
# # 	print('\n\n')

# # 	# packet = packet[0]
# # 	# eth_len = 14
# # 	# eth_header = packet[:eth_len]
# # 	# eth = unpack('!6s6sH', eth_header)
# # 	# eth_protocol = socket.ntohs(eth[2])
# # 	# print('Destination MAC : ' + eth_addr(packet[0:6]) + ' Source MAC : ' + eth_addr(packet[6:12]) + ' Protocol : ' + str(eth_protocol))
# # 	# try:
# # 	# 	if "HTTP" in data[0][54:] or "FTP" in data[0][54:]:
# # 	# 		print "[","="*30,']','\n\n'
# # 	# 		raw=data[0][54:]
# # 	# 		if "\r\n\r\n" in raw:
# # 	# 			line=raw.split('\r\n\r\n')[0]
# # 	# 			print "[*] Header Captured "
# # 	# 			print line[line.find('HTTP'):]
# # 	# 		else:
# # 	# 			print raw
# # 	# 	else:
# # 	# 	# 	# print '[{}]'.format(data)
# # 	# 		pass
# # 	# except:
# # 	# 	pass