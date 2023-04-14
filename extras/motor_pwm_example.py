# pulse-width modulated (PWM) output example for M5stack ATOM 
# tested with M5Stack Vibrator Motor: https://docs.m5stack.com/en/unit/vibrator

from m5stack import *
from machine import Pin, PWM
from time import *

motor_pwm = PWM(Pin(26))          # create PWM output on pin G26 (yellow wire)

while True:
    print('turn on vibration motor..')
    motor_pwm.duty(25)
    sleep_ms(500)
    print('turn off vibration motor..')
    motor_pwm.duty(0)
    sleep_ms(2000)
    
