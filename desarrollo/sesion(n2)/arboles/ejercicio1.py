# Árbol binario representado con listas
# Estructura: [valor, hijo_izquierdo, hijo_derecho]

# Crear el árbol
#       1
#      / \
#     2   3
#    / \
#   4   5

def crear_nodo(valor, izquierdo=None, derecho=None):
    # Función para crear un nodo con valor e hijos opcionales
    return [valor, izquierdo, derecho]

# Construir el árbol de abajo hacia arriba
nodo4 = crear_nodo(4)  # Hoja izquierda
nodo5 = crear_nodo(5)  # Hoja derecha
nodo2 = crear_nodo(2, nodo4, nodo5)  # Nodo con dos hijos
nodo3 = crear_nodo(3)  # Hoja derecha de la raíz
raiz = crear_nodo(1, nodo2, nodo3)  # Raíz del árbol

# Función para recorrer el árbol en preorden (raíz-izquierda-derecha)
def recorrer_preorden(nodo):
    if nodo is None:  # Caso base: nodo vacío
        return
    print(nodo[0], end=" ")  # Imprimir valor del nodo
    recorrer_preorden(nodo[1])  # Recorrer subárbol izquierdo
    recorrer_preorden(nodo[2])  # Recorrer subárbol derecho

print("Recorrido en preorden:")
recorrer_preorden(raiz)  # Salida: 1 2 4 5 3