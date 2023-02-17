from mpu6886 import MPU6886
from neopixel import NeoPixel
from machine import Pin, SoftI2C
from time import sleep
from math import *

# Definitions for the ATOM Matrix
LED_GPIO = const(27)
MPU6886_SCL = const(21)
MPU6886_SDA = const(25)
matrix_size_x = const(5)
matrix_size_y = const(5)
is_atom_matrix = True

# Definitions for the M5StickC + NeoFlash hat
#LED_GPIO = const(26)
#MPU6886_SCL = const(22)
#MPU6886_SDA = const(21)
#matrix_size_x = const(18)
#matrix_size_y = const(7)
#is_atom_matrix = False

threshold = const(5) # minimum angle that triggers movement 
color = (0, 0, 20) # Initial color: Blue
x = int(matrix_size_x / 2) # Get matrix
y = int(matrix_size_y / 2) # center
np = NeoPixel(Pin(LED_GPIO), matrix_size_x * matrix_size_y)

def computeAngles(ax,ay,az):
    # https://roboticsclubiitk.github.io/2017/12/21/Beginners-Guide-to-IMU.html
    pitch = 180 * atan (ax/sqrt(ay**2 + az**2))/ pi
    roll = 180 * atan (ay/sqrt(ax**2 + az**2))/ pi
    yaw = 180 * atan (az/sqrt(ax**2 + ay**2))/ pi
    return pitch, roll, yaw

def updateDot(p, angle, size, threshold, color1, color2):
    global color
    if angle > threshold:     # Test if angle is positive
        if p < size - 1:      # If it is not at the matrix
            p = p + 1         # border, move the dot
        else:
            color = color1    # change color if reached the border
    elif angle < - threshold: # Test if angle is negative
        if p > 0:             # If it is not at the matrix
            p = p - 1         # border, move the dot
        else:
            color = color2    # change color if reached the border
    return p

# I2C bus init for MPU6886
i2c = SoftI2C(scl=Pin(MPU6886_SCL), sda=Pin(MPU6886_SDA))

# Values you can use to initialize the accelerometer. AFS_16G, means +-8G sensitivity, and so on
# Larger scale means less precision
AFS_2G      = const(0x00)
AFS_4G      = const(0x01)
AFS_8G      = const(0x02)
AFS_16G     = const(0x03)

# Values you can use to initialize the gyroscope. GFS_2000DPS means 2000 degrees per second sensitivity, and so on
# Larger scale means less precision
GFS_250DPS  = const(0x00)
GFS_500DPS  = const(0x01)
GFS_1000DPS = const(0x02)
GFS_2000DPS = const(0x03)  

# by default, if you initialize MPU6886 with  imu = MPU6886(i2c), GFS_2000DPS and AFS_8G are used
# if you want to initialize with other values you have too use :
# imu = MPU6886(i2c,mpu6886.GFS_250DPS,mpu6886.AFS_4G )
# imu = MPU6886(i2c) #=> use default 8G / 2000DPS
imu = MPU6886(i2c, GFS_500DPS, AFS_4G)

# in order to calibrate Gyroscope you have to put the device on a flat surface
# preferably level with the floor and not touch it during the procedure. (1s for 20 cycles)
#calibrateGyro(20)

while True:
    ax,ay,az = imu.getAccelData()
#    gx,gy,gz = imu.getGyroData()
    pitch, roll, yaw = computeAngles(ax,ay,az)
#    print(ax,ay,az)
#    print(pitch, roll, yaw)
    np[ y * matrix_size_x + x ] = (0,0,0) # Turn off the LED on the current dot possition
    if is_atom_matrix:
        x = updateDot(x, pitch, matrix_size_x, threshold, (20, 0, 0), (20, 20, 0))
        y = updateDot(y, roll, matrix_size_y, threshold, (20, 0, 20), (0, 20, 20))
    else:  # Compensate for the different orientation of the sensor on the M5StickC
        x = updateDot(x, -roll, matrix_size_x, threshold, (20, 0, 0), (20, 20, 0))
        y = updateDot(y, pitch, matrix_size_y, threshold, (20, 0, 20), (0, 20, 20))
    np[ y * matrix_size_x + x ] = color # Turn on the LED on the new dot possition
    np.write()
    sleep(0.2)