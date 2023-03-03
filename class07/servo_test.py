from m5stack import *
from time import *
from machine import Pin, ADC
from servo import Servo
from easyIO import *

analog_pin = Pin(32, Pin.IN)  # configure input on pin G32 (white wire)
adc = ADC(analog_pin)  # create analog input on analog_pin
adc.atten(ADC.ATTN_11DB)  # enable full-range on ADC

print('servo test..')
servo_obj = Servo(Pin(26))  # create a Servo object on G26 (yellow wire)
# servo_obj.write_us(1400)  # move clockwise
# sleep_ms(2000)
# servo_obj.write_us(1600)  # move counter-clockwise
# sleep_ms(2000)
# servo_obj.write_us(1500)  # stop

while True:
    analog_val = adc.read()  # read analog value (0 - 4095 range)
    servo_val = map_value(analog_val, 0, 4095, 1000, 1500)
    servo_obj.write_us(servo_val)
    print(servo_val)
    sleep_ms(100)

