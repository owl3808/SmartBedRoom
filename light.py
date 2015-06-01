import RPi.GPIO as GPIO

class light:
	isLightOn=False
	def __init__(self, pin):
		self.lightpin = pin
		GPIO.setup(self.lightpin, GPIO.OUT)
		GPIO.output(self.lightpin, False)

	def lightOn(self):
		if not self.isLightOn:
			GPIO.output(self.lightpin, True)
			self.isLightOn=True

	def lightOff(self):
		if self.isLightOn:
			GPIO.output(self.lightpin, False)
			self.isLightOn=False

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
