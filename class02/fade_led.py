# pulse-width modulated (PWM) output LED example for M5stack ATOM 

from m5stack import *
from machine import Pin, PWM
from time import *

led_pwm = PWM(Pin(32))          # create PWM output on pin G32 (white wire)

while True:
  for i in range(100):
    led_pwm.duty(i)             # set PWM duty cycle 
    #wait_ms(10)                 # delay 
    sleep_ms(10)
  for i in range(100):
    led_pwm.duty(100-i)         # set PWM duty cycle 
    #wait_ms(10)                 # delay 
    sleep_ms(10)
  sleep_ms(100)
  print('hello!')
