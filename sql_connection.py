#! /usr/bin/env python3
### This file executes a code that connects to a database,
### for executing different sentences.
### Made by RAGZ
import pyodbc
class sql_connection :
    @staticmethod
    def get_data():
        db = pyodbc.connect("DRIVER=FreeTDS;SERVER=192.168.X.XX;PORT=1433;DATABASE=XXX;UID=XXXXXX;PWD=XXXXXXXXXXXX;TDS_Version=4.2;")
        cursor = db.cursor()
        sql_text = "SELECT TOP 1 ID_estado, ID_Cambio FROM SAC.dbo.SAC_Semaforo ORDER BY ID_Cambio DESC"
        cursor.execute(sql_text)
        for row in cursor:
            estado = row[0] #ID_estado
            cambio = row[1] #ID_Cambio
        cursor.close()
        db.close()
        print("Data from Semaforo consulted without complications")
        print("The state is:")
        print(estado)
        return (estado, cambio)
    def update_estadoPR(self, cambio):
        db = pyodbc.connect("DRIVER=FreeTDS;SERVER=192.168.X.XX;PORT=1433;DATABASE=XXX;UID=XXXXXX;PWD=XXXXXXXXXXXX;TDS_Version=4.2;")
        cursor = db.cursor()
        sql_text = "UPDATE SAC.dbo.SAC_Semaforo SET int_estadoPR = 1 WHERE ID_Cambio = ?"
        cursor.execute(sql_text, cambio)
        cursor.commit()
        cursor.close()
        db.close()
        print("State Semaforo update without complications")
    def update_estadoBO(self, cambio):
        db = pyodbc.connect("DRIVER=FreeTDS;SERVER=192.168.X.XX;PORT=1433;DATABASE=XXX;UID=XXXXXX;PWD=XXXXXXXXXXXX;TDS_Version=4.2;")
        cursor = db.cursor()
        sql_text = "UPDATE SAC.dbo.SAC_Semaforo SET int_estadoBO = 1 WHERE ID_Cambio = ?"
        cursor.execute(sql_text, cambio)
        cursor.commit()
        cursor.close()
        db.close()
        print("State Semaforo update without complications")
    def update_estadoBA(self, cambio):
        db = pyodbc.connect("DRIVER=FreeTDS;SERVER=192.168.X.XX;PORT=1433;DATABASE=XXX;UID=XXXXXX;PWD=XXXXXXXXXXXX;TDS_Version=4.2;")
        cursor = db.cursor()
        sql_text = "UPDATE SAC.dbo.SAC_Semaforo SET int_estadoBA = 1 WHERE ID_Cambio = ?"
        cursor.execute(sql_text, cambio)
        cursor.commit()
        cursor.close()
        db.close()
        print("State Semaforo update without complications")
    def update_estadoLab(self, cambio):
        db = pyodbc.connect("DRIVER=FreeTDS;SERVER=192.168.X.XX;PORT=1433;DATABASE=XXX;UID=XXXXXX;PWD=XXXXXXXXXXXX;TDS_Version=4.2;")
        cursor = db.cursor()
        sql_text = "UPDATE SAC.dbo.SAC_Semaforo SET int_estadoLab = 1 WHERE ID_Cambio = ?"
        cursor.execute(sql_text, cambio)
        cursor.commit()
        cursor.close()
        db.close()
        print("State Semaforo update without complications")
    def update_estadoDRKF(self, cambio):
        db = pyodbc.connect("DRIVER=FreeTDS;SERVER=192.168.X.XX;PORT=1433;DATABASE=XXX;UID=XXXXXX;PWD=XXXXXXXXXXXX;TDS_Version=4.2;")
        cursor = db.cursor()
        sql_text = "UPDATE SAC.dbo.SAC_Semaforo SET int_estadoDRKF = 1 WHERE ID_Cambio = ?"
        cursor.execute(sql_text, cambio)
        cursor.commit()
        cursor.close()
        db.close()
        print("State Semaforo update without complications")
    @staticmethod
    def get_estadoI():
        db = pyodbc.connect("DRIVER=FreeTDS;SERVER=192.168.X.XX;PORT=1433;DATABASE=XXX;UID=XXXXXX;PWD=XXXXXXXXXXXX;TDS_Version=4.2;")
        cursor = db.cursor()
        sql_text = "SELECT ID_Rasp, txt_ETH0 FROM SAC.dbo.SAC_Raspberry WHERE int_estado = 0"
        cursor.execute(sql_text)
        for row in cursor:
            sac = row[0] #ID_rasp
        cursor.close()
        db.close()
        print("Initial data consulted without complications")
        print(sac)
        print(type(sac))
        return (sac)
    def get_estadoA(self, sac):
        db = pyodbc.connect("DRIVER=FreeTDS;SERVER=192.168.X.XX;PORT=1433;DATABASE=XXX;UID=XXXXXX;PWD=XXXXXXXXXXXX;TDS_Version=4.2;")
        cursor = db.cursor()
        sql_text = "SELECT int_estado, txt_ETH0 FROM SAC.dbo.SAC_Raspberry WHERE ID_Rasp = ?"
        cursor.execute(sql_text, sac)
        for row in cursor:
            estado = row[0] #int_estado
        cursor.close()
        db.close()
        print("State consulted without complications")
        return (estado)
    def get_relationcodes(self, sac):
        db = pyodbc.connect("DRIVER=FreeTDS;SERVER=192.168.X.XX;PORT=1433;DATABASE=XXX;UID=XXXXXX;PWD=XXXXXXXXXXXX;TDS_Version=4.2;")
        cursor = db.cursor()
        sql_text = "SELECT ID_Tipo_modulo, ID_relacionRasp_Modulo FROM SAC.dbo.SAC_Rasp_Modulo WHERE ID_Rasp = ?"
        cursor.execute(sql_text, sac)
        relacion =[]
        for row in cursor:
            relacion.append(row[0]) #ID_Tipo_modulo
        cursor.close()
        db.close()
        print("Relation codes consulted without complications")
        return (relacion)
    def get_codes(self, relacion):
        db = pyodbc.connect("DRIVER=FreeTDS;SERVER=192.168.X.XX;PORT=1433;DATABASE=XXX;UID=XXXXXX;PWD=XXXXXXXXXXXX;TDS_Version=4.2;")
        cursor = db.cursor()
        sql_text = "SELECT txt_nombreModulo, txt_codigoModulo FROM SAC.dbo.SAC_Modulos_programacion WHERE ID_Tipo_modulo = ?"
        cursor.execute(sql_text, relacion)
        for row in cursor:
            name = row[0] #txt_nombreModulo
            code = row[1] #txt_codigoModulo
        cursor.close()
        db.close()
        print("Codes consulted without complications")
        return (name, code)
    def update_estado(self, sac, estado):
        db = pyodbc.connect("DRIVER=FreeTDS;SERVER=192.168.X.XX;PORT=1433;DATABASE=XXX;UID=XXXXXX;PWD=XXXXXXXXXXXX;TDS_Version=4.2;")
        cursor = db.cursor()
        sql_text = "UPDATE SAC.dbo.SAC_Raspberry SET int_estado = ? WHERE ID_Rasp = ?"
        cursor.execute(sql_text, (estado, sac))
        cursor.commit()
        cursor.close()
        db.close()
        print("State update without complications")
    def insert_dataG(self, loadcpu, ram, cputemp, uptime, cpufreq, humidity, temperature, voltage, current, shunt, sac, power, datt, alertG):
        db = pyodbc.connect("DRIVER=FreeTDS;SERVER=192.168.X.XX;PORT=1433;DATABASE=XXX;UID=XXXXXX;PWD=XXXXXXXXXXXX;TDS_Version=4.2;")
        cursor = db.cursor()
        sql_text = """
                    INSERT INTO SAC.dbo.SAC_GeneralData (float_cpuLoad, float_ramFree, float_cpuTemp, txt_upTime, float_cpuFreq, float_humidity, float_temperature, float_voltage, float_current, float_shunt, ID_Rasp, float_power, dtm_date, int_alerta) 
                    VALUES
                    (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                   """
        cursor.execute(sql_text, (loadcpu, ram, cputemp, uptime, cpufreq, humidity, temperature, voltage, current, shunt, sac, power, datt, alertG))
        cursor.commit()
        cursor.close()
        db.close()
        print("General data inserted without complications")
    def insert_dataF(self, sac, datt, promedioL, promedioU, alertF):
        db = pyodbc.connect("DRIVER=FreeTDS;SERVER=192.168.X.XX;PORT=1433;DATABASE=XXX;UID=XXXXXX;PWD=XXXXXXXXXXXX;TDS_Version=4.2;")
        cursor = db.cursor()
        sql_text = """
                    INSERT INTO SAC.dbo.SAC_ControlEstructural (ID_Rasp, dtm_date, float_laser, float_ultrasonic, int_alerta) 
                    VALUES
                    (?, ?, ?, ?, ?)
                   """
        cursor.execute(sql_text, (sac, datt, promedioL, promedioU, alertF))
        cursor.commit()
        cursor.close()
        db.close()
        print("Function data inserted without complications")
    def insert_dataGE(self, loadcpu, ram, cputemp, uptime, cpufreq, humidity, temperature, voltage, current, shunt, sac, power, alertG):
        db = pyodbc.connect("DRIVER=FreeTDS;SERVER=192.168.X.XX;PORT=1433;DATABASE=XXX;UID=XXXXXX;PWD=XXXXXXXXXXXX;TDS_Version=4.2;")
        #db = pyodbc.connect("DRIVER=FreeTDS;SERVER=192.168.X.XX;PORT=1433;DATABASE=XXX;UID=XXXXXX;PWD=XXXXXXXXXXXX;TDS_Version=4.2;")
        cursor = db.cursor()
        sql_text = "EXEC SPS_SAC_INSERT_DATAG @float_cpuLoad=?, @float_ramFree=?, @float_cpuTemp=?, @txt_upTime=?, @float_cpuFreq=?, @float_humidity=?, @float_temperature=?, @float_voltage=?, @float_current=?, @float_shunt=?, @ID_Rasp=?, @float_power=?, @int_alerta=?;"
        cursor.execute(sql_text, (loadcpu, ram, cputemp, uptime, cpufreq, humidity, temperature, voltage, current, shunt, sac, power, alertG))
        cursor.commit()
        cursor.close()
        db.close()
        print("General data inserted without complications")
    def insert_dataFECE(self, sac, promedioL, promedioU, alertF):
        db = pyodbc.connect("DRIVER=FreeTDS;SERVER=192.168.X.XX;PORT=1433;DATABASE=XXX;UID=XXXXXX;PWD=XXXXXXXXXXXX;TDS_Version=4.2;")
        #db = pyodbc.connect("DRIVER=FreeTDS;SERVER=192.168.X.XX;PORT=1433;DATABASE=XXX;UID=XXXXXX;PWD=XXXXXXXXXXXX;TDS_Version=4.2;")
        cursor = db.cursor()
        sql_text = "EXEC SPS_SAC_INSERT_DATAGECE @ID_Rasp=?, @float_laser=?, @float_ultrasonic=?, @int_alerta=?;"
        cursor.execute(sql_text, (sac, promedioL, promedioU, alertF))
        cursor.commit()
        cursor.close()
        db.close()
        print("Function data inserted without complications")