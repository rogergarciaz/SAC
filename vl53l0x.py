#! /usr/bin/env python3
### This file executes a code that stablish the
### value of the distance using the vl53l0x sensor.
### Made by RAGZ
import time
import board
import busio
import adafruit_vl53l0x
class vl53l0x :
    def __init__(self):
        print("Initializing VL53L0X sensor")
        ## Initialize I2C bus and sensor.
        i2c = busio.I2C(board.SCL, board.SDA) #i2c: busio.I2C object at 0x7668fb90 --- class busio.I2C
        self.vl53 = adafruit_vl53l0x.VL53L0X(i2c) #vl53: adafruit_vl53l0x.VL53L0X object at 0x76546f90 --- class adafruit_vl53l0x.VL53L0X
        self.vl53.measurement_timing_budget = 200000
        print("VL53L0X sensor initializaton successfull")
    def distancial(self):
        distance1 = float(self.vl53.range) #vl53.range: int
        distance = round(distance1, 3)
        return distance
# Optionally adjust the measurement timing budget to change speed and accuracy.
# See the example here for more details:
#   https://github.com/pololu/vl53l0x-arduino/blob/master/examples/Single/Single.ino
# For example a higher speed but less accurate timing budget of 20ms:
#vl53.measurement_timing_budget = 20000
# Or a slower but more accurate timing budget of 200ms:
#vl53.measurement_timing_budget = 200000
# The default timing budget is 33ms, a good compromise of speed and accuracy.