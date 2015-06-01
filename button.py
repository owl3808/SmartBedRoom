import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

class Button:
	def __init__(self, pin):
		self.pin=pin
		GPIO.setup(self.pin, GPIO.IN)

	def isPressed(self):
		if GPIO.input(self.pin):
			for i in range(100):
				if not GPIO.input(self.pin):
					break
				time.sleep(0.01)
			return True
		else:
			return False

if __name__ == '__main__':
	GPIO.setmode(GPIO.BOARD)
	mybutton = Button(12)
	while True:
		print mybutton.isPressed()
