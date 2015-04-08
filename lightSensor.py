import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

class lightSensor:
	def __init__(self, pin):
		self.pin=pin
		GPIO.setup(self.pin, GPIO.IN)

	def isLightful(self):
		return GPIO.input(self.pin)


if __name__ == '__main__':
	GPIO.setmode(GPIO.BOARD)
	mylightsensor = lightSensor(7)
	while True:
		print mylightsensor.isLightful()
