#! /usr/bin/env python3
### This file executes a code that stablish
### the value of the actual datetime, and
### the alert of the date accoding to an interval.
### Made by RAGZ
import datetime
class dates :
    @staticmethod
    def dateT ():
        datt = datetime.datetime.now()
        print (datt)
        return datt
    def dateAlert(self, fechaV, fechaN, lapso, alertG):
        if (fechaN - fechaV >= datetime.timedelta(seconds=lapso)):
            alertG = alertG + 1000
        return alertG