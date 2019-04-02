import pyudev
import time
from functools import partial
import requests, socket, datetime

def getNumberOfConnections(context):
	totalConnected = 0
	for device in context.list_devices(subsystem = 'block', DEVTYPE = 'partition'):
		print(device)
		totalConnected += 1
	return totalConnected

def synchronousMonitoring(context):
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

			if device.action == 'add' and device.get('ID_FS_LABEL') != 'None':
				postLogs('USB Connected - ' + msgstring)
			elif device.action == 'remove' and device.get('ID_FS_LABEL') != 'None':
				postLogs('USB Removed - ' + msgstring)

		# FOR INTERNET

		# FOR LAN
	except Exception, e:
		print(e)
		synchronousMonitoring(context)


def postLogs(message):
	hostname, ip = getSystemInfo()
	url = "http://localhost:8000/recordlogs/"
	params = {
		'hostname'	:	hostname,
		'ip'		:	ip,
		'time'		:	str(time.ctime()),
		'message'	:	message,

	}

	r = requests.post(url = url, data = params)

def getSystemInfo():
	hostname = socket.gethostname()
	ip = socket.gethostbyname(hostname)
	return (hostname, ip)

if __name__ == "__main__":
	context = pyudev.Context()
	# print(getNumberOfConnections(context))

	t0 = time.time()
	synchronousMonitoring(context)
