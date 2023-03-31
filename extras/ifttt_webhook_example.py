from m5stack import *
from time import *
from machine import Pin, ADC
import wifiCfg  # wifi configuration library
import urequests

button_pin = Pin(39, Pin.IN)  # configure input on pin G39 (matrix display button)

# change arguments below to connect to the WiFi network, such as 'ACCD':
wifiCfg.doConnect('INSERT_NETWORK_NAME', 'INSERT_NETWORK_PASSWORD')  

# check WiFi connection status:
if wifiCfg.wlan_sta.isconnected():
    print('connected to WiFi network..')

while True:
    if(button_pin.value() == 0):    # if input pin is low:
        print('button pressed..')
        try:
            # post http request to ifttt:
            req = urequests.request(method='POST', url='http://maker.ifttt.com/trigger/INSERT_YOUR_IFTTT_EVENT_NAME/with/key/INSERT_YOUR_IFTTT_KEY',json={'value_name':'value'}, headers={'Content-Type':'application/json'})
            print('success!')
        except:
            print('fail..')
        sleep_ms(500)
    sleep_ms(500)
