import motor

class curtain:
	def __init__(self, roundofmotor, openstep=2):
	# roundofmotor: the round of stepmotor that needed to close/open the curtain
	# openstop: the stepdir of stepper, 1 slow, 2 faster, -1 -2 inverse direction slow and fast
		self.curtainmotor = motor.Stepper()
		self.curtainmotor.setWaitTime(1)
		self.roundOfMotor = roundofmotor
		self.openStep = openstep
		self.closeStep = openstep * (-1)
		print self.closeStep

	def open(self):
		self.curtainmotor.setStepDir(2)
		self.curtainmotor.runInBackGround(self.roundOfMotor)

	def close(self):
		self.curtainmotor.setStepDir(-2)
		self.curtainmotor.runInBackGround(self.roundOfMotor)

if __name__ == '__main__':
	import time
	mycurtain = curtain(1000)
	mycurtain.open()
	print 'curtain opening'
	time.sleep(10)
	mycurtain.close()
	print 'curtain closing'
