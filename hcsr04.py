#! /usr/bin/env python3
### This file executes a code that stablish the value
### of a unic distance without using environment variables.
### Made by RAGZ
import RPi.GPIO as GPIO
import time
class hcsr04:
    def __init__(self):
        print("Initializing HCSR04 sensor")
        GPIO.setmode(GPIO.BCM)
        print("HCSR04 sensor initialization successfull")
    def distanciau(self, GPIO_TRIGGER, GPIO_ECHO):
        TRIGGER = GPIO_TRIGGER
        ECHO = GPIO_ECHO
        GPIO.setup(TRIGGER, GPIO.OUT)
        GPIO.setup(ECHO, GPIO.IN)
        GPIO.output(TRIGGER, True)
        time.sleep(0.00001)
        GPIO.output(TRIGGER, False)
        StartTime = time.time()
        StopTime = time.time()
        while GPIO.input(ECHO) == 0:
            StartTime = time.time()
        while GPIO.input(ECHO) == 1:
            StopTime = time.time()
        TimeElapsed = StopTime - StartTime
        distance1 = (TimeElapsed * 343000) / 2 #distance: float
        distance = round(distance1, 3)
        return distance