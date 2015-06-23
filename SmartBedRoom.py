import os, time, __builtin__
import light, lightSensor, clock, musicPlayer, button, webui, curtain
import RPi.GPIO as GPIO
GPIO.setwarnings(False)

# variables
__builtin__.enableAlarm = True
isplayingmusic = False

# create instance of modules
lightsensor = lightSensor.lightSensor(7)
ledlight = light.light(3)
alarmclock = clock.Clock()
button = button.Button(12)
musicPlayer = musicPlayer.MusicPlayer('little_love_song.mp3')
curtain = curtain.curtain(700)

# store instances into __builtin__
__builtin__.lightsensor = lightsensor
__builtin__.ledlight = ledlight
__builtin__.alarmclock = alarmclock
__builtin__.button = button
__builtin__.musicPlayer = musicPlayer
__builtin__.curtain = curtain

# for test, set the time of alarm clock
alarmclock.settingAlarmClock(8,0)

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
	
	if __builtin__.enableAlarm:
		if alarmclock.isAchiveAlarmTime():
			if not isplayingmusic:
				print 'alarmclock: alarming!'
				musicPlayer.play()
				curtain.open()
				isplayingmusic = True

	if __builtin__.enableAlarm and button.isPressed():
		musicPlayer.stop()
		isplayingmusic = False
		__builtin__.enableAlarm=False

	if not __builtin__.enableAlarm and button.isPressed():
		alarmclock.settingAlarmClockToNextDay()
		__builtin__.enableAlarm=True

	time.sleep(0.1)
