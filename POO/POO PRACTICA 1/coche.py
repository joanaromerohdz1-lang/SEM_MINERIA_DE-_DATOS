#CLASE COCHE
#Mis Parametros/Atributos seran:marca,modelo,color y velocidad
#Mis Metodos seran:acelerar,frenar y mostrar
#RECORDAR=__init__ es el constructor (se ejecuta cuando creo el objeto)
# Y self representa el objeto actual.

class Coche:
    def __init__(self,marca,modelo,color):
        self.marca=marca
        self.modelo=modelo
        self.color=color
        self.velocidad=0
#Método para aumentar la velocidad(Sumamos a la velocidad actual)
    def acelerar(self,cantidad):
        self.velocidad += cantidad 

#Método para disminuir la velocidad( Restamos velocidad)
    def frenar(self,cantidad):
        self.velocidad -= cantidad 
    #Debemos evitar que la velocidad sea negativa
        if self.velocidad < 0:
            self.velocidad = 0

    def mostrar_info(self):
        print("Marca",self.marca)
        print("Modelo:",self.modelo)
        print("Color:",self.color)
        print("Velocidad Actual:",self.velocidad)