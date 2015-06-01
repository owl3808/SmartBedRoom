from datetime import datetime, timedelta


class Clock:
	def __init__(self, alarmtime='0800', daystart='0600', nightstart='1800'):
		h, m = self.changeStringToTime(alarmtime)
		self.settingAlarmClock(h, m)

	def changeStringToTime(self, timeString):
		hour = int(timeString[0:2])
		minute = int(timeString[2:4])
		return hour, minute

	def settingAlarmClock(self, hour, minute):
		now = datetime.now()
		if now < now.replace(hour=hour, minute=minute):
			self.alarmtime = now.replace(hour=hour, minute=minute)
		else:
			self.alarmtime = now.replace(hour=hour, minute=minute) + timedelta(days=1)
		print 'set alarm clock at %d/%d/%d %02d:%02d' % (self.alarmtime.year, self.alarmtime.month, self.alarmtime.day, self.alarmtime.hour, self.alarmtime.minute)

	def getAlarmClock(self):
		print "%d:%d" % (self.alarmtime.hour, self.alarmtime.minute)

	def isAchiveAlarmTime(self):
		return datetime.now() > self.alarmtime

	def settingAlarmClockToNextDay(self):
		self.settingAlarmClock(self.alarmtime.hour ,self.alarmtime.minute)
		
if __name__ == '__main__':
	import time
	c=Clock()
	c.settingAlarmClock(0,9)
	print c.getAlarmClock()
	while True:
		print datetime.now()
		print c.isAchiveAlarmTime()
		time.sleep(1)
	
