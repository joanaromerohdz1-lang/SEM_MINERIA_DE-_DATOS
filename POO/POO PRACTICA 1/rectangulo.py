#CLASE RECTANGULO
#Mis Parametros/Atributos son:ancho y alto
#Mis Metodos son:calcular Area y Perimetro, mostrar_valores
class rectangulo:
    def __init__(self,ancho,alto):
        self.ancho=float(ancho)
        self.alto=float(alto)
    
    def calArea(self):
        return self.ancho * self.alto
    
    def calPerimetro(self):
        return 2* (self.ancho+self.alto)
        
    def mostrar_valores(self) :
           print("Ancho:", self.ancho)
           print("Alto:", self.alto)
           print("Area:", self.calArea())
           print("Perimetro:", self.calPerimetro())