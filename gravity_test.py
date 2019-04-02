import os
import time
import math
import board
import busio
import adafruit_lsm9ds1
import adafruit_lis3dh

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_lsm9ds1.LSM9DS1_I2C(i2c)
#sensor = adafruit_lis3dh.LIS3DH_I2C(i2c)

def detect_gravity (num_readings):
    total = 0
    for reading in range (0,num_readings):
        m = get_magnitude(0)
        print(m)
        total += m
        time.sleep(0.1)
    return total / num_readings

def get_magnitude (gravity):
    (x,y,z) = sensor.acceleration
    return abs(math.sqrt(x**2 + y**2 + z**2)-gravity)

if __name__ == "__main__":
    time.sleep(1)
    g = detect_gravity(20)
    print("Gravity = ", g, "m/s^2")
    input("Press enter to go to live readout.")
    while True:
        os.system("clear")
        print(get_magnitude(g))
        time.sleep(0.1)

