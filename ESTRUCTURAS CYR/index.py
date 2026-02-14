print("HOLA MUNDO")

numero=10.0
texto= "Esto es un texto"
verdadero=True
falso=False
print(numero)
mi_lista=[1,2,3,4,5]
print(mi_lista[3])

mi_diccionaario = {
    "nombre":"Juan",
    "edad":30,
    "ciudad":"Madrid"
}

print(mi_diccionaario["edad"])

#OPERADORES
suma=5+5
resta=5-4
multi=5*5
divi=18/2
modulo=10%2
print(modulo)

#OPERADORES OR,AND,NOT =LOGICOS


#ESTRUCTURAS DE CONTROL CONDICIONALES
numeros=10
if numeros > 0:
    print("EL NUMERO ES POSITIVO")
elif numeros < 0:
    print("EL NUMERO ES NEGATIVO")
else:
    print("EL NUMERO ES CERO")


#MATCH CASE
color = "rojo" 
match color:
    case "rojo":
        print("El color es rojo")
    case "azul":
        print("El color es azul ")
    case _:
        print("El color no es rojo ni azul")

#FUNCIONES
def sumar(a,b):
    return a+b

resultado = sumar(5,9)
print(resultado)

#BUCLES
animales= ["perro","gato","conejo"]
for animal in animales:
    print(animal)

for i in range(5):
    print(i)

for i in range(2, 21,2):
    print(i)