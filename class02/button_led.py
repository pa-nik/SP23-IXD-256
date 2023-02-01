# digital input with LED output example for M5stack ATOM 

from m5stack import *
from machine import Pin

led_pin = Pin(32, Pin.OUT)        # create output pin on G32 (white wire)
button_pin = Pin(26, Pin.IN, Pin.PULL_UP)  # create pull-up input on pin G26 (yellow wire)

while True:
  if(button_pin.value() == 0):    # if input pin is low:
    led_pin.on()                  # set pin to "on" (high) level
  else:                           # else input pin is high:
    led_pin.off()                 # set pin to "off" (low) level
  wait_ms(100)                    # delay 
