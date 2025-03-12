# Construir una función que reciba como parámetro una lista de datos numéricos y que retorne el promedio de dichos datos.

print("----------------------------------------")
print("--------Promedio lista de datos---------")
print("----------------------------------------")

import random

# Definición de la función
def promedio_lista_datos(lista):
    suma = 0
    for i in lista:
        suma = suma + i
        promedio = suma / len(lista)
    return promedio

# input
# Creamos una lista vacía
lista = []
# Tamaño de la lista
n = int(input("Dígite el tamaño de la lista: "))

for i in range(n):
    num = random.randint(14,18)
    lista.append(num)

# processing
print("Lista: " , lista)
print("El promedio de la lista es: ", promedio_lista_datos(lista))

# output
print("\nEso era...")