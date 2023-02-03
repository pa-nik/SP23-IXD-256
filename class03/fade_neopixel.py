from machine import Pin
from time import *
from neopixel import NeoPixel

neopixel_pin = Pin(26, Pin.OUT)  # create an output on pin G26
neopixel_strip = NeoPixel(neopixel_pin, 16)

neopixel_strip[0] = (255, 0, 0)  # set pixel at index 0 to red color
neopixel_strip.write()
