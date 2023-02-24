# IMU example (using the built-in Intertial Measurement Unit)
from m5stack import *  # import m5stack libraries
from time import *
import unit  # import m5stack unit library 
import imu  # imports m5stack imu unit

imu_sensor = imu.IMU()

left_arrow = [0,0,0,0xffffff,0,0,0,0xffffff,0,0,0,0xffffff,0,0,0,0,0,0xffffff,0,0,0,0,0,0xffffff,0]
right_arrow = [0,0xffffff,0,0,0,0,0,0xffffff,0,0,0,0,0,0xffffff,0,0,0,0xffffff,0,0,0,0xffffff,0,0,0]

while True:
    acc_x = imu_sensor.acceleration[0]
    print(acc_x)
    sleep_ms(100)