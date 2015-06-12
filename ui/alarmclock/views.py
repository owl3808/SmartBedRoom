from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
import sys, os

def index(request):
	return render_to_response('alarmclock.html')

def setalarmtime(request):
	try:
		hour = request.REQUEST['hour']
		minute = request.REQUEST['minute']
        except KeyError:
		return HttpResponse("Error: not import hour or minute value")
	sys.path.append(os.path.realpath("../"))
	import clock
	myclock = clock.Clock()
	myclock.settingAlarmClock(int(hour), int(minute))
	print myclock.getAlarmClock()
	return HttpResponse("Setting Alarm Clock: " + hour + ':' + minute)

def status(request):
	return HttpResponse("status: ON<br>time: 11:23")
