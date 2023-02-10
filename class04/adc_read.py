from machine import Pin, ADC
from time import *

analog_pin = Pin(32, Pin.IN)  # configure input on pin G32 (white wire)
adc = ADC(analog_pin)  # create analog-to-digital converter (ADC) input
adc.atten(ADC.ATTN_11DB)  # set 11dB attenuation (2.45V range)

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
    print(analog_val_8bit)
    sleep_ms(100)