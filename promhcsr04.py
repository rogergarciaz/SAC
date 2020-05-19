#! /usr/bin/env python3
### This file executes a code that stablish the value
### of the average distance without environment variables.
### Made by RAGZ
import RPi.GPIO as GPIO
import time
class promhcsr04:
    def __init__(self):
        print("Initializing HCSR04 sensor")
        GPIO.setmode(GPIO.BCM)
        print("HCSR04 sensor initialization successfull")
    def distanciauprom(self, GPIO_TRIGGER, GPIO_ECHO):
        dis = []
        for i in range(1,101):
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
            distance1 = (TimeElapsed * 343000) / 2
            dis.append(distance1)
            time.sleep(1)
        sumatoria = sum(dis)
        longitud = float(len(dis))
        promedio1 = sumatoria/longitud
        promedio = round(promedio1, 3)
        print("Distance Sensor")
        print(promedio)
        return promedio