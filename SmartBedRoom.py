import light, lightSensor, clock, musicPlayer, button
import RPi.GPIO as GPIO
GPIO.setwarnings(False)

enableAlarm = True
isplayingmusic = False

lightsensor = lightSensor.lightSensor(7)
ledlight = light.light(3)
alarmclock = clock.Clock()
button = button.Button(12)
musicPlayer = musicPlayer.MusicPlayer('little_love_song.mp3')

alarmclock.settingAlarmClock(0,23)

while True:
	if lightsensor.isLightful():
		ledlight.lightOff()
	else:
		ledlight.lightOn()
	
	if enableAlarm:
		if alarmclock.isAchiveAlarmTime():
			if not isplayingmusic:
				print 'alarmclock: alarming!'
				musicPlayer.play()
				isplayingmusic = True

	if enableAlarm and button.isPressed():
		musicPlayer.stop()
		ismucicplaying = False
		enableAlarm=False

	if not enableAlarm and button.isPressed():
		alarmclock.settingAlarmClockToNextDay()
		enableAlarm=True


