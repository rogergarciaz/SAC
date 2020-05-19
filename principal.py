#! /usr/bin/env python3
### This file executes a code that controls
### the action to be taken for the unity SAC.
### Made by RAGZ
import time
import sys
import importlib
import RPi.GPIO as GPIO
import sql_connection as conn
import ficheros as fic
import code
ficheros = fic.ficheros()
db = conn.sql_connection()
#sac = int(ficheros.leer("sacNumero.txt"))
#estado = int(ficheros.leer("estadoActual.txt"))
estado = 0
time.sleep(60)
def main():
    try:
        while True:
            global estado
            global sac
            ## Initial State
            if estado ==0:
                sac = db.get_estadoI()
                db.update_estado(sac, 1)
                time.sleep(60)
                #ficheros.sobrescribir("sacNumero.txt",str(sac))
                #ficheros.sobrescribir("estadoActual.txt",str(estado))
                estado = db.get_estadoA(sac)
            ## Reading Relation of the unit with the codes
            if estado ==1:
                relacion = db.get_relationcodes(sac)
                db.update_estado(sac, 2)
                time.sleep(60)
                #ficheros.sobrescribir("sacNumero.txt",str(sac))
                #ficheros.sobrescribir("estadoActual.txt",str(estado))
                estado = db.get_estadoA(sac)
            ## Saving codes of the unit with the codes
            if estado == 2:
                for rela in relacion:
                    name, codes = db.get_codes(rela)
                    ficheros.sobrescribir(name, codes)
                db.update_estado(sac, 3)
                time.sleep(60)
                #ficheros.sobrescribir("sacNumero.txt",str(sac))
                #ficheros.sobrescribir("estadoActual.txt",str(estado))
                estado = db.get_estadoA(sac)
                importlib.reload(code)
                #importlib.reload(sql_connection)#solo si se altera
                time.sleep(60)
            ## Executing the specific function
            if estado == 3:
                code.code().doit(sac)
                time.sleep(1)
                #ficheros.sobrescribir("sacNumero.txt",str(sac))
                #ficheros.sobrescribir("estadoActual.txt",str(estado))
                estado = db.get_estadoA(sac)
            ## Reconfiguring the unit
            if estado == 4:
                estado = 0
                sac = 0
                #ficheros.sobrescribir("sacNumero.txt",str(sac))
                #ficheros.sobrescribir("estadoActual.txt",str(estado))
                db.update_estado(sac, 5) #Ending the unit activity
                ## Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
    except:
        print("Error Inesperado: ", sys.exc_info()[0])
        time.sleep(15)
while True: 
    main()