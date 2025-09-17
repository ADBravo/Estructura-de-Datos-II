import numpy as np

# Dos listas de igual tamaño
lista1 = [10, 20, 30, 40, 50]
lista2 = [1, 2, 3, 4, 5]

vctr1 = np.array(lista1)
vctr2 = np.array(lista2)

print("vector lista 1")
print(vctr1)
print("vector lista 2")
print(vctr2)

# Multiplicación elemento a elemento
vctr_mult = vctr1 * vctr2
print("vector multiplicacion")
print(vctr_mult)

# División elemento a elemento
vctr_div = vctr1 / vctr2
print("vector division")
print(vctr_div)