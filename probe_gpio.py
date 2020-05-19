#! /usr/bin/env python3
### This file executes a code for probe the
### correct operation of a GPIO pin from the
### unit SAC that works near the oven of CMSA.
### Made by RAGZ
import time
import RPi.GPIO as GPIO
class probe_gpio :
    def __init__(self):
        ## GPIO Mode (BOARD / BCM)
        GPIO.setmode(GPIO.BCM)
        ## State of the pin
        self.estado = 1
    def accion_probe(self, pinN):
        ## Number of the GPIO
        self.pinGPIO = pinN
        ## set GPIO direction (IN / OUT)
        GPIO.setup(self.pinGPIO, GPIO.OUT)
        ### Test GPIO Active
        if self.estado == 1:
            GPIO.output(self.pinGPIO, True)
            time.sleep(5)
            self.estado = 0
        ### Test GPIO Inactive
        if self.estado == 0:
            GPIO.output(self.pinGPIO, False)
            time.sleep(5)
            self.estado = 1