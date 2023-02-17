from machine import Pin, ADC
from time import *
from neopixel import NeoPixel

analog_pin = Pin(32, Pin.IN)  # configure input on pin G32 (white wire)
adc = ADC(analog_pin)  # create analog-to-digital converter (ADC) input
adc.atten(ADC.ATTN_11DB)  # set 11dB attenuation (2.45V range)

neopixel_pin = Pin(27, Pin.OUT)  # configure output on pin G27 (atom matrix display)
neopixel_strip = NeoPixel(neopixel_pin, 25)  # create NeoPixel object with 25 pixels

# light sensor calibration
sensor_timer = ticks_ms()  # create a timer variable and save current time
program_state = 'CALIBRATION' # variable to keep track of program state
calibration_val = 0  # sensor calibration value
analog_val_adjusted = 0  # adjusted sensor value
button_pin = Pin(39, Pin.IN)  # configure input on pin G39 (atom matrix display button)

# define pixel maps for digits 0 and 1:
digit_0 = [
    0,1,1,1,0,
    0,1,0,1,0,
    0,1,0,1,0,
    0,1,0,1,0,
    0,1,1,1,0
]
digit_1 = [
    0,1,1,0,0,
    0,0,1,0,0,
    0,0,1,0,0,
    0,0,1,0,0,
    0,1,1,1,0
]
# define some colors:
red_color = (100, 0, 0)
black_color = (0, 0, 0)

# define a function to get color for a pixel:
def get_pixel_color(n):
    if(n == 0):
        return black_color
    else:
        return red_color
    
# define a function to display a digit:
def display_digit(n):
    for i in range(25):
        if(n == 0):
            neopixel_strip[i] = get_pixel_color(digit_0[i])
        else:
            neopixel_strip[i] = get_pixel_color(digit_1[i])
    neopixel_strip.write()
    
# map an input value (v_in) between min/max ranges:
def map_value(in_val, in_min, in_max, out_min, out_max):
    v = out_min + (in_val - in_min) * (out_max - out_min) / (in_max - in_min)
    if (v < out_min): 
        v = out_min 
    elif (v > out_max): 
        v = out_max
    return int(v)

while True:
    if(ticks_ms() > sensor_timer + 100):
        analog_val = adc.read()  # read 12-bit analog value (0 - 4095 range)
        analog_val_8bit = map_value(analog_val, in_min = 0, in_max = 4095, out_min = 0, out_max = 255)
        #print(analog_val)
        #print(analog_val_8bit)
        # changing how many neopixels are colored using ADC value:
        # map ADC value from 0 - 4095 range to 0 - 30
        analog_val_25 = map_value(analog_val, 0, 4095, out_min = 0, out_max = 25)
        

        if(program_state == 'CALIBRATION'):
            if(button_pin.value() == 0):  # button_pin is low
                calibration_val = analog_val
                print('calibration finished..')
                program_state = 'DEFAULT'
                print('change program_state to ' + program_state)
        elif(program_state == 'DEFAULT'):
            # adjust sensor reading using calibration value:
            analog_val_adjusted = analog_val - calibration_val
            # make sure adjusted value is never negative:
            if(analog_val_adjusted < 0):
                analog_val_adjusted = 0
            analog_val_25 = map_value(analog_val_adjusted, 0, 4095, 0, 25)
        
            #print(analog_val_25)
            #print(f'{analog_val} {calibration_val}')
            #print('analog_val = ' + str(analog_val))
            #print(f'analog_val = {analog_val}')
            print(analog_val, calibration_val)
            
            if(analog_val > calibration_val + 100):
                display_digit(1)
            else:
                display_digit(0)

        '''
        for pixel_index in range(25):
            if(pixel_index < analog_val_25):  # pixel index is less than ADC value
                neopixel_strip[pixel_index] = (255, 0, 0)
            else:
                neopixel_strip[pixel_index] = (0, 0, 0)
        neopixel_strip.write()  # write color data to neopixels
        '''
        '''
        # change of brightness of 30 pixels using ADC value:
        for pixel_index in range(25):
            r = (analog_val_8bit, 0, 0)  # red color that changes with ADC value
            neopixel_strip[pixel_index] = r  # assign pixel to red color
        neopixel_strip.write()  # write color data to neopixels
        '''
        #sleep_ms(100)
        sensor_timer = ticks_ms()  # update sensor timer