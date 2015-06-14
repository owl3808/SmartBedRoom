from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
import sys, os, __builtin__
from datetime import datetime

def index(request):
	return render_to_response('curtain_control.html')

def Open(request):
	__builtin__.curtain.open()
	return HttpResponse("Opening")

def Close(request):
	__builtin__.curtain.close()
	return HttpResponse("Closing")
