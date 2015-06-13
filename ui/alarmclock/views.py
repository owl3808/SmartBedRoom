from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
import sys, os, __builtin__

def index(request):
	return render_to_response('alarmclock.html')

def setalarmtime(request):
	print 'AA='+str(__builtin__.AA)
	try:
		hour = request.REQUEST['hour']
		minute = request.REQUEST['minute']
        except KeyError:
		return HttpResponse("Error: not import hour or minute value")
	__builtin__.alarmclock.settingAlarmClock(int(hour), int(minute))
	print __builtin__.alarmclock.getAlarmClock()
	return HttpResponse("Setting Alarm Clock: " + hour + ':' + minute)

def status(request):
	return HttpResponse("status: ON<br>time: 11:23")
