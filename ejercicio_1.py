# Construir una función que reciba su nombre como parámetro y que lo muestre 5 veces en la pantalla.

print("---------------------------------")
print("--------Tú nombre 5 veces--------")
print("---------------------------------")

def NombrePor5(nombre):
   for i in range(1,6):
      print(f"{i} . {nombre}")

# input
nombre = input("Dígite su nombre: ")

# processing
NombrePor5(nombre)

# output
print("\nEso era...")