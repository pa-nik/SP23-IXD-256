from machine import Pin, ADC
from time import *
from neopixel import NeoPixel

analog_pin = Pin(32, Pin.IN)  # configure input on pin G32 (white wire)
adc = ADC(analog_pin)  # create analog-to-digital converter (ADC) input
adc.atten(ADC.ATTN_11DB)  # set 11dB attenuation (2.45V range)

neopixel_pin = Pin(27, Pin.OUT)  # configure output on pin G27 (atom matrix display)
neopixel_strip = NeoPixel(neopixel_pin, 25)  # create NeoPixel object with 25 pixels

# map an input value (v_in) between min/max ranges:
def map_value(in_val, in_min, in_max, out_min, out_max):
    v = out_min + (in_val - in_min) * (out_max - out_min) / (in_max - in_min)
    if (v < out_min): 
        v = out_min 
    elif (v > out_max): 
        v = out_max
    return int(v)

while True:
    analog_val = adc.read()  # read 12-bit analog value (0 - 4095 range)
    analog_val_8bit = map_value(analog_val, in_min = 0, in_max = 4095, out_min = 0, out_max = 255)
    #print(analog_val)
    #print(analog_val_8bit)
    # changing how many neopixels are colored using ADC value:
    # map ADC value from 0 - 4095 range to 0 - 30
    analog_val_25 = map_value(analog_val, 0, 4095, out_min = 0, out_max = 25)
    print(analog_val_25)
    
    for pixel_index in range(25):
        if(pixel_index < analog_val_25):  # pixel index is less than ADC value
            neopixel_strip[pixel_index] = (255, 0, 0)
        else:
            neopixel_strip[pixel_index] = (0, 0, 0)
    neopixel_strip.write()  # write color data to neopixels
    '''
    # change of brightness of 30 pixels using ADC value:
    for pixel_index in range(25):
        r = (analog_val_8bit, 0, 0)  # red color that changes with ADC value
        neopixel_strip[pixel_index] = r  # assign pixel to red color
    neopixel_strip.write()  # write color data to neopixels
    '''
    sleep_ms(100)