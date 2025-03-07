print("---------------------------------")
print("-Buscar un número en un conjunto-")
print("----------------------------------")

# definición de la función
def buscarDatoEnLista(DatoABuscar, lista):
    r = False
    for i in lista:
        if i == DatoABuscar:
          r = True
    return r

# input
dato = int(input("Número a buscar: ")) # se recibe el dato del usuario

# processing
lista = [1,2,3,4,5] # se almacena una lista de datos
if buscarDatoEnLista(dato, lista):
   print("Lo encontré.")
else:
   print("No  lo encontré.")

# output
print("\nEso era...")