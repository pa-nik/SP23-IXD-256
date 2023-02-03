from machine import Pin
from time import *

led_pin_green = Pin(32, Pin.OUT)           # create output pin on G32 (4-pin bottom connector white wire)
led_pin_yellow = Pin(21, Pin.OUT)          # create output on pin G21 (4-pin back connector)
led_pin_red = Pin(25, Pin.OUT)             # create output on pin G25 (4-pin back connector)
button_pin = Pin(26, Pin.IN, Pin.PULL_UP)  # create pull-up input on pin G26 (yellow wire)

timer_ms = ticks_ms()  # create a timer variable and save current time
program_state = 'GREEN'

while True:
    if(ticks_ms() > timer_ms + 500):
        if(program_state == 'GREEN'):
            led_pin_green.off()
            led_pin_yellow.on()
            program_state = 'YELLOW'
            print(program_state)
        elif(program_state == 'YELLOW'):
            led_pin_yellow.off()
            led_pin_red.on()
            program_state = 'RED'
            print(program_state)
        elif(program_state == 'RED'):
            led_pin_red.off()
            led_pin_green.on()
            program_state = 'GREEN'
            print(program_state)
        timer_ms = ticks_ms()
