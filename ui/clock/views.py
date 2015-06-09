from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
	return render_to_response('alarmclock.html')

def setalarmtime(request):
	try:
		hour = request.REQUEST['hour']
		minute = request.REQUEST['minute']
        except KeyError:
		return HttpResponse("Error: not import hour or minute value")
	return HttpResponse(hour + ':' + minute)
