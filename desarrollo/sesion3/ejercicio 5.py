import numpy as np

# Dos listas de números de igual tamaño
lista1 = [10, 20, 30, 40, 50]
lista2 = [1, 2, 3, 4, 5]

# Convertimos a vectores numpy
vctr1 = np.array(lista1)
vctr2 = np.array(lista2)

print("vector lista 1")
print(vctr1)
print("vector lista 2")
print(vctr2)

# Suma elemento a elemento
vctr_add = vctr1 + vctr2
print("vector suma")
print(vctr_add)