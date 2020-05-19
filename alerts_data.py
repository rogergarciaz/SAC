#! /usr/bin/env python3
### This file executes a code that stablish the
### value of the alert in the general data.
### Made by RAGZ
class alerts_data :
     def loadcpu(self, load, alertG):
          if (load >= 80):
               alertG = alertG + 1
          return alertG
     def ram(self, ram, alertG):
          if (ram <= 200):
               alertG = alertG + 10
          return alertG
     def cputemp(self, temp, alertG):
          if (temp >= 45):
               alertG = alertG + 4
          return alertG
     def cpufreq(self, freq, alertG):
          if (freq >= 1000):
               alertG = alertG + 2
          return alertG
     def tempe(self, tempe, alertG):
          if (tempe >= 45):
               alertG = alertG + 20
          return alertG
     def power(self, power, alertG):
          if (power <= 10.5 or power >= 15.5):
               alertG = alertG + 400
          return alertG
     def current(self, current, alertG):
          if (current >= 3.1 or current <= 2.1):
               alertG = alertG + 40
          return alertG
     def voltage(self, voltage, alertG):
          if (voltage != 5):
               alertG = alertG + 100
          return alertG
     def shunt(self, shunt, alertG):
          if (shunt >= 1.5 or shunt <= 0.7):
               alertG = alertG + 200
          return alertG
     def hume(self, humi, alertG):
          if (humi >= 80):
               alertG = alertG + 2000
          return alertG