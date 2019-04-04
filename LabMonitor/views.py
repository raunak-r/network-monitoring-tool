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
	# At each receiving request, make a sound or something.

	def post(self, request):
		# import pdb; pdb.set_trace()
		hostname = str(request.POST.get('hostname', ''))
		ip = str(request.POST.get('ip', ''))
		clientStatus = request.POST.get('clientStatus', '')
		usb = request.POST.get('usbDetected', '')
		internet = request.POST.get('internetDetected', '')
		lan = request.POST.get('lanDetected', '')
		
		print(ip + ' ' + clientStatus + ' ' + usb + ' ' + internet + ' ' + lan) 
		
		flag = False
		if usb == 'True' or internet == 'True' or lan == 'True':
			flag = True

		entry = LabReport(clientIP = ip,\
						clientName = hostname,\
						clientStatus = clientStatus,
						flag = flag,
						usbDetected = usb,
						internetDetected = internet,
						lanDetected = lan)
		entry.save()

		# with open(BASE_DIR + '/../LabReport.txt', 'a+') as outfile:
		# 	outfile.write(json.dumps(info, sort_keys = False, indent = 4))

		return HttpResponse('Info Saved Successfully', status = 200)