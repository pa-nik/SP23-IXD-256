from m5stack import *
from m5stack_ui import *
from uiflow import *
import wifiCfg  # wifi configuration library
import urequests, json
import unit
from time import *

screen = M5Screen()
screen.clean_screen()

label0 = M5Label('label0', x=20, y=20, color=0x000000, font=FONT_MONT_14, parent=None)
label1 = M5Label('label1', x=20, y=40, color=0x000, font=FONT_MONT_14, parent=None)
tof_0 = unit.get(unit.TOF, unit.PORTA)

# change arguments below to connect to the WiFi network, such as 'ACCD':
wifiCfg.doConnect('INSERT_NETWORK_NAME', 'INSERT_NETWORK_PASSWORD') 

# check WiFi connection status:
if wifiCfg.wlan_sta.isconnected():
    #print('connected to WiFi network..')
    screen.set_screen_bg_color(0x0000FF)  # blue screen

try:
    # get 'dateTime' with timeapi.io:
    req = urequests.get(url='https://timeapi.io/api/Time/current/zone?timeZone=America/Los_Angeles') 
    req_data = req.json()
    datetime = req_data['dateTime']
    # get 'datetime' with worldtimeapi.org:
    #req = urequests.request(method='GET', url='https://www.worldtimeapi.org/api/timezone/America/Los_Angeles', headers={'Content-Type':'application/json'})
    #req_data = req.json()
    #datetime = req_data['datetime']
    #print('datetime:', datetime)
    screen.set_screen_bg_color(0x00FF00)  # green screen
    label0.set_text(datetime)
    #print('success!')
except:
    screen.set_screen_bg_color(0xFF0000)  # red screen
    #print('fail..')
    
while True:
    label1.set_text('distance = ' + str(tof_0.distance))
    sleep_ms(100)
  