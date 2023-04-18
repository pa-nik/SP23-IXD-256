# Button counter example for M5Stack Atom Matrix
# press the display button to trigger 3, 2, 1, Go! printed to terminal
# press the display button again to reset counter and program state

from m5stack import *
from machine import Pin
from time import *

program_state = 'start'
counter = 3

# create pull-up input on pin G39 (Atom Matrix display button):
button_pin = Pin(39, Pin.IN, Pin.PULL_UP)  

# display red square:
rgb.set_screen([0,0,0,0,0,0,0xff0000,0xff0000,0xff0000,0,0,0xff0000,0,0xff0000,0,0,0xff0000,0xff0000,0xff0000,0,0,0,0,0,0])

while True: 
    if(program_state == 'start'):
        if(button_pin.value() == 0):  # button pressed
            program_state = 'countdown'
            # display yellow square:
            rgb.set_screen([0,0,0,0,0,0,0xffff00,0xffff00,0xffff00,0,0,0xffff00,0,0xffff00,0,0,0xffff00,0xffff00,0xffff00,0,0,0,0,0,0])
            sleep_ms(1000)

    elif(program_state == 'countdown'):
        print(counter)
        if(counter > 0):
            counter -= 1
        else:
            print('Go!')
            program_state = 'go'
            # display green square:
            rgb.set_screen([0,0,0,0,0,0,0x00ff00,0x00ff00,0x00ff00,0,0,0x00ff00,0,0x00ff00,0,0,0x00ff00,0x00ff00,0x00ff00,0,0,0,0,0,0])
        sleep_ms(1000)
        
    elif(program_state == 'go'):
        if(button_pin.value() == 0):  # button pressed
            # reset counter and program state:
            program_state = 'start'
            counter = 3
            print(counter)
            # display red square:
            rgb.set_screen([0,0,0,0,0,0,0xff0000,0xff0000,0xff0000,0,0,0xff0000,0,0xff0000,0,0,0xff0000,0xff0000,0xff0000,0,0,0,0,0,0])
            sleep_ms(1000)
            
        