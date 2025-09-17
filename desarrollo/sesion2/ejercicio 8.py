# Lista de edades
edades = [20, 41, 6, 18, 23]

# Agregamos nuevos elementos a la lista
edades.append(12)
edades.append(22)
edades.append("valery")  # Incluso un string (mezcla de tipos en lista)

indice = 0
# Recorremos la lista completa con while
while indice < len(edades):
    print(edades[indice])
    indice += 1