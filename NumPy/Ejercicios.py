#-----------------------------------------------EJERCICIOS NUMPY----------------------------------------
import pandas as pd
import numpy as np
from numpy import random

#Crea un array de 10 números aleatorios enteros entre 0 y 100.
numero10 = random.randint(0,100,10)#(inicio,fin,num elmntos)
print(numero10)

#Crea un array de 5 números aleatorios decimales entre 0 y 1.
array_5_dec = np.random.rand(5)
print(array_5_dec)

#Crea dos arrays de números aleatorios enteros de longitud 5 y concaténalos.
# Generamos dos arrays distintos con números al azar
a = np.random.randint(0, 10, 5) 
b = np.random.randint(0, 10, 5)
print(np.concatenate((a, b)))

#Crea dos arrays de números aleatorios enteros de longitud 5 y concaténalos.
array1 = np.random.randint(0, 50, size=5)
array2= np.random.randint(0, 50, size=5)
concatenado = np.concatenate((array1, array2))
print(concatenado)

#Crea un array de 10 números aleatorios enteros y sepáralo en dos arrays de 5 elementos cada uno.
original = np.random.randint(0, 100, size=10)
parte_1, parte_2 = np.split(original, 2)
print(original)

#Crea una matriz de 3x3 con números aleatorios decimales entre 0 y 1.
matriz_3x3 = np.random.rand(3, 3)
print(matriz_3x3)

#Crea un array de 10 números aleatorios enteros y selecciona 3 elementos al azar.
array_para_muestreo = np.random.randint(0, 100, size=10)
seleccion_azar = np.random.choice(array_para_muestreo, size=3, replace=False)
print(seleccion_azar)

#Crea un array de 10 números aleatorios enteros entre 0 y 100 y calcula la media.
array_media = np.random.randint(0, 101, size=10)
media = np.mean(array_media)
print(media)