#! /usr/bin/env python3
### This file executes a code that stablish the value
### of the distance using environment variables.
### Made by RAGZ
import RPi.GPIO as GPIO
import time
class dht11hcsr04:
    def __init__(self):
        print("Initializing HCSR04 sensor")
        GPIO.setmode(GPIO.BCM)
        print("HCSR04 sensor initializaton successfull")
    def distanciau(self, GPIO_TRIGGER, GPIO_ECHO, temp, humi):
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
        #vel1 = 331.4 + (0.606 * temp) + (0.0124 * humi) # Speed of Sound in M/s
        #vel2 = 331400 + (606 * temp) + (12.4 * humi) # Speed of Sound in mm/s
        vel = 328360 + (610 * temp) # Velocidad del Sonido
        distance1 = (TimeElapsed * vel) / 2
        distance = round(distance1, 3)
        return distance