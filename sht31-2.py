import smbus
import time
print("Starting...")
 
# Get I2C bus
bus = smbus.SMBus(1)
 
# SHT31 address, 0x44(68)
while (True):
    count = 0
    humidity = 0
    humid = 0
    while count < 20:
        try:
            bus.write_i2c_block_data(0x44, 0x2C, [0x06])
             
            time.sleep(0.5)
             
            # SHT31 address, 0x44(68)
            # Read data back from 0x00(00), 6 bytes
            # Temp MSB, Temp LSB, Temp CRC, Humididty MSB, Humidity LSB, Humidity CRC
            data = bus.read_i2c_block_data(0x44, 0x00, 6)
             
            # Convert the data
            #temp = data[0] * 256 + data[1]
            #cTemp = -45 + (175 * temp / 65535.0)
            #Temp = -49 + (315 * temp / 65535.0)
            humidity = 100 * (data[3] * 256 + data[4]) / 65535.0
            #print(humidity)
            #humid += humidity*0.9171-0.1934
            humid += humidity
            count += 1
            time.sleep(0.1)
        
        except:
            pass
             
            # Output data to screen
            #print "Temperature in Celsius is : %.2f C" %cTemp
            #print "Temperature in Fahrenheit is : %.2f F" %fTemp
            #print "Relative Humidity is : %.2f %%RH" %humidity

        #print (" {:.2F}".format(cTemp))
        #print (" {:.2F}".format(humidity*1.3141-13.642))
        print (" {:.2F}".format(humidity*0.9338 - 2.0081))
        #print (" {:.2F}".format(humid/count))
        #print ("")
        
        time.sleep(5)
