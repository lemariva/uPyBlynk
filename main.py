import pycom                        # only WIPY 2.0/3.0
import BlynkLibWiPy as BlynkLib     # for WIPY 2.0/3.0
#import BlynkLibESP32 as BlynkLib   # for ESP32

# initialize Blynk
blynk = BlynkLib.Blynk("< auth tokens >")

# start Blynk (this call should never return)
pycom.heartbeat(False)              # only WIPY 2.0/3.0

blynk.run()
