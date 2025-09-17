import numpy as np

# Dos listas con tamaños diferentes
lista1 = [10, 20, 30, 40, 50]
lista2 = [1, 2, 3, 4, 5, 6, 7]

vctr1 = np.array(lista1)
vctr2 = np.array(lista2)

print("vector lista 1")
print(vctr1)
print("vector lista 2")
print(vctr2)

# Esto lanzará un error porque numpy no puede sumar vectores de distinto tamaño
vctr_add = vctr1 + vctr2
print("vector suma")
print(vctr_add)