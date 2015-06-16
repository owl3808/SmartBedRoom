from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
import sys, os, __builtin__
from datetime import datetime

def index(request):
	return render_to_response('alarmclock.html')

def setalarmtime(request):
	try:
		hour = request.REQUEST['hour']
		minute = request.REQUEST['minute']
        except KeyError:
		return HttpResponse("Error: not import hour or minute value")
	__builtin__.alarmclock.settingAlarmClock(int(hour), int(minute))
	__builtin__.enableAlarm = True
	print __builtin__.alarmclock.getAlarmClock()
	return HttpResponse("Setting Alarm Clock: " + hour + ':' + minute)

def status(request):
	hour, minute = __builtin__.alarmclock.getAlarmClock()
	ntime = datetime.now()
	return HttpResponse("status: ON<br>currenttime: %d:%d<br>alarmtime: %d:%d" %(ntime.hour, ntime.minute, hour,minute))

