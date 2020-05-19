#! /usr/bin/env python3
### This file executes a code that responds to a variable provided by a database,
### with that state is activate a siren and ten seconds later activate a
### light and a tanker.
### Made by RAGZ
import time
import RPi.GPIO as GPIO
import sql_connection as sconn
class semaforo :
    def __init__(self):
        print("Initializing Semaforo sensor")
        # GPIO Mode (BOARD / BCM)
        GPIO.setmode(GPIO.BCM)
        self.estado = 0
        self.cambio = 1
        # Initialize class
        self.db = sconn.sql_connection()
        print("Semaforo initializaton successfull")
    def inicio_semaforo(self, GPIO_SIREN, GPIO_LIGHT, GPIO_TANKER):
        # Set GPIO Pins
        self.GPIO_SIREN = GPIO_SIREN #17
        self.GPIO_LIGHT = GPIO_LIGHT #27
        self.GPIO_TANKER = GPIO_TANKER #22
        # Set GPIO direction (IN / OUT)
        GPIO.setup(self.GPIO_SIREN, GPIO.OUT)
        GPIO.setup(self.GPIO_LIGHT, GPIO.OUT)
        GPIO.setup(self.GPIO_TANKER, GPIO.OUT)
        GPIO.output(self.GPIO_SIREN, False)
        GPIO.output(self.GPIO_LIGHT, False)
        GPIO.output(self.GPIO_TANKER, False)
    def estado_semaforo(self):
        self.estado, self.cambio = self.db.get_data()
        # State inactive
        if self.estado == 0:
            GPIO.output(self.GPIO_SIREN, False)
            GPIO.output(self.GPIO_LIGHT, False)
            GPIO.output(self.GPIO_TANKER, False)
            time.sleep(1)
            self.db.update_estadoBO(self.cambio)#Toca cambiar dependiendo del semaforo
            self.estado, self.cambio = self.db.get_data()
        # State active
        if self.estado == 1:
            GPIO.output(self.GPIO_SIREN, True)
            time.sleep(10)
            GPIO.output(self.GPIO_LIGHT, True)
            GPIO.output(self.GPIO_TANKER, True)
            time.sleep(1)
            self.db.update_estadoBO(self.cambio)