from m5stack import *  # import m5stack libraries
import unit  # import m5stack unit library 
from machine import Pin, ADC
from time import *
from neopixel import NeoPixel

tof_sensor = unit.get(unit.TOF, unit.PORTA)
question_mark = [
    0, 0xff0000, 0xff0000, 0xff0000, 0,
    0, 0,        0,        0xff0000, 0,
    0, 0,        0xff0000, 0xff0000, 0,
    0, 0,        0,        0,        0,
    0, 0,        0xff0000, 0,        0]
rgb.set_screen(question_mark)

neopixel_pin = Pin(27, Pin.OUT)  # configure output on pin G27 (atom matrix display)
neopixel_display = NeoPixel(neopixel_pin, 25)  # create NeoPixel object with 25 pixels

# map an input value (v_in) between min/max ranges:
def map_value(in_val, in_min, in_max, out_min, out_max):
    v = out_min + (in_val - in_min) * (out_max - out_min) / (in_max - in_min)
    if (v < out_min): 
        v = out_min 
    elif (v > out_max): 
        v = out_max
    return int(v)

while True:
    d = tof_sensor.distance  # get distance from ToF sensor
    brightness = map_value(d, in_min = 0, in_max = 8192, out_min = 0, out_max = 255)
    #print(d)
    print(brightness)
    '''
    # change of brightness of 25 pixels using ToF value:
    for pixel_index in range(25):
        r = (brightness, 0, 0)  # red color that changes with ADC value
        neopixel_display[pixel_index] = r  # assign pixel to red color
    neopixel_display.write()  # write color data to neopixels
    '''
    sleep_ms(50)
