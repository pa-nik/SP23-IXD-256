from machine import Pin
from time import sleep_ms

led_pin_green = Pin(32, Pin.OUT)           # create output pin on G32 (4-pin bottom connector white wire)
led_pin_yellow = Pin(21, Pin.OUT)          # create output on pin G21 (4-pin back connector)
led_pin_red = Pin(25, Pin.OUT)             # create output on pin G25 (4-pin back connector)
button_pin = Pin(26, Pin.IN, Pin.PULL_UP)  # create pull-up input on pin G26 (yellow wire)

while True:
    led_pin_green.on()
    sleep_ms(500)
    led_pin_green.off()
    sleep_ms(500)

    led_pin_yellow.on()
    sleep_ms(500)
    led_pin_yellow.off()
    sleep_ms(500)

    led_pin_red.on()
    sleep_ms(500)
    led_pin_red.off()
    sleep_ms(500)
