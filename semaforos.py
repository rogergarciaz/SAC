#! /usr/bin/env python3
### This file executes a code used for the control
### of light traffics of slag pot.
### Made by RAGZ
import time
#import dht11 as dht
import dates as dats
#import ina129 as ina
import general_data as dat
import alerts_data as ale
import sql_connection as sconn
import semaforo as sema
class semaforos :
    def __init__(self):
        ## Parametrization GPIO
        self.GPIO_SIREN = 17
        self.GPIO_LIGHT = 27
        self.GPIO_TANKER = 22
        ## Iitialization of classes
        #self.ambiente = dht.dht11()
        self.dates = dats.dates()
        #self.consumo = ina.ina129()
        self.datos = dat.general_data()
        self.aleg = ale.alerts_data()
        self.db = sconn.sql_connection()
        self.semaf = sema.semaforo()
        ## Parametrization sensor DHT11
        #self.gpioS = 4 #DHT11 GPIO DATA SAC
        ## Current date
        self.fechaV = self.dates.dateT()
        ## Interval of time to realize one cycle
        self.lapso = 5
        ## Parametrization Semaforo
        self.semaf.inicio_semaforo(self.GPIO_SIREN, self.GPIO_LIGHT, self.GPIO_TANKER)
    def accion_semaforo(self, sac):
        ### DHT11 SAC
        #humidity, temperature = self.ambiente.environment(self.gpioS)
        humidity = 0 #Comment if the sensor exists
        temperature = 0 #Comment if the sensor exists
        print("Temp: {0}C  Humidity: {1}%".format(temperature, humidity))
        ### SBC SAC
        cpufreq = self.datos.cpufreq()
        print("CPU Freq: {0} Hz".format(cpufreq))
        loadcpu = self.datos.loadcpu()
        print("CPU Load: {0}%".format(loadcpu))
        cputemp = self.datos.cputemp()
        print("CPU Temp: {0}C".format(cputemp))
        ram = self.datos.ram()
        print("RAM Free: {0}Mbytes".format(ram))
        uptime = str(self.datos.uptime())
        print("Uptime: {0}".format(uptime))
        ### INA129 SAC
        #power = self.consumo.power()
        power = 11.5 # Comment only if exists sensor
        #print("Power: {0} W".format(power))
        #voltage = self.consumo.voltage()
        voltage = 5 # Comment only if exists sensor
        #print("Voltage: {0} V".format(voltage))
        #current = self.consumo.current()
        current = 2.3 # Comment only if exists sensor
        #print("Current: {0} A".format(current))
        #shunt = self.consumo.shunt()
        shunt = 1.2 # Comment only if exists sensor
        #print("Voltage Shunt: {0} V".format(shunt))
        ### Date
        datt = self.dates.dateT() # Current date
        fechaN = datt
        #print(datt)
        ### Alerts General
        alertG = int(10) # Declaring general alertG
        alertG = self.aleg.cpufreq(cpufreq, alertG)
        alertG = self.aleg.cputemp(cputemp, alertG)
        alertG = self.aleg.loadcpu(loadcpu, alertG)
        alertG = self.aleg.ram(ram, alertG)
        alertG = self.aleg.tempe(temperature, alertG)
        alertG = self.aleg.hume(humidity, alertG)
        alertG = self.aleg.power(power, alertG)
        alertG = self.aleg.current(current, alertG)
        alertG = self.aleg.voltage(voltage, alertG)
        alertG = self.aleg.shunt(shunt, alertG)
        alertG = self.dates.dateAlert(self.fechaV, fechaN, self.lapso, alertG)
        self.fechaV = fechaN
        ### SQL
        ## Insert General Data
        self.db.insert_dataGE(loadcpu, ram, cputemp, uptime, cpufreq, humidity, temperature, voltage, current, shunt, sac, power, alertG)
        ## Specific Function
        self.semaf.estado_semaforo()
        time.sleep(1)