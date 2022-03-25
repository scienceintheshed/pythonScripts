import RPi.GPIO as GPIO
import sys

#filename = sys.argv[1]
myPin = int(sys.argv[2])
gpioState = int(sys.argv[3])
#samplingTime = int(sys.argv[4])

#programType = sys.argv[5]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(myPin, GPIO.OUT)

GPIO.output(myPin, gpioState)
