# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, JsonResponse

import json, os, io

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Logs(View):
	def post(self, request):
		info = {
			'hostname' : request.POST.get('hostname', ''),
			'ip' : request.POST.get('ip', ''),
			'message' : request.POST.get('message', '')
		}

		with open(BASE_DIR + '/../file.txt', 'w') as outfile:
			outfile.write(json.dumps(info))

		return HttpResponse('Info Saved Successfully', status = 200)