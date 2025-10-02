# Creamos un grafo no dirigido usando un diccionario
# Cada clave es una persona y el valor es una lista de sus amigos
red_social = {
    'Ana': ['Bob', 'Carlos', 'Diana'],      # Ana es amiga de Bob, Carlos y Diana
    'Bob': ['Ana', 'Carlos'],               # Bob es amigo de Ana y Carlos
    'Carlos': ['Ana', 'Bob', 'Elena'],      # Carlos tiene tres amigos
    'Diana': ['Ana', 'Elena'],              # Diana está conectada con Ana y Elena
    'Elena': ['Carlos', 'Diana']            # Elena es amiga de Carlos y Diana
}

# Función para agregar una nueva amistad (bidireccional)
def agregar_amistad(grafo, persona1, persona2):
    # Si la persona1 no existe en el grafo, la agregamos con lista vacía
    if persona1 not in grafo:
        grafo[persona1] = []
    # Si la persona2 no existe en el grafo, la agregamos con lista vacía
    if persona2 not in grafo:
        grafo[persona2] = []
    
    # Agregamos la amistad en ambas direcciones (grafo no dirigido)
    grafo[persona1].append(persona2)
    grafo[persona2].append(persona1)

# Función para encontrar amigos en común entre dos personas
def amigos_en_comun(grafo, persona1, persona2):
    # Convertimos las listas a conjuntos y encontramos la intersección
    amigos1 = set(grafo.get(persona1, []))  # Amigos de persona1
    amigos2 = set(grafo.get(persona2, []))  # Amigos de persona2
    return amigos1.intersection(amigos2)     # Retornamos amigos comunes

# Probamos las funciones
print("Red Social:")
print(red_social)
print("\nAmigos en común entre Ana y Elena:")
print(amigos_en_comun(red_social, 'Ana', 'Elena'))

# Agregamos una nueva amistad
agregar_amistad(red_social, 'Bob', 'Elena')
print("\nDespués de agregar amistad Bob-Elena:")
print(red_social['Bob'])