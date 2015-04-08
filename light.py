import RPi.GPIO as GPIO

class light:
	def __init__(self, pin):
		self.lightpin = pin
		GPIO.setup(self.lightpin, GPIO.OUT)

	def lightOn(self):
		GPIO.output(self.lightpin, True)

	def lightOff(self):
		GPIO.output(self.lightpin, False)

if __name__ == '__main__':
	import time
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)
	mylight = light(3)
	for i in range(1,10):
		mylight.lightOff()
		time.sleep(0.5)
		mylight.lightOn()
		time.sleep(0.5)
