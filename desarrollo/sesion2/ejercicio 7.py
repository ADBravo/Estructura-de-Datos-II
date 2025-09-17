# Lista de edades
edades = [20, 41, 6, 18, 23]
indice = 0  # Inicializamos el índice

# Recorremos con while saltando de 2 en 2
while indice < len(edades):
    print(edades[indice])  # Imprime solo posiciones pares de la lista
    indice += 2  # Incrementa de 2 en 2