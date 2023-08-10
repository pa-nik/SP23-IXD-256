# digital output blink LED example for M5stack ATOM 

from m5stack import *
from machine import Pin
from time import *

led_pin = Pin(32, Pin.OUT)      # create output pin on G32 (white wire)

while True:
  led_pin.on()                  # set pin to "on" (high) level
  sleep_ms(500)                 # delay 
  led_pin.off()                 # set pin to "off" (low) level
  sleep_ms(500)                 # delay 
