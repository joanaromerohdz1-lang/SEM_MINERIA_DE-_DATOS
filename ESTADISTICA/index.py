from estadisticas import Estadistica

lista_numeros = [2,4,6,8,4,6,4]

estadistica = Estadistica(lista_numeros)

print("Media:",estadistica.calcular_media())
print("Mediana:",estadistica.calcular_mediana())
print("Moda:",estadistica.calcular_moda())

