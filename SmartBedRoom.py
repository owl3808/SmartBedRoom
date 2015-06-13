import os, time, __builtin__
import light, lightSensor, clock, musicPlayer, button, webui, curtain
import RPi.GPIO as GPIO
GPIO.setwarnings(False)

# variables
enableAlarm = True
isplayingmusic = False

# create instance of modules
lightsensor = lightSensor.lightSensor(7)
ledlight = light.light(3)
alarmclock = clock.Clock()
button = button.Button(12)
musicPlayer = musicPlayer.MusicPlayer('little_love_song.mp3')
curtain = curtain.curtain(10000)

# store instances into __builtin__
__builtin__.lightsensor = lightsensor
__builtin__.ledlight = ledlight
__builtin__.alarmclock = alarmclock
__builtin__.button = button
__builtin__.musicPlayer = musicPlayer
__builtin__.curtain = curtain

# for test, set the time of alarm clock
alarmclock.settingAlarmClock(0,23)

# start web ui (django)
webui.setEnv()
webui.runInBackGround()
webui.cleanEnv()

# main loop
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
				curtain.open()
				isplayingmusic = True

	if enableAlarm and button.isPressed():
		musicPlayer.stop()
		ismucicplaying = False
		enableAlarm=False

	if not enableAlarm and button.isPressed():
		alarmclock.settingAlarmClockToNextDay()
		enableAlarm=True

	time.sleep(0.1)
