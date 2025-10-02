# Grafo dirigido usando lista de tuplas (origen, destino)
# Cada tupla representa una dependencia: (tarea_prerequisito, tarea_dependiente)
dependencias = [
    ('Diseño', 'Desarrollo'),           # Desarrollo requiere que Diseño esté completo
    ('Desarrollo', 'Testing'),          # Testing requiere que Desarrollo esté completo
    ('Testing', 'Despliegue'),          # Despliegue requiere que Testing esté completo
    ('Diseño', 'Documentación'),        # Documentación puede empezar después de Diseño
    ('Documentación', 'Despliegue'),    # Despliegue también requiere Documentación
]

# Función para convertir lista de tuplas a diccionario (más eficiente para consultas)
def crear_grafo_dependencias(lista_dependencias):
    grafo = {}  # Diccionario vacío para almacenar el grafo
    # Recorremos cada dependencia en la lista
    for prerequisito, tarea in lista_dependencias:
        # Si la tarea no existe en el grafo, la agregamos con lista vacía
        if tarea not in grafo:
            grafo[tarea] = []
        # Agregamos el prerequisito a la lista de dependencias de la tarea
        grafo[tarea].append(prerequisito)
    return grafo

# Función para encontrar todas las tareas que no tienen prerequisitos
def tareas_iniciales(lista_dependencias):
    # Conjunto de todas las tareas que son prerequisito de algo
    con_prerequisitos = set(tarea for _, tarea in lista_dependencias)
    # Conjunto de todas las tareas que aparecen como prerequisito
    todas_tareas = set(prereq for prereq, _ in lista_dependencias)
    # Retornamos las tareas que son prerequisito pero no dependen de nada
    return todas_tareas - con_prerequisitos

# Función para obtener todas las tareas únicas del proyecto
def obtener_todas_tareas(lista_dependencias):
    tareas = set()  # Conjunto para evitar duplicados
    # Agregamos todas las tareas (prerequisitos y dependientes)
    for prereq, tarea in lista_dependencias:
        tareas.add(prereq)
        tareas.add(tarea)
    return tareas

# Función para verificar si una tarea es prerequisito directo de otra
def es_prerequisito_directo(lista_dependencias, prereq, tarea):
    # Verificamos si existe la tupla (prereq, tarea) en la lista
    return (prereq, tarea) in lista_dependencias

# Probamos las funciones
print("Tareas del proyecto:", obtener_todas_tareas(dependencias))
print("\nTareas iniciales (sin prerequisitos):", tareas_iniciales(dependencias))

grafo_tareas = crear_grafo_dependencias(dependencias)
print("\nPrerequisitos para 'Despliegue':", grafo_tareas.get('Despliegue', []))
print("\n¿'Diseño' es prerequisito de 'Testing'?:", 
      es_prerequisito_directo(dependencias, 'Diseño', 'Testing'))