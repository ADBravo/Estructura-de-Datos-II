# Árbol N-ario (cada nodo puede tener múltiples hijos) con diccionarios
# Representa un sistema de archivos

# Crear estructura de carpetas y archivos
sistema_archivos = {
    'nombre': 'raiz',  # Nombre del directorio
    'tipo': 'carpeta',  # Tipo de nodo
    'hijos': [  # Lista de hijos (subcarpetas y archivos)
        {
            'nombre': 'documentos',
            'tipo': 'carpeta',
            'hijos': [
                {'nombre': 'trabajo.pdf', 'tipo': 'archivo', 'tamaño': 150},
                {'nombre': 'personal.docx', 'tipo': 'archivo', 'tamaño': 80}
            ]
        },
        {
            'nombre': 'imagenes',
            'tipo': 'carpeta',
            'hijos': [
                {'nombre': 'foto1.jpg', 'tipo': 'archivo', 'tamaño': 200},
                {'nombre': 'foto2.png', 'tipo': 'archivo', 'tamaño': 300}
            ]
        },
        {'nombre': 'readme.txt', 'tipo': 'archivo', 'tamaño': 10}
    ]
}

# Función para mostrar la estructura del árbol con indentación
def mostrar_arbol(nodo, nivel=0):
    # Crear indentación según el nivel de profundidad
    indentacion = "  " * nivel
    
    # Mostrar información del nodo actual
    if nodo['tipo'] == 'carpeta':
        print(f"{indentacion}📁 {nodo['nombre']}/")
    else:
        print(f"{indentacion}📄 {nodo['nombre']} ({nodo['tamaño']} KB)")
    
    # Recorrer recursivamente los hijos si existen
    if 'hijos' in nodo:
        for hijo in nodo['hijos']:
            mostrar_arbol(hijo, nivel + 1)

# Función para calcular el tamaño total del árbol
def calcular_tamaño(nodo):
    # Si es un archivo, devolver su tamaño
    if nodo['tipo'] == 'archivo':
        return nodo['tamaño']
    
    # Si es carpeta, sumar el tamaño de todos los hijos
    tamaño_total = 0
    if 'hijos' in nodo:
        for hijo in nodo['hijos']:
            tamaño_total += calcular_tamaño(hijo)
    
    return tamaño_total

# Mostrar la estructura del sistema de archivos
print("Estructura del sistema de archivos:")
mostrar_arbol(sistema_archivos)

# Calcular y mostrar el tamaño total
tamaño = calcular_tamaño(sistema_archivos)
print(f"\nTamaño total: {tamaño} KB")  # Salida: 740 KB