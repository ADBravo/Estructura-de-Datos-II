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

# Resta elemento a elemento
vctr_add = vctr1 - vctr2
print("vector resta")
print(vctr_add)