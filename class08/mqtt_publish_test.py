from m5stack import *
from time import *
from machine import Pin, ADC
from easyIO import *
import wifiCfg  # wifi configuration library
from m5mqtt import M5mqtt  # M5Stack MQTT library

analog_pin = Pin(32, Pin.IN)  # configure input on pin G32 (white wire)
adc = ADC(analog_pin)  # create analog input on analog_pin
adc.atten(ADC.ATTN_11DB)  # enable full-range on ADC

# change arguments below to connect to the WiFi network, such as 'ACCD':
wifiCfg.doConnect('INSERT_NETWORK_NAME', 'INSERT_NETWORK_PASSWORD')  

# create the MQTT feed by inserting your Adafruit IO username and key:
mqtt_feed = M5mqtt(
    client_id = 'testclient',  # any name for your device (MQTT client)
    server = 'io.adafruit.com',  # MQTT broker address
    port = 1883,  # port to use for the connection
    user = 'INSERT_ADAFRUIT_IO_USERNAME',  # your Adafruit IO username 
    password = 'INSERT_ADAFRUIT_IO_KEY',  # your Adafruit IO key (check yellow key icon)
    keepalive = 300  # keep alive timeout  
)
mqtt_feed.start()

while True:
    analog_val = adc.read()  # read analog value (0 - 4095 range)
    print(analog_val)
    # change your username and feed name to publish sensor data to the feed:
    mqtt_feed.publish('INSERT_ADAFRUIT_IO_USERNAME/feeds/INSERT_ADAFRUIT_IO_FEED', str(analog_val))
    sleep_ms(3000)

