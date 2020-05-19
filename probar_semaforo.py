#! /usr/bin/env python3
### This file executes a code that executes a probe
### without connection in the traffic lights, with
### that state is activate a siren and ten seconds
### later activate a light and a tanker.
### Made by RAGZ
import time
import RPi.GPIO as GPIO
class probar_semaforo :
    def __init__(self):
        # GPIO Mode (BOARD / BCM)
        GPIO.setmode(GPIO.BCM)
        # state of traffic lights
        self.estado = 0
        print("Semaforo initializaton successfull")
        # Set GPIO Pins
        self.GPIO_SIREN = 17
        self.GPIO_LIGHT = 27
        self.GPIO_TANKER = 22
        # Set GPIO direction (IN / OUT)
        GPIO.setup(self.GPIO_SIREN, GPIO.OUT)
        GPIO.setup(self.GPIO_LIGHT, GPIO.OUT)
        GPIO.setup(self.GPIO_TANKER, GPIO.OUT)
        GPIO.output(self.GPIO_SIREN, False)
        GPIO.output(self.GPIO_LIGHT, False)
        GPIO.output(self.GPIO_TANKER, False)
    def accion_probar(self):
        # State inactive
        if self.estado == 0:
            GPIO.output(self.GPIO_SIREN, False)
            GPIO.output(self.GPIO_LIGHT, False)
            GPIO.output(self.GPIO_TANKER, False)
            print("Semaforo inactive")
            while self.estado == 0:
                time.sleep(60)
                self.estado = 1
                print("Semaforo inactive to active")
        # State active
        if self.estado == 1:
            GPIO.output(self.GPIO_SIREN, True)
            time.sleep(10)
            GPIO.output(self.GPIO_LIGHT, True)
            GPIO.output(self.GPIO_TANKER, True)
            print("Semaforo active")
            while self.estado == 1:
                time.sleep(60)
                self.estado = 0
                print("Semaforo active to inactive")