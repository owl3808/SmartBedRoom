# Import required libraries
import sys
import time
from threading import Thread
import RPi.GPIO as GPIO

class Stepper:
    def __init__(self): 
        # Using physical pin numbers
        GPIO.setmode(GPIO.BOARD)
         
        # Define GPIO signals to use
        self.StepPins = [13,15,16,18]
         
        # Set all pins as output
        for pin in self.StepPins:
            print "Setup pins"
            GPIO.setup(pin,GPIO.OUT)
            GPIO.output(pin, False)
         
        # Define advanced sequence
        # as shown in manufacturers datasheet
        self.Seq = [[1,0,0,0],
               [1,1,0,0],
               [0,1,0,0],
               [0,1,1,0],
               [0,0,1,0],
               [0,0,1,1],
               [0,0,0,1],
               [1,0,0,1]]
                
        self.StepCount = len(self.Seq)-1
        self.StepDir = 1 # Set to 1 or 2 for clockwise
                    # Set to -1 or -2 for anti-clockwise
        self.WaitTime = 10/float(1000)

    def setWaitTime(self, waittime):
        self.WaitTime = float(float(waittime)/1000)
        print "set waittime: %f" % self.WaitTime

    def setStepDir(self, stepdir):
	stepdir = int(stepdir)
        if stepdir <= 2 and stepdir >= -2 and stepdir != 0:
            self.StepDir = stepdir


    def stop(self):
        # Set all pins False
        for pin in self.StepPins:
            GPIO.output(pin, False)


    def run(self, round=0, no=0):
        # Initialise variables
        StepCounter = 0
        roundCounter = 0

        # Start main loop
        while True:
            for pin in range(0, 4):
                xpin = self.StepPins[pin]
                if self.Seq[StepCounter][pin]!=0:
                    #print " Step %i Enable %i" %(StepCounter,xpin)
                    GPIO.output(xpin, True)
                else:
                    GPIO.output(xpin, False)
           
            StepCounter += self.StepDir
            
            # If we reach the end of the sequence
            # start again and count round number
            if (StepCounter>self.StepCount):
                StepCounter = 0
                roundCounter += 1
            if (StepCounter<0):
                StepCounter = self.StepCount
                roundCounter += 1

            # if reach the setting round
            if round!=0 and roundCounter >= round:
		self.stop()
		break
	    
            # Wait before moving on
            time.sleep(self.WaitTime)

    def runInBackGround(self, round=0):
        self.thread = Thread(target=self.run, args=(round,0))
        self.thread.start()

if __name__ == '__main__':
	m = Stepper()
	m.setWaitTime(sys.argv[1])
	m.setStepDir(sys.argv[2])
	m.run()
