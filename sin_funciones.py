print("---------------------------------")
print("-Buscar un número en un conjunto-")
print("----------------------------------")

# input
b = int(input("Número a buscar: ")) # se recibe el dato del usuario

# processing
a = [1,2,3,4,5] # se almacena una lista de datos
r = False # se inicia la variable r con un valor Falso

for i in a:
    if i == b:
        print("Lo encontré")
        r = True
if r  == False:
    print("No lo encontré")

# output
print("\nEso era...")    