# Construir una función que reciba como parámetro una lista de datos numéricos y retorne la suma de dichos datos.

import random
print("------------------------------------")
print("--------Suma lista de datos---------")
print("------------------------------------")

# Definición de la función
def sumar_lista_datos(lista):
    suma = 0
    for i in lista:
        suma = suma + i
    return suma

# input
# Creamos una lista vacía
lista = [ ]
# Tamaño de la lista
n = int(input("Dígite el tamaño de la lista: "))

for i in range(n):
    num = random.randint(1,9)
    lista.append(num)

# processing
print("Lista: " , lista)
print("La suma es: ", sumar_lista_datos(lista))

# output
print("\nEso era...")