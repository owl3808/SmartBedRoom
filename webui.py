import os,sys
from threading import Thread

def run():
	print 'starting httpd'
	import __init__ as ui

def runInBackGround():
	thread = Thread(target=run, args=())
	thread.start()
	return thread

def setEnv():
	#os.chdir('ui')
	newpath = [os.path.dirname(os.path.abspath(__file__))+'/ui']
	newpath.extend(sys.path)
	sys.path=newpath

def cleanEnv():
	os.chdir('..')

if __name__ == '__main__':
	runInBackGround()
