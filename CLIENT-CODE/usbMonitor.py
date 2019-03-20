import pyudev

def getNumberOfConnections(context):
	totalConnected = 0
	for device in context.list_devices(subsystem = 'block', DEVTYPE = 'partition'):
		print(device)
		totalConnected += 1
	return totalConnected

if __name__ == "__main__":
	context = pyudev.Context()
	print(getNumberOfConnections(context))