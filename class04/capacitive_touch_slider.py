from machine import TouchPad, Pin
from time import *
from neopixel import NeoPixel

# variables
pixel_used = 30 # Desired number of pixels on the strip
max_cap_value = 690 #The maximum value of the capacitive sensing
min_cap_value = 650 #The minimum value of the capacitive sensing

# Setup
touch = TouchPad(Pin(33)) # Set the Pin 33 as the touch pin
neopixel_pin = Pin(26, Pin.OUT)  # create an output on pin G26
neopixel_strip = NeoPixel(neopixel_pin, pixel_used) # Initialize the led strip

# To map the input value to certain range, output will be interger
def IntergerConvert(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

while True:
    # Clear out the strip at the beginning
    for i in range(pixel_used):
        neopixel_strip[i] = (0,0,0)

    # Read the value and map it to the number of desired pixels
    loop_range = IntergerConvert(touch.read(),min_cap_value,max_cap_value,0,pixel_used)

    # Restrict the loop_range to avoid memory leaks
    if loop_range > pixel_used:
        loop_range = pixel_used
    if loop_range < 0:
        loop_range = 0

    # Light up the led strip based on the calculated loop_range
    for i in range(loop_range):
        neopixel_strip[i] = (125,0,0)
    
    # Write to the led strip
    neopixel_strip.write()

    #Debug section
    print("Capacitive reading:",touch.read())  
    print("Pixel light up:",loop_range)
    print("")

    # Restrict the running speed with 100 ms
    sleep_ms(100)