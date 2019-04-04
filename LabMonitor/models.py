# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# username - admin
# p/w - administrator

# Create your models here.
class LabReport(models.Model):
	clientIP = models.CharField(max_length = 15, primary_key = True)
	clientName = models.CharField(max_length = 100, blank = False)
	clientStatus = models.BooleanField(default = False)
	flag = models.BooleanField(default = False)

	usbDetected = models.BooleanField(default = False)
	# usbTimestamp = models.DateField(null = True)
	
	internetDetected = models.BooleanField(default = False)
	# internetTimestamp = models.DateField(null = True)
	
	lanDetected = models.BooleanField(default = False)
	# lanTimestamp = models.DateField(null = True)

	def __str__(self):
		return '%s' % (self.clientIP)

	class Meta:
		ordering = ['flag']
