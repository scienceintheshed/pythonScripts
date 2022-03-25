import RPi.GPIO as GPIO
import sys
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)

GPIO.output(19, GPIO.LOW)
GPIO.output(26, GPIO.LOW)