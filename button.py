import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

class Button:
	def __init__(self, pin):
		self.pin=pin
		GPIO.setup(self.pin, GPIO.IN)

	def isPressed(self):
		return GPIO.input(self.pin)


if __name__ == '__main__':
	GPIO.setmode(GPIO.BOARD)
	mybutton = Button(12)
	while True:
		print mybutton.isPressed()
