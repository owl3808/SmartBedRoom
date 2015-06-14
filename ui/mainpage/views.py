from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
import sys, os, __builtin__
from datetime import datetime

def index(request):
	return render_to_response('index.html')
