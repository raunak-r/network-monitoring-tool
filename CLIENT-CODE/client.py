import pyudev
import time
from functools import partial
import requests, socket

clientStatus = True
usb = False
internet = False
lan = False

# def getNumberOfConnections(context):
# 	totalConnected = 0
# 	for device in context.list_devices(subsystem = 'block', DEVTYPE = 'partition'):
# 		print(device)
# 		totalConnected += 1
# 	return totalConnected

def synchronousMonitoring(context):
	global usb, internet, lan, clientStatus
	
	try:
		# Creates a Monitor which keeps on running
		monitor = pyudev.Monitor.from_netlink(context)
		monitor.filter_by('block')

		# action can be add, remove for the corresponding device
		# for action, device in monitor:
		# 	if 'ID_FS_TYPE' in device:
		# 		print('{0} partition {1}'\
		# 				.form*at(action, device.get('ID_FS_LABEL')))

		# Runs for the next 2 hours once an event is logged

		# FOR USB
		for device in iter(partial(monitor.poll, 7200), None):
			msgstring = '{0.action} on {1}' .format(device, device.get('ID_FS_LABEL'))
			print(msgstring)

			if device.action == 'add' or device.action == 'remove':
				usb = True
				postLogsToServer()

		# FOR INTERNET

		# FOR LAN
	except Exception, e:
		clientStatus = False
		postLogsToServer()

		print(e)
		synchronousMonitoring(context)

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



try:
	# Up and Running	
	clientStatus = True
	postLogsToServer()

	context = pyudev.Context()
	# print(getNumberOfConnections(context))
	synchronousMonitoring(context)

except Exception, e:
	print(e)
	clientStatus = False
	postLogsToServer()