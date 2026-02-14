#CLASE CUENTA BANCARIA
#Mis Parametros/Atributos son:titular y saldo=0
#Mis Metodos son:depositar,retirar y mostrar saldo

class cuentaBan:
    def __init__(self,titular):
        self.titular=titular
        self.saldo=0.0
#Declaracion de Metodos
    def depositar(self,cantidad):
        self.saldo +=cantidad

    def retirar(self,cantidad):
        if cantidad <= self.saldo:
            self.saldo -=cantidad
        else:
            print("No tienes fondos suficientes,verifica tu saldo")
        
    def mostrar_saldo(self):
            print("Titular:",self.titular)
            print("Saldo:",self.saldo)


        