#! /usr/bin/env python3
### This file executes a code that gets
### the value of the dht11 sensor.
### Made by RAGZ
import sys
import Adafruit_DHT
class dht11 :
    def __init__(self):
        self.sensor = 11 #Or Adafruit_DHT.DHT11
        print("INA129 sensor initialization successfull")
    def environment(self, gpio):
        humidity1, temperature1 = Adafruit_DHT.read_retry(self.sensor, gpio) #humidity: float and temperature: float
        humidity = round(humidity1, 3)
        temperature = round(temperature1, 3)
        return humidity, temperature