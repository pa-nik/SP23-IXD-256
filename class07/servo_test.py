from m5stack import *
from time import *
from machine import Pin
from servo import Servo

servo_obj = Servo(Pin(26))  # create a Servo object on G26 (yellow wire)
servo_obj.write_us(1400)  # move clockwise
sleep_ms(2000)
servo_obj.write_us(1600)  # move counter-clockwise
sleep_ms(2000)
servo_obj.write_us(1500)  # stop