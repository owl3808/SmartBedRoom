import light, lightSensor
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

lightsensor = lightSensor.lightSensor(7)
ledlight = light.light(3)

while True:
	if lightsensor.isLightful():
		ledlight.lightOff()
	else:
		ledlight.lightOn()
		
