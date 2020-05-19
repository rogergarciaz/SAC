#! /usr/bin/env python3
### This file executes a code that stablish the value
### of the distance without using environment variables.
### Made by RAGZ
import time
import RPi.GPIO as GPIO
import vl53l0x as las
import hcsr04 as ult
## Class are initialized
laser = las.vl53l0x()
ultrasonic = ult.hcsr04()
## Parametrization sensor hcsr04
GPIO_TRIGGER = 23
GPIO_ECHO = 24
if __name__ == "__main__":
    try:
        while True:
            distLaser = laser.distancial()
            print("Range laser: {0}mm".format(distLaser))
            distUltra = ultrasonic.distanciau(GPIO_TRIGGER, GPIO_ECHO)
            print("Range Ultrasonic {0}mm".format(distUltra))
            time.sleep(1)
            print("##################################################")
    ## Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()