import RPi.GPIO as GPIO
import sys
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

count=0

while (count < 10):
    count = count +1
    print(count)

    GPIO.output(19, GPIO.LOW)
    time.sleep(2)
    GPIO.output(26, GPIO.LOW)
    time.sleep(5)
    GPIO.output(26, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(19, GPIO.HIGH)

    time.sleep(10)