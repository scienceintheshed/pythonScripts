#
#   Program name    |   getGas.py
#   Written by      |   Steven Owen
#   Date            |   January 2021
#   Version         |   1.0
#
#   Description     |   A program to read electrode responses from an Alphasense AFE through the
#                       South Coast SCience DFE via a Raspberry Pi4.
#
#   Comments        |   This version is functionally correctly.  Try loops with error handling
#                       for connection errors have been included.
#                       
#                       Version 1.0 : This is an update to Gas.py and Gas2.py but convberted to a single
#                       script.  The c# calling program has been rewritten such that the same
#                       function calls multiple python scripts and handles the output based
#                       on the returned data.

#   Import necessary libraries.
import time
from datetime import datetime, timedelta
import socket
import sys
import os
import re
# from Adafruit_Python_ADS1x15 import ADS1x15
import ADS1x15

filename = sys.argv[1]
myPin = int(sys.argv[2])
gpioState = int(sys.argv[3])
samplingTime = int(sys.argv[4])

# Create ADS1115 ADC (16-bit) instances.
adcFE = ADS1x15.ADS1115(address=0x48, busnum=1) # FE prefix = Forty Eight (Auxilliary Electrode)
adcFN = ADS1x15.ADS1115(address=0x49, busnum=1) # FN prefix = Forty Nine  (Working Electrode)
GAIN=8

# Now we will create a loop to average the electrode readings. The number of samples to average is
# set in the calling program and passed to this script as sys.argv[1]. We take electrode readings at
# 1Hz. There is a delay that uses the millis approach for each cycle.

count = 0
#samplingTime = 60
FEvalues = [0]*4
FNvalues = [0]*4

while (count < samplingTime):
        futureTime = datetime.now() + timedelta(milliseconds=1000)
        count = count +1
        FEvalues[3] = FEvalues[3]+adcFE.read_adc(3, gain=GAIN)
        FNvalues[3] = FNvalues[3]+adcFN.read_adc(3, gain=GAIN)
        FEvalues[2] = FEvalues[2]+adcFE.read_adc(2, gain=GAIN)
        FNvalues[2] = FNvalues[2]+adcFN.read_adc(2, gain=GAIN)
        dt=datetime.now()
        # Force a 1 second delay between readings
        while (dt < futureTime):
                dt=datetime.now()

NO2_WE=round((FNvalues[3]*4.096/count)/(32768*GAIN),5)
NO2_AE=round((FEvalues[3]*4.096/count)/(32768*GAIN),5)
NO_WE=round((FNvalues[2]*4.096/count)/(32768*GAIN),5)
NO_AE=round((FEvalues[2]*4.096/count)/(32768*GAIN),5)

print(NO_WE)
print(NO_AE)
print(NO2_WE)
print(NO2_AE)
