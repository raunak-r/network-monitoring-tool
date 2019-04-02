import os

def startup():
	BASE_DIR = os.path.dirname(os.path.abspath(__file__))
	open(BASE_DIR + '/../LabReport.txt', 'w').close()

startup()