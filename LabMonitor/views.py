# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generics import View
from django.http import HttpRepsponse, JsonResponse

class Logs(View):
	def post(self, request):
