# Grafo usando diccionario de conjuntos (sets)
# Cada usuario tiene un conjunto de intereses/categorías
usuarios_intereses = {
    'Juan': {'Python', 'IA', 'Machine Learning', 'Grafos'},        # Intereses de Juan
    'María': {'JavaScript', 'Web', 'React', 'Node.js'},            # Intereses de María
    'Pedro': {'Python', 'Data Science', 'Machine Learning'},       # Intereses de Pedro
    'Ana': {'Python', 'IA', 'Deep Learning', 'TensorFlow'},        # Intereses de Ana
    'Luis': {'Web', 'CSS', 'JavaScript', 'HTML'}                   # Intereses de Luis
}

# Función para agregar un nuevo interés a un usuario
def agregar_interes(grafo, usuario, interes):
    # Si el usuario no existe, creamos un conjunto vacío para él
    if usuario not in grafo:
        grafo[usuario] = set()
    # Agregamos el interés al conjunto del usuario
    grafo[usuario].add(interes)

# Función para encontrar usuarios con intereses similares
def usuarios_similares(grafo, usuario):
    # Si el usuario no existe, retornamos diccionario vacío
    if usuario not in grafo:
        return {}
    
    intereses_usuario = grafo[usuario]  # Intereses del usuario objetivo
    similitudes = {}  # Diccionario para almacenar similitudes
    
    # Comparamos con cada otro usuario
    for otro_usuario, intereses_otro in grafo.items():
        # No comparamos al usuario consigo mismo
        if otro_usuario != usuario:
            # Calculamos intersección de intereses (intereses comunes)
            comunes = intereses_usuario.intersection(intereses_otro)
            # Si hay intereses comunes, guardamos la cantidad
            if comunes:
                similitudes[otro_usuario] = len(comunes)
    
    # Retornamos diccionario ordenado por similitud (mayor a menor)
    return dict(sorted(similitudes.items(), key=lambda x: x[1], reverse=True))

# Función para recomendar nuevos intereses basados en usuarios similares
def recomendar_intereses(grafo, usuario):
    # Obtenemos usuarios similares
    similares = usuarios_similares(grafo, usuario)
    
    # Si no hay usuarios similares, no hay recomendaciones
    if not similares:
        return set()
    
    intereses_actuales = grafo[usuario]  # Intereses que ya tiene el usuario
    recomendaciones = set()  # Conjunto para almacenar recomendaciones
    
    # Recorremos usuarios similares (ya están ordenados por similitud)
    for usuario_similar in similares.keys():
        # Obtenemos intereses del usuario similar que no tiene el usuario actual
        nuevos = grafo[usuario_similar].difference(intereses_actuales)
        # Agregamos estos intereses a las recomendaciones
        recomendaciones.update(nuevos)
    
    return recomendaciones

# Función para encontrar intereses comunes entre dos usuarios
def intereses_comunes(grafo, usuario1, usuario2):
    # Si algún usuario no existe, retornamos conjunto vacío
    if usuario1 not in grafo or usuario2 not in grafo:
        return set()
    # Retornamos la intersección de los conjuntos de intereses
    return grafo[usuario1].intersection(grafo[usuario2])

# Función para calcular índice de similitud de Jaccard entre dos usuarios
def similitud_jaccard(grafo, usuario1, usuario2):
    # Si algún usuario no existe, retornamos 0
    if usuario1 not in grafo or usuario2 not in grafo:
        return 0
    
    # Obtenemos los conjuntos de intereses
    intereses1 = grafo[usuario1]
    intereses2 = grafo[usuario2]
    
    # Calculamos intersección (intereses comunes) y unión (todos los intereses)
    interseccion = len(intereses1.intersection(intereses2))
    union = len(intereses1.union(intereses2))
    
    # Evitamos división por cero
    if union == 0:
        return 0
    
    # Índice de Jaccard = intersección / unión
    return interseccion / union

# Probamos las funciones
print("Usuarios Similares a Juan:")
print(usuarios_similares(usuarios_intereses, 'Juan'))

print("\nIntereses comunes entre Juan y Ana:")
print(intereses_comunes(usuarios_intereses, 'Juan', 'Ana'))

print("\nRecomendaciones para Juan:")
print(recomendar_intereses(usuarios_intereses, 'Juan'))

print("\nSimilitud Jaccard entre Juan y Pedro:", 
      f"{similitud_jaccard(usuarios_intereses, 'Juan', 'Pedro'):.2f}")

# Agregamos un nuevo interés
agregar_interes(usuarios_intereses, 'Juan', 'Deep Learning')
print("\nIntereses actualizados de Juan:", usuarios_intereses['Juan'])