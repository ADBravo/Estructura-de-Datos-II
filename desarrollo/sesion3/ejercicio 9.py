import numpy as np

# Dos listas del mismo tamaño
lista1 = [10, 20, 30, 40, 50]
lista2 = [1, 1, 1, 1, 1]

vctr1 = np.array(lista1)
vctr2 = np.array(lista2)

print("vector lista 1")
print(vctr1)
print("vector lista 2")
print(vctr2)

# Producto punto (suma de multiplicaciones elemento a elemento)
vctr_dot = vctr1.dot(vctr2)
print("vector producto punto")
print(vctr_dot)  # En este caso devuelve la suma de los elementos de vctr1