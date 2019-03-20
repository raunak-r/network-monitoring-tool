import pyudev

def getNumberOfConnections(context):
	totalConnected = 0
	for device in context.list_devices(subsystem = 'block', DEVTYPE = 'partition'):
		print(device)
		totalConnected += 1
	return totalConnected

def synchronousMonitoring(context):
	monitor = pyudev.Monitor.from_netlink(context)
	monitor.filter_by('block')
	for action, device in monitor:
		if 'ID_FS_TYPE' in device:
			print('{0} partition {1}'\
					.format(action, device.get('ID_FS_LABEL')))

if __name__ == "__main__":
	context = pyudev.Context()
	print(getNumberOfConnections(context))
	synchronousMonitoring(context)