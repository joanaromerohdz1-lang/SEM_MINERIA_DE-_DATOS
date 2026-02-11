#EJERCICIO 1-NUMERO PAR O IMPAR

numero = int(input("Ingresa un número: "))
if numero % 2 == 0:
    print("Par")
else:
    print("Impar")

#EJERCICIO 2-NUMERO POSITIVO O NEGATIVO

numero=int(input("Ingresa un Numero: "))
if numero >=0:
    print("El numero es POSITIVO")
else:
    print("El numero es NEGATIVO")

#EJERCICIO 3-MAYOR O MENOR DE EDAD

edad=int(input("Ingresa tu EDAD por favor: "))
if edad >=18:
    print("Mayor de Edad")
else:
    print("Menor de Edad")

#EJERCICIO 4-APROBACION DE MATERIAS

calificacion=float(input("Ingresa la calificacion: "))
if calificacion >=60:
    print("Aprobado")
else:
    print("Reprobado")

#JERCICIO 5-CLASIFICAR MATERIAS A,B,C,D,F

calif=float(input("Ingresa la Calificacion Numerica: "))
if calificacion >=90:
    print("A")
elif calificacion >=80:
    print("B")
elif calificacion >=70:
    print("C")
elif calificacion >=60:
    print("D")
else:
    print("F")

#EJERCICIO 6-ESTADO DEL AGUA

temperatura = float(input("Ingresa la temperatura en °C: "))

if temperatura < 0:
    print("Sólido")
elif temperatura <= 100:
    print("Líquido")
else:
    print("Vapor")
