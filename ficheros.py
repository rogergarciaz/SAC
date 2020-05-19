class ficheros :
    def leer(self, nombre):
        camino = "/home/pi/Documents/reto/"
        #ruta = camino + "test.txt"
        ruta = camino + nombre
        handler = open(ruta, "r")
        contenido = handler.read()
        valor1 = contenido.split(", ", 1)
        valor = valor1[0]
        handler.seek(0)
        handler.close
        return valor
    def escribir(self, nombre, valor):
        camino = "/home/pi/Documents/reto/"
        ruta = camino + nombre
        handler = open(ruta, "a")
        handler.write(valor)
        handler.close
    def sobrescribir(self, nombre, valor):
        camino = "/home/pi/Documents/reto/"
        ruta = camino + nombre
        handler = open(ruta, "w")
        handler.write(valor)
        handler.close