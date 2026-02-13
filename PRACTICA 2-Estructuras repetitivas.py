#-----------------------------Estructuras repetitivas-----------------

#Ejercicio 1: Suma de los primeros N números
Numero=int(input("Ingresa el valor de Numero: "))
suma=0
for i in range(1,Numero+1):
    suma+=i
    print("La suma total es: ",suma)

#Ejercicio 2: Factorial de un número
numeroo=int(input("Ingresa un numero entero positivo:" ))
factorial=1
for i in range(1,numeroo+1):
    factorial *=i
    print("El factorial es: ",factorial)

#Ejercicio 3: Tabla de multiplicar
num=int(input("Ingresa el numero para la tabla: "))

for i in range(1,11):
    resultado=num*i
    print(num,"X",i,"=",resultado)

#Ejercicio 4: Cálculo de promedio de notas
suma = 0
contador = 0

nota = float(input("Ingresa una nota (negativa para terminar): "))
for i in range(100):
    if nota < 0:
        break
    suma += nota
    contador += 1
    nota = float(input("Ingresa otra nota (negativa para terminar): "))

if contador > 0:
    promedio = suma / contador
    print("El promedio es:", promedio)
else:
    print("No se ingresaron notas válidas.")

#Ejercicio 5: Potencia de un número
base = int(input("Ingresa la base: "))
exponente = int(input("Ingresa el exponente: "))
resultado = 1
for i in range(exponente):
    resultado *= base
print("La potencia es:", resultado)

#Ejercicio 6: Suma de números pares en un rango
A = int(input("Ingresa el valor de A: "))
B = int(input("Ingresa el valor de B: "))
suma = 0
for i in range(A, B + 1):
    if i % 2 == 0:
        suma += i
print("La suma de los números pares es:", suma)
