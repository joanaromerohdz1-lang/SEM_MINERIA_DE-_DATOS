#Importo la clase, creo un objeto a partir de ella, modifico sus atributos usando métodos y finalmente muestro su estado actual.

#CLASE COCHE

from coche import Coche

mi_coche=Coche("Toyota","Corolla","Rojo")
mi_coche.acelerar(100)
mi_coche.frenar(20)
mi_coche.mostrar_info()

#CLASE CUENTA BANCARIA

from cuentaBan import cuentaBan

mi_cuentaBan=cuentaBan("Joana Romero")
mi_cuentaBan.depositar(2500)
mi_cuentaBan.retirar(500)
mi_cuentaBan.mostrar_saldo()

#CLASE RECTANGULO

from rectangulo import rectangulo

mi_rectangulo=rectangulo("8.5","2.3")
mi_rectangulo.mostrar_valores()
