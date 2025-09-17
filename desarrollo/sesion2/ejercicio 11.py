# Dos listas paralelas: nombres y cédulas
nombres = ["Daniel", "Alejandro", "jose"]
cedulas = ["123", "456", "789"]

# Eliminamos en la misma posición (índice 1)
nombres.pop(1)   # Elimina "Alejandro"
cedulas.pop(1)   # Elimina "456"

print(nombres)   # Imprime nombres restantes
print(cedulas)   # Imprime cédulas restantes

# Recorremos la lista de nombres
for nombre in nombres:
    print(nombre)
    # Por cada nombre recorremos todas las cédulas
    for cedula in cedulas:
        print(cedula)