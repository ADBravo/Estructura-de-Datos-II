# Grafo dirigido con pesos usando diccionario de diccionarios
# Estructura: {origen: {destino: costo}}
vuelos = {
    'Bogotá': {'Medellín': 150, 'Cali': 200, 'Cartagena': 250},      # Vuelos desde Bogotá
    'Medellín': {'Bogotá': 160, 'Cartagena': 180},                   # Vuelos desde Medellín
    'Cali': {'Bogotá': 210, 'Cartagena': 220},                       # Vuelos desde Cali
    'Cartagena': {'Medellín': 190, 'Cali': 230},                     # Vuelos desde Cartagena
}

# Función para agregar una ruta de vuelo con su costo
def agregar_vuelo(grafo, origen, destino, costo):
    # Si la ciudad origen no existe, la creamos con diccionario vacío
    if origen not in grafo:
        grafo[origen] = {}
    # Agregamos el destino y su costo al diccionario del origen
    grafo[origen][destino] = costo

# Función para encontrar vuelos directos desde una ciudad
def vuelos_directos(grafo, ciudad):
    # Retornamos el diccionario de destinos desde la ciudad
    return grafo.get(ciudad, {})

# Función para verificar si existe vuelo directo entre dos ciudades
def existe_vuelo(grafo, origen, destino):
    # Verificamos si el origen existe y si el destino está en sus vuelos
    return origen in grafo and destino in grafo[origen]

# Función para obtener el costo de un vuelo directo
def costo_vuelo(grafo, origen, destino):
    # Obtenemos el costo si existe, sino retornamos None
    if existe_vuelo(grafo, origen, destino):
        return grafo[origen][destino]
    return None

# Probamos las funciones
print("Vuelos desde Bogotá:")
print(vuelos_directos(vuelos, 'Bogotá'))

print("\n¿Existe vuelo Medellín → Cali?:", existe_vuelo(vuelos, 'Medellín', 'Cali'))
print("Costo Bogotá → Cartagena: $", costo_vuelo(vuelos, 'Bogotá', 'Cartagena'))

# Agregamos un nuevo vuelo
agregar_vuelo(vuelos, 'Medellín', 'Cali', 170)
print("\nNuevo vuelo agregado Medellín → Cali: $", costo_vuelo(vuelos, 'Medellín', 'Cali'))