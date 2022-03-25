import ADS1x15

adcFE = ADS1x15.ADS1115(address=0x48, busnum=1) # FE prefix = Forty Eight (Auxilliary Electrode)
adcFN = ADS1x15.ADS1115(address=0x49, busnum=1) # FN prefix = Forty Nine  (Working Electrode)
GAIN=8