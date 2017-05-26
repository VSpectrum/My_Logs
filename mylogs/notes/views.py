# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from notes.models import Log
from collections import OrderedDict
from pprint import pprint
# Create your views here.
def index(request):
	Logs = [x for x in Log.objects.all().order_by('order')]
	dict_dates = {}

	for log in Logs:
		try:
			if dict_dates[log.date]:
				dict_dates[log.date].append((log.logHours, log.logNote))
		except:
			dict_dates[log.date] = [(log.logHours, log.logNote)]
	pprint(dict_dates)
	data = {'Logs': OrderedDict(sorted(dict_dates.items(), key=lambda t: t[0], reverse=True)) }
	return render(request,'logs.html', data)

def filter(request, filter_word):
	Logs = [x for x in Log.objects.filter(tags__name__in=[filter_word]).order_by('order')]
	dict_dates = {}

	for log in Logs:
		try:
			if dict_dates[log.date]:
				dict_dates[log.date].append((log.logHours, log.logNote))
		except:
			dict_dates[log.date] = [(log.logHours, log.logNote)]
	pprint(dict_dates)
	data = {'Logs': OrderedDict(sorted(dict_dates.items(), key=lambda t: t[0], reverse=True)) }
	return render(request,'logs.html', data)