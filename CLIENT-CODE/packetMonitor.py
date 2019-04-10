from scapy.all import sniff, TCP
import time, socket, requests
import os, datetime

stars = lambda n: "*" * n
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def timer(x):
	if time.time() - start >= 1000:
		return True
	else:
		return False

def mainfunc(x):
	with open(BASE_DIR + '/clientPacketReport.txt', 'a+') as outfile:
		outfile.write(str(datetime.datetime.now()) + '\t' + str(x.summary()) + '\n')
	
	print(x.summary())
	print(x.show())
	print('\n\n\n')

	# return "\n".join((
 #        stars(40) + "GET PACKET" + stars(40),
 #        "\n".join(x.sprintf("{Raw:%Raw.load%}").split(r"\r\n")),
 #        stars(90)))

	if x.haslayer(TCP):
		postLogsToServer(2, True)

	return True

def postLogsToServer(flag, booleanStatus):
	hostname, ip = getSystemInfo()
	url = "http://172.16.46.10:8000/recordlogs/"

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

# Up and Running
with open(BASE_DIR + '/clientPacketReport.txt', 'w') as outfile:
	outfile.close()

postLogsToServer(0, True)

sniff(filter="ip",\
	# prn=lambda x:x.sprintf("{IP:%IP.src% -> %IP.dst%\n}"),\
	prn = mainfunc,
	count = 0,
	# lfilter = lambda p: "GET" in str(p),
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