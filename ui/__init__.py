#!/usr/bin/env python
import os
import sys
sys.argv[0]=os.path.abspath(__file__)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ui.settings")
from django.core.management import execute_from_command_line
execute_from_command_line(('SmartBedRoom.py','runserver','0.0.0.0:8080'))

