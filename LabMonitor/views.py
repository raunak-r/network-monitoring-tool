# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, JsonResponse

import json, os, io

# Import from Database 
from models import LabReport

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Logs(View):
	
	def post(self, request):
		hostname = str(request.POST.get('hostname', ''))
		ip = str(request.POST.get('ip', ''))
		flag = int(request.POST.get('flag', ''))
		booleanStatus = request.POST.get('booleanStatus', '')

		print(ip + ' ' + str(flag) + ' ' + booleanStatus)

		if flag == 0:	#Up and Running. Create New Entry
			entry = LabReport(clientIP = ip,\
						clientName = hostname,\
						clientStatus = booleanStatus,
						flag = False,
						usbDetected = False,
						internetDetected = False,
						lanDetected = False)
			entry.save()
		elif flag == 1:	# USB Flag
			entry = LabReport.objects.get(clientIP = ip)
			entry.usbDetected = booleanStatus
			entry.flag = booleanStatus
			entry.save()
		elif flag == 2:	# Internet and LAN Flag
			entry = LabReport.objects.get(clientIP = ip)
			entry.internetDetected = booleanStatus
			entry.lanDetected = booleanStatus
			entry.flag = booleanStatus
			entry.save()

		os.system('spd-say "ALERT"')

		return HttpResponse('Info Saved Successfully', status = 200)