#! /usr/bin/env python3
### This file executes a code that stablish the
### value of the alert in the function data.
### Made by RAGZ
class alerts_function :
     def laserd(self, las, alert, antL):
          resta = las - antL
          if (abs(resta) >= 5):
               alert = alert + 1
          return alert
     def ultrad(self, ult, alert, antU):
          resta = ult - antU
          if (abs(resta) >= 5):
               alert = alert + 2
          return alert