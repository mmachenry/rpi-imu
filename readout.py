# Started from https://learn.adafruit.com/adafruit-lsm9ds1-accelerometer-plus-gyro-plus-magnetometer-9-dof-breakout/python-circuitpython

import os
import time
import board
import busio
import adafruit_lsm9ds1

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_lsm9ds1.LSM9DS1_I2C(i2c)

while True:
    os.system("clear")
    (x,y,z) = sensor.acceleration
    print(abs(x)+abs(y)+abs(z))
    print('Acceleration (m/s^2): ({0:0.3f},{1:0.3f},{2:0.3f})'
        .format(*sensor.acceleration))
    print('Magnetometer (gauss): ({0:0.3f},{1:0.3f},{2:0.3f})'
        .format(*sensor.magnetic))
    print('Gyroscope (degrees/sec): ({0:0.3f},{1:0.3f},{2:0.3f})'
        .format(*sensor.gyro))
    print('Temperature: {0:0.3f}C'.format(sensor.temperature))
    time.sleep(0.1)
