from scapy.all import sniff, TCP
import time, socket, requests

def timer(x):
	if time.time() - start >= 1000:
		return True
	else:
		return False

def mainfunc(x):
	print(x.summary())
	if x.haslayer(TCP):
		postLogsToServer(2, True)

	return True

def postLogsToServer(flag, booleanStatus):
	hostname, ip = getSystemInfo()
	url = "http://localhost:8000/recordlogs/"

	params = {
		'hostname'	:	hostname,
		'ip'		:	ip,
		'flag':	flag,
		'booleanStatus' : booleanStatus
	}

	r = requests.post(url = url, data = params)

def getSystemInfo():
	hostname = socket.gethostname()
	ip = socket.gethostbyname(hostname)
	return (hostname, ip)

start = time.time()

sniff(filter="ip",\
	# prn=lambda x:x.sprintf("{IP:%IP.src% -> %IP.dst%\n}"),\
	prn = mainfunc,
	count = 0,
	stop_filter = timer)
	
 
# s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
# port_num = 65565
# print("port_num = " + str(port_num))

# while True:
# 	data = s.recvfrom(65565)

# 	try:
# 		if "HTTP" in data[0][54:] or "FTP" in data[0][54:]:
# 			print "[","="*30,']','\n\n'
# 			raw=data[0][54:]
			
# 			if "\r\n\r\n" in raw:
# 				line=raw.split('\r\n\r\n')[0]
# 				print "[*] Header Captured "
# 				print line[line.find('HTTP'):]
# 			else:
# 				print raw
		
# 		else:
# 			# print '[{}]'.format(data)
# 			pass
	
# 	except:
# 		pass