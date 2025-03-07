# Construir una función que reciba una cadena digitada (como parámetro) por el usuario y que lo muestre n veces en la pantalla. El valor de n también es digitado por el usuario.

print("------------------------------------")
print("-Mostrar cadena n veces en pantalla-")
print("------------------------------------")

# Definición de la función
def mostrarNombre(cadena, n):
    for cadena in range(n):
        print(f"{n}  .  {cadena}") # type: ignore

# input
cadena = input("Dígite la cadena que desea mostrar en pantalla: ")
n = int(input("Dígite el número de veces que quiere mostrar la cadena: "))

# processing
mostrarNombre(cadena, n)

# output
print("\nEso era...")