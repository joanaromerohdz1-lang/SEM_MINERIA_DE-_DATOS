import pandas as pd
import numpy as np
from numpy import random

# #TIPOS DE ARRAY
# array_0 = np.array(5)

# #arreglo de 1 sola dimension
# array_1 = np.array([1,2,3,4,5,6])

# #arreglo de 2 dimensiones
# array_2 = np.array([[1,2,3],[4,5,6]])

# #arreglo de 3 dimensiones
# array_3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

# #INDEXAR LOS ARRAY
# print(array_1[0])
# print(array_2[0][1]) #selecionar fila(0) ,columna (1)
# #ver el elemento 5
# print(array_2[1][1]) 
# #ver el elemento 4 del array 3
# print(array_3[0][1][0]) #primero la dimeension,fila,columa
# #ver el elemento 7 del array 3
# print(array_3[1][0][0]) #dimension,fila,columa

# #Metodo Shape -->mueestra la forma en que esta compuetsa la matriz o arreglo
# print(array_1.shape)
# print(array_2.shape)
# print(array_3.shape)

# #Metodo Reshape --->reestructurar
# print(array_1.reshape(1,6))
# print(array_2.reshape(3,2))
# print(array_3.reshape(2,3,2))

# #Metodo Concatenacion
# #unir el primerp con el primero
# print(np.concatenate((array_1,array_1))) 


# #Metodo Split   --->separar los elementos y deben ser divisibles
# print(np.split(array_1,2))

# print(np.split(array_1,3))

# #Metodo WHERE -->Hacer una busquedad
# print(np.where(array_1==3))

# #Metodo Sort  ---->ordenar ascendente

# arrayN=np.array([10,58,2,8,7,6])
# print(np.sort(arrayN))

# #Metodo Sort  ---->ordenar decendente
# arrayN=np.array([10,58,2,8,7,6])
# print(np.sort(arrayN))
# print(np.sort(arrayN)[::-1])


#Metodo Random  --->matrices con numeros aleatorios ENTEROS



numero = random.randint(100,200,1)#(inicio,fin,num elmntos)
#print(numero)


numero = random.randint(10,size=(5))
#print(numero)

numero = random.randint(10,size=(2,3))
#print(numero)


#Metodo Random  --->matrices con numeros aleatorios DECIMALES
numero = random.rand()
#print(round(numero,2)) #----1>solo 2 decimales


numero2 = random.rand()+5
#print(numero2)


numero3 = random.rand(3,5)
#print(numero3)

#LISTAS  ---->acceder aletoriamente a los elementos de una lista
lista_nombres = ["Juan","Pedro","Maria"]
print(random.choice(lista_nombres))