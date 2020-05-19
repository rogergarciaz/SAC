#! /usr/bin/env python3
### This file executes a code that stablish the value
### of the average distance using the vl53l0x sensor.
### Made by RAGZ
import time
import board
import busio
import adafruit_vl53l0x
class promvl53l0x :
    def __init__(self):
        print("Initializing VL53L0X sensor")
        i2c = busio.I2C(board.SCL, board.SDA)
        self.vl53 = adafruit_vl53l0x.VL53L0X(i2c)
        print("VL53L0X sensor initialization successfull")
    def distancialprom(self):
        dis = []
        for i in range(1,101):
            dis.append(self.vl53.range)
            time.sleep(1)
        sumatoria = sum(dis)
        longitud = float(len(dis))
        promedio1 = sumatoria/longitud
        promedio = round(promedio1, 3)
        return promedio