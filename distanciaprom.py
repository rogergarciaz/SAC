#! /usr/bin/env python3
### This file executes a code that stablish the value
### of the average distance without using environment variables.
### Made by RAGZ
import time
import RPi.GPIO as GPIO
import promvl53l0x as las
import promhcsr04 as ult
## Class are initialized
laser = las.promvl53l0x()
ultrasonic = ult.promhcsr04()
## Parametrization sensor HCSR04
GPIO_TRIGGER = 23
GPIO_ECHO = 24
if __name__ == "__main__":
    try:
        while True:
            distLaser = laser.distancialprom()
            print("Range laser: {0}mm".format(distLaser))
            distUltra = ultrasonic.distanciauprom(GPIO_TRIGGER, GPIO_ECHO)
            print("Range Ultrasonic {0}mm".format(distUltra))
            time.sleep(1)
            print("##################################################")
    ## Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()