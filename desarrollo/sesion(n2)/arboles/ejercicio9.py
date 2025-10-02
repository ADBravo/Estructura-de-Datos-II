# Cada persona será representada con un diccionario
def crear_persona(nombre, edad):
    return {"nombre": nombre, "edad": edad, "hijos": []}

# Agregar hijo a una persona
def agregar_hijo(padre, hijo):
    padre["hijos"].append(hijo)

# Buscar persona por nombre (recursivo)
def buscar_persona(persona, nombre):
    if persona["nombre"] == nombre:
        return persona
    for hijo in persona["hijos"]:
        resultado = buscar_persona(hijo, nombre)
        if resultado:
            return resultado
    return None

# Mostrar árbol genealógico completo
def mostrar_arbol(persona, nivel=0):
    print("  " * nivel + f"{persona['nombre']} ({persona['edad']} años)")
    for hijo in persona["hijos"]:
        mostrar_arbol(hijo, nivel + 1)

# Calcular promedio de edades
def promedio_edad(persona):
    edades = []

    def recolectar(persona):
        edades.append(persona["edad"])
        for hijo in persona["hijos"]:
            recolectar(hijo)

    recolectar(persona)
    return sum(edades) / len(edades)

# Ejemplo de árbol genealógico
abuelo = crear_persona("Juan", 75)
padre = crear_persona("Carlos", 50)
hijo = crear_persona("Luis", 20)

agregar_hijo(abuelo, padre)
agregar_hijo(padre, hijo)

mostrar_arbol(abuelo)
print("Promedio de edad:", promedio_edad(abuelo))  