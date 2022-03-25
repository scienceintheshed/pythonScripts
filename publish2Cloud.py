"""
'publish.py'
=========================================
Publishes an incrementing value to a feed

Author(s): Brent Rubell, Todd Treece for Adafruit Industries
"""
# Import standard python modules
import time
from datetime import datetime
import random
import sys

print("Adafruit publish",datetime.now())

temp=sys.argv[1]
humid=sys.argv[2]
#pressure=sys.argv[3]
NOAE=sys.argv[3]
NOWE=sys.argv[4]
NO2AE=sys.argv[5]
NO2WE=sys.argv[6]

# Import Adafruit IO REST client.
from Adafruit_IO import Client, Feed

ADAFRUIT_IO_KEY = 'cadd84023ad044f2be4e79d711da38e8'
ADAFRUIT_IO_USERNAME = 'simos_iot'

# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

try:
    aio.send_data('biocatalytic-coatings.temperature', temp)
    aio.send_data('biocatalytic-coatings.humidity', humid)
    #aio.send_data('biocatalytic-coatings.pressure', pressure)
    aio.send_data('biocatalytic-coatings.nowe', NOWE)
    aio.send_data('biocatalytic-coatings.noae', NOAE)
    aio.send_data('biocatalytic-coatings.no2we', NO2WE)
    aio.send_data('biocatalytic-coatings.no2ae', NO2AE)
    #time.sleep(10)
    print("Data sent...")
except:
    print("An error occurred.")
