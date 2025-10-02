# Matriz de adyacencia usando listas de listas
# 0 significa que no hay conexión directa
# Los números representan distancias en kilómetros
ciudades = ['A', 'B', 'C', 'D']  # Lista de nombres de ciudades

# Matriz donde [i][j] es la distancia de ciudad i a ciudad j
# Índices: A=0, B=1, C=2, D=3
matriz_distancias = [
    [0, 100, 0, 150],    # Distancias desde ciudad A: A-B=100km, A-D=150km
    [100, 0, 200, 0],    # Distancias desde ciudad B: B-A=100km, B-C=200km
    [0, 200, 0, 50],     # Distancias desde ciudad C: C-B=200km, C-D=50km
    [150, 0, 50, 0]      # Distancias desde ciudad D: D-A=150km, D-C=50km
]

# Función para obtener la distancia entre dos ciudades por nombre
def obtener_distancia(matriz, nombres, ciudad1, ciudad2):
    # Encontramos los índices de las ciudades en la lista de nombres
    try:
        indice1 = nombres.index(ciudad1)
        indice2 = nombres.index(ciudad2)
        # Retornamos la distancia de la matriz
        distancia = matriz[indice1][indice2]
        # Si es 0, no hay conexión directa
        return distancia if distancia > 0 else None
    except ValueError:
        # Si alguna ciudad no existe, retornamos None
        return None

# Función para obtener todas las ciudades conectadas directamente a una ciudad
def ciudades_conectadas(matriz, nombres, ciudad):
    try:
        # Obtenemos el índice de la ciudad
        indice = nombres.index(ciudad)
        conectadas = []  # Lista para almacenar ciudades conectadas
        # Recorremos la fila de la matriz correspondiente a la ciudad
        for i, distancia in enumerate(matriz[indice]):
            # Si hay distancia (mayor a 0) y no es la misma ciudad
            if distancia > 0 and i != indice:
                # Agregamos la ciudad con su distancia
                conectadas.append((nombres[i], distancia))
        return conectadas
    except ValueError:
        return []

# Función para verificar si el grafo es simétrico (no dirigido)
def es_simetrico(matriz):
    n = len(matriz)  # Tamaño de la matriz
    # Verificamos que matriz[i][j] == matriz[j][i] para todos los pares
    for i in range(n):
        for j in range(n):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True

# Función para imprimir la matriz de forma legible
def imprimir_matriz(matriz, nombres):
    # Imprimimos encabezado con nombres de ciudades
    print("    ", end="")
    for nombre in nombres:
        print(f"{nombre:>6}", end="")
    print()
    
    # Imprimimos cada fila con su nombre de ciudad
    for i, fila in enumerate(matriz):
        print(f"{nombres[i]:>3} ", end="")
        for valor in fila:
            print(f"{valor:>6}", end="")
        print()

# Probamos las funciones
print("Matriz de Distancias:")
imprimir_matriz(matriz_distancias, ciudades)

print("\n¿Es un grafo simétrico (no dirigido)?:", es_simetrico(matriz_distancias))
print("\nDistancia A → D:", obtener_distancia(matriz_distancias, ciudades, 'A', 'D'), "km")
print("\nCiudades conectadas a C:", ciudades_conectadas(matriz_distancias, ciudades, 'C'))