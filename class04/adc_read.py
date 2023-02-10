from machine import Pin, ADC
from time import *

analog_pin = Pin(32, Pin.IN)  # configure input on pin G32 (white wire)
adc = ADC(analog_pin)  # create analog-to-digital converter (ADC) input
adc.atten(ADC.ATTN_11DB)  # set 11dB attenuation (2.45V range)

while True:
    analog_val = adc.read()  # read 12-bit analog value (0 - 4095 range)
    print(analog_val)
    sleep_ms(100)