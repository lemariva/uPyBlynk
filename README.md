# uPyBlynk
This project is about controlling a WiPy 2.0/3.0 or an ESP32 running MicroPython with [Blynk](https://www.blynk.cc/).

## Instructions
### Android
1. Install the [Android](https://play.google.com/store/apps/details?id=cc.blynk) or [iOS](https://itunes.apple.com/us/app/blynk-control-arduino-raspberry/id808760481) application
2. Create a New Project and choose as device the `WiPy`
3. Copy the `auth token`


### WiPy 3.0 / 2.0
1. Rename and upload the [`boot.py`](https://github.com/lemariva/ESP32MicroPython/blob/master/boot_wipy.py) file to the WiPy to connect your WI-FI. Do not forget to change the `<wlan-ssid>` and `<wlan-password>` with your SSID and the WPA2 password of your router
2. Change the `auth token` inside the `main.py` file
3. Upload the `BlynkLibWiPy.py` and the `main.py` files to the WiPy
4. Reboot the WiPy.

Check the WiPy 3.0 / 2.0 pinout [here](https://docs.pycom.io/datasheets/development/wipy3.html).

If you need some help to upload the files to the WiPy, follow this [tutorial](https://lemariva.com/blog/2017/10/micropython-getting-started).

### ESP32
0. Install MicroPython following this [tutorial](https://lemariva.com/blog/2017/10/micropython-getting-started).
1. Rename and upload the [`boot.py`](https://github.com/lemariva/ESP32MicroPython/blob/master/boot_esp32.py) file to the ESP32 to connect your WI-FI. Do not forget to change the `<wlan-ssid>` and `<wlan-password>` with your SSID and the WPA2 password of your router
2. Change the `auth token` inside the `main.py` file, and switch the corresponding `imports`
3. Upload the `BlynkLibESP32.py` and the `main.py` files to the ESP32
4. Reboot the ESP32.

Check the ESP32 pinout [here](https://docs.espressif.com/projects/esp-idf/en/latest/get-started/get-started-devkitc.html).

### Additional Configuration
* [Blynk examples](https://github.com/wipy/wipy/tree/master/examples/blynk)

## Changelog
* Revision 0.1a
	- it is still buggy
	- PWM, ADC, DO, DI working - some pins are not available

## Credits
* Based on [WiPy 1.0 Library](https://github.com/wipy/wipy/blob/master/lib/blynk/BlynkLib.py)
