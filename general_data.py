#! /usr/bin/env python3
### This file executes a code that stablish the value
### of the general data from the unit SAC.
### Made by RAGZ
import datetime
import psutil
import subprocess
from datetime import timedelta
class general_data :
     @staticmethod
     def loadcpu():
          cpuload1 = psutil.cpu_percent(interval=1, percpu=False) #cpuload: float
          cpuload = round(cpuload1, 3)
          return cpuload
     @staticmethod
     def ram():
          san = str(subprocess.check_output(['free','-m']))
          lines = san.split('n')
          free1 = lines[1].split()[3] #free: str
          free2 = float(free1)
          free = round(free2, 3)
          return free #int
     @staticmethod
     def cputemp():
          tempFile = open( '/sys/class/thermal/thermal_zone0/temp' )
          cpu_temp1 = tempFile.read() #cpu_temp: str 
          tempFile.close()
          cpu_temp2 = float(cpu_temp1)/1000
          cpu_temp = round(cpu_temp2, 3)
          return cpu_temp #Float
     @staticmethod
     def uptime():
          with open('/proc/uptime', 'r') as f:
               uptime_seconds = float(f.readline().split()[0])
               uptimeV = (timedelta(seconds = uptime_seconds)) #uptime: datetime.timedelta
               return uptimeV
     @staticmethod
     def cpufreq():
          tempfrq = open('/sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq', 'r')
          cpu_freq1 = tempfrq.read() #cpu_freq: str
          tempfrq.close()
          cpu_freq2 = float(cpu_freq1)/1000
          cpu_freq = round(cpu_freq2, 3)
          return cpu_freq #Float