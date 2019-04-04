# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from models import LabReport

class LabReportModelAdmin(admin.ModelAdmin):
	list_display = [field.name for field in LabReport._meta.get_fields()]
	list_filter = ['flag', 'usbDetected', 'internetDetected', 'lanDetected']
	
	class Meta:
		model = LabReport

admin.site.register(LabReport, LabReportModelAdmin)