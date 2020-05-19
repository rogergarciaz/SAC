#! /usr/bin/env python3
### This file executes a code that stablish the
### value of the general and specifi function of
### the unit SAC that works near the oven of CMSA.
### Made by RAGZ
import time
import dht11 as dht
import dates as dats
#import ina129 as ina
import general_data as dat
import alerts_data as ale
import sql_connection as sconn
import vl53l0x as las
import dht11hcsr04 as ult
import alerts_function as alef
class horno :
    def __init__(self):
        ## Class are initialized
        self.ambiente = dht.dht11()
        self.dates = dats.dates()
        self.datos = dat.general_data()
        self.aleg = ale.alerts_data()
        self.db = sconn.sql_connection()
        #self.consumo = ina.ina129()
        self.laser = las.vl53l0x()
        self.ultrasonic = ult.dht11hcsr04()
        self.alef = alef.alerts_function()
        ## Parametrization sensor DHT11
        self.gpioS = 4 #DHT11 GPIO DATA SAC
        self.gpioE = 17 #DHT11 GPIO DATA environment
        ## Parametrization sensor HCSR04
        self.GPIO_TRIGGER = 23
        self.GPIO_ECHO = 24
        ## Current date
        self.fechaV = self.dates.dateT()
        ## Interval of time to realize one cycle
        self.lapso = 200
        ## Previous value
        self.antL = 80
        self.antU = 80
    def accion_horno(self, sac):
        ### DHT11 SAC
        humidity, temperature = self.ambiente.environment(self.gpioS)
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
        power = 11.5 # Delete only if exists sensor
        #print("Power: {0} W".format(power))
        #voltage = self.consumo.voltage()
        voltage = 5 # Delete only if exists sensor
        #print("Voltage: {0} V".format(voltage))
        #current = self.consumo.current()
        current = 2.3 # Delete only if exists sensor
        #print("Current: {0} A".format(current))
        #shunt = self.consumo.shunt()
        shunt = 1.2 # Delete only if exists sensor
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
        ### Specific Function
        distL = []
        distU = []
        tempP = []
        humiP = []
        for i in range(1,101):
            lass = self.laser.distancial()
            distL.append(lass)
            #print("Range laser: {0}mm".format(lass))
            humi, temp = self.ambiente.environment(self.gpioE)
            #print("Temp: {0} C  Humidity: {1} %".format(temp, humi)) # "Temp: {0:0.1f} C  Humidity: {1:0.1f} %".format(temp, humi)
            tempP.append(temp)
            humiP.append(humi)
            ultt = self.ultrasonic.distanciau(self.GPIO_TRIGGER, self.GPIO_ECHO, temp, humi)
            distU.append(ultt)
            #print("Range Ultrasonic {0}mm".format(ultt))
            time.sleep(1)
        sumatoriaL = sum(distL)
        longitudL = float(len(distL))
        promedio1L = sumatoriaL/longitudL
        promedioL = round(promedio1L, 3)
        print("Average laser range: {0}mm".format(promedioL))
        sumatoriaU = sum(distU)
        longitudU = float(len(distU))
        promedio1U = sumatoriaU/longitudU
        promedioU = round(promedio1U, 3)
        print("Average ultrasonic range: {0}mm".format(promedioU))
        sumatoriaT = sum(tempP)
        longitudT = float(len(tempP))
        promedio1T = sumatoriaT/longitudT
        promedioT = round(promedio1T, 3)
        print("Average temperature: {0}C".format(promedioT))
        sumatoriaH = sum(humiP)
        longitudH = float(len(humiP))
        promedio1H = sumatoriaH/longitudH
        promedioH = round(promedio1H, 3)
        print("Average humidity: {0}%".format(promedioH))
        ### Alerts Function
        alertF = int(10) # Declaring function alert
        alertF = self.alef.laserd(promedioL,alertF, self.antL)
        alertF = self.alef.ultrad(promedioU, alertF, self.antU)
        self.antL = promedioL
        self.antU = promedioU
        ### SQL
        ## Insert Function Data
        self.db.insert_dataFECE(sac, promedioL, promedioU, alertF)
        time.sleep(1)