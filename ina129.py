#! /usr/bin/env python3
### This file executes a code that stablish the value
### of the energy consumption of the unit SAC.
### Made by RAGZ
from ina219 import INA219
from ina219 import DeviceRangeError
class ina129 :
    def __init__(self):
        print("Initializing INA129 sensor")
        SHUNT_OHMS = 0.1
        self.ina = INA219(SHUNT_OHMS)
        self.ina.configure()
        print("INA129 sensor initializaton successfull")
    def power(self):
        try:
            pow = "Power: %.3f mW" % self.ina.power()
            print(self.ina.power())
            print(type(self.ina.power()))
            #pow2 = self.ina.power()
            #pow3 = float(pow2)
            #pow = round(pow3, 3)
            return pow
        except DeviceRangeError as e:
            ## Current out of device range with specified shunt resister
            print(e)
    def current(self):
        try:
            curr = "Bus Current: %.3f mA" % self.ina.current()
            print(type(self.ina.current()))
            #curr1 = self.ina.current()
            #curr2 = float(curr1)
            #curr = round(curr2, 3)
            return curr
        except DeviceRangeError as e:
            print(e)
    def voltage(self):
        try:
            volt = "Bus Voltage: %.3f V" % self.ina.voltage()
            print(type(self.ina.voltage()))
            #volt1 = self.ina.voltage()
            #volt2 = float(volt1)
            #volt = round(volt2, 3)
            return volt
        except DeviceRangeError as e:
            print(e)
    def shunt(self):
        try:
            shu = "Shunt voltage: %.3f mV" % self.ina.shunt_voltage()
            print(type(self.ina.shunt_voltage()))
            #shu2 = self.ina.shunt_voltage()
            #shu3 = float(shu2)
            #shu = round(shu3, 3)
            return shu
        except DeviceRangeError as e:
            print(e)