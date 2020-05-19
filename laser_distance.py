#! /usr/bin/env python3
### This file executes a code that stablish the value
### of the distance without using environment variables.
### Made by RAGZ
import time
import board
import busio
import adafruit_vl53l0x
import RPi.GPIO
## Initialize I2C bus and sensor.
i2c = busio.I2C(board.SCL, board.SDA)
vl53 = adafruit_vl53l0x.VL53L0X(i2c)
def distancial():
    distance = vl53.range
    return distance
if __name__ == "__main__":
    try:
        while True:
            distLaser = distancial()
            print("Range laser: {0}mm".format(distLaser))
            time.sleep(1)
            print("###################################")
    ## Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        RPi.GPIO.cleanup()