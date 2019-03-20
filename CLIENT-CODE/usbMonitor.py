import pyudev
import time
from functools import partial

def getNumberOfConnections(context):
	totalConnected = 0
	for device in context.list_devices(subsystem = 'block', DEVTYPE = 'partition'):
		print(device)
		totalConnected += 1
	return totalConnected

def synchronousMonitoring(context):
	# Creates a Monitor which keeps on running
	monitor = pyudev.Monitor.from_netlink(context)
	monitor.filter_by('block')

	# action can be add, remove for the corresponding device
	# for action, device in monitor:
	# 	if 'ID_FS_TYPE' in device:
	# 		print('{0} partition {1}'\
	# 				.format(action, device.get('ID_FS_LABEL')))

	# Runs for the next 2 hours once an event is logged
	for device in iter(partial(monitor.poll, 7200), None):
		print('{0.action} on {1}' .format(device, device.get('ID_FS_LABEL')))

if __name__ == "__main__":
	context = pyudev.Context()
	print(getNumberOfConnections(context))

	t0 = time.time()


	synchronousMonitoring(context)
