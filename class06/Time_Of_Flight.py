from m5stack import *
from m5ui import *
from uiflow import *
import unit
from machine import *
from time import *
import random

# Setup and init
tof_unit = unit.get(unit.TOF,unit.PORTA) # Set up the TOF module
button_pin = Pin(39, Pin.IN)  # configure input on pin G39 (atom matrix display button)

# Timers
sensor_timer = ticks_ms()  # create a timer variable and save current time for the sensor
countdown_timer = ticks_ms() # create a timer for the ready countdown

# States
countdown_state = None # Set up a state variable for the countdown logic
program_state = 'READY' # variable to keep track of program state

# Variables
senstivity = 2 # Use this to define how far/close the player should be getting to the correct answer
max_distance = 1200 # The max distance that will be used for the playing distance range
min_distance = 100 # The min distance that will be used for the playing distance range
total_distance = max_distance - min_distance # Store a variable for the total interval distance for later calculation
button_value = None # Create a variable to store the button state
random_distance = None # Craete a global variable to store the generated random distance

# store all the matrix pattern
ready = [0,0xffffff,0xffffff,0xffffff,0,0xffffff,0,0,0,0xffffff,0xffffff,0,0xffffff,0,0xffffff,0xffffff,0,0,0,0xffffff,0,0xffffff,0xffffff,0xffffff,0]
digit_1 = [0,0xffffff,0xffffff,0,0,0,0,0xffffff,0,0,0,0,0xffffff,0,0,0,0,0xffffff,0,0,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff]
digit_2 = [0,0xffffff,0xffffff,0xffffff,0,0xffffff,0,0,0xffffff,0,0,0,0xffffff,0,0,0,0xffffff,0,0,0,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff]
digit_3 = [0,0xffffff,0xffffff,0xffffff,0,0,0,0,0xffffff,0,0,0,0xffffff,0,0,0,0,0,0xffffff,0,0,0xffffff,0xffffff,0xffffff,0]
success = [0,0,0,0,0,0,0,0,0,0x00ff1e,0,0,0,0x00ff1e,0,0x00ff1e,0,0x00ff1e,0,0,0,0x00ff1e,0,0,0]
upper = [0,0,0,0,0,0xff0000,0xff0000,0xff0000,0xff0000,0xff0000,0x00ff1e,0x00ff1e,0x00ff1e,0x00ff1e,0x00ff1e,0,0,0,0,0,0,0,0,0,0]
upper_50 = [0xff0000,0xff0000,0xff0000,0xff0000,0xff0000,0xff0000,0xff0000,0xff0000,0xff0000,0xff0000,0x00ff1e,0x00ff1e,0x00ff1e,0x00ff1e,0x00ff1e,0,0,0,0,0,0,0,0,0,0]
lower = [0,0,0,0,0,0,0,0,0,0,0x00ff1e,0x00ff1e,0x00ff1e,0x00ff1e,0x00ff1e,0xff0000,0xff0000,0xff0000,0xff0000,0xff0000,0,0,0,0,0]
lower_50 = [0,0,0,0,0,0,0,0,0,0,0x00ff1e,0x00ff1e,0x00ff1e,0x00ff1e,0x00ff1e,0xff0000,0xff0000,0xff0000,0xff0000,0xff0000,0xff0000,0xff0000,0xff0000,0xff0000,0xff0000]

# Set the init screen to indicate the system is ready
rgb.set_screen(ready)

while True:
    # input section
    # a non-stop timer to limit the frequency of the sensor
    if(ticks_ms() > sensor_timer + 50):
        tof_distance = tof_unit.distance # Get the sensor distance and store it 
        button_value = button_pin.value() # Get the button input and store it

        # debug section
        print("")
        print("Sensor distance: ", tof_distance)
        print("Random distance: ", random_distance)
        # print(light_state)
        # print(program_state)

    # calculation section
    if program_state == "READY":
        if button_value == 0: # when in button pressed down
            # start countdown
            # print ("Start countdown")
            countdown_state = 3 # Start the countdown from 3
            countdown_timer = ticks_ms() # Set the timer variable to the current ticks
        if(ticks_ms() > countdown_timer + 1000) and countdown_state != None: # when 1 second pass and the countdown has already happened
            countdown_timer = ticks_ms() # Set the timer to the variable again when 1 second pass
            countdown_state -= 1 # Countdown decrease by 1

    if program_state == "PLAYING":
        if tof_distance > random_distance + upper_distance * 0.5: # if the current sensor distance is greater than the generated random distance plus the 50% of the upper distance
            rgb.set_screen(upper_50)
        elif tof_distance > random_distance + senstivity: # if the current sensor distance is greater than the generated random distance
            rgb.set_screen(upper)  
        elif random_distance - senstivity <= tof_distance <= random_distance + senstivity: # if the current sensor distance fall in the range of the random distance +- the sensitivity
            program_state = "END" # Change the state to END
            # start the end countdown for transition to the READY state
            countdown_timer = ticks_ms()
        elif tof_distance > random_distance * 0.5: # if the current sensor distance is less than the 50% of the generated random distance
            rgb.set_screen(lower)
        elif tof_distance > 0: # if the current sensor distance is in the least distance range
            rgb.set_screen(lower_50)

    elif program_state == "END":
        rgb.set_screen(success) # Set the screen to the success screen
        if(ticks_ms() > countdown_timer + 3000): # A non-stop timer that will transit to READY state after 3 seconds
            program_state = "READY"
            rgb.set_screen(ready) 

    # output section
    if countdown_state == 3: 
        rgb.set_screen(digit_3)
    elif countdown_state == 2:
        rgb.set_screen(digit_2)
    elif countdown_state == 1:
        rgb.set_screen(digit_1)
    elif countdown_state == 0:
        program_state = "PLAYING" # when countdown finished, change the state to PLAYING
        countdown_state = None # reset the countdown state
        random_distance = random.randint(min_distance,max_distance) # generate a random distance every time we enter the PLAYING state to be the correct answer
        upper_distance = max_distance - random_distance # calculate the upper distance based on the max distance and the random distance
    
    