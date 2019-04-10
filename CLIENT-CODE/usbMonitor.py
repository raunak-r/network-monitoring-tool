import pyudev
import time
from functools import partial
import requests, socket, os
import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# def getNumberOfConnections(context):
# 	totalConnected = 0
# 	for device in context.list_devices(subsystem = 'block', DEVTYPE = 'partition'):
# 		print(device)
# 		totalConnected += 1
# 	return totalConnected

def synchronousMonitoring(context):	
	try:
		# Creates a Monitor which keeps on running
		monitor = pyudev.Monitor.from_netlink(context)
		monitor.filter_by('block')

		# Runs for the next 2 hours once an event is logged
		for device in iter(partial(monitor.poll, 7200), None):
			msgstring = '{0.action} on {1}' .format(device, device.get('ID_FS_LABEL'))
			print(msgstring)

			with open(BASE_DIR + '/clientUSBReport.txt', 'a+') as outfile:
				outfile.write(str(datetime.datetime.now()) + '\t' + msgstring + '\n')

			if device.action == 'add' or device.action == 'remove':
				postLogsToServer(1, True)

	except Exception, e:
		postLogsToServer(0, False)

		print(e)
		synchronousMonitoring(context)

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

try:
	with open(BASE_DIR + '/clientUSBReport.txt', 'w') as outfile:
		outfile.close()

	# Up and Running
	postLogsToServer(0, True)

	context = pyudev.Context()
	# print(getNumberOfConnections(context))
	synchronousMonitoring(context)

except Exception, e:
	print(e)
	postLogsToServer(0, False)