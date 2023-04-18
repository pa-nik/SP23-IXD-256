# Simple counter example 
# 3, 2, 1, Go! are printed to terminal continously at 1 sec interval

from m5stack import *
from machine import Pin
from time import *

counter = 3

while True: 
    if(counter > 0):
        print(counter)
        counter -= 1
    else:
        print('Go!')
        counter = 3
    sleep_ms(1000)
    
            
        