# Definición de un nodo para Árbol Binario
class NodoBinario:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None   # Hijo izquierdo
        self.derecho = None     # Hijo derecho

# Creamos un árbol binario de ejemplo
#        1
#       / \
#      2   3
#     / \
#    4   5
raiz_bin = NodoBinario(1)
raiz_bin.izquierdo = NodoBinario(2)
raiz_bin.derecho = NodoBinario(3)
raiz_bin.izquierdo.izquierdo = NodoBinario(4)
raiz_bin.izquierdo.derecho = NodoBinario(5)

# Función para contar hojas en árbol binario
def contar_hojas_binario(arbol):
    # Caso base: si el árbol está vacío, no hay hojas
    if arbol is None:
        return 0
    
    # Si no tiene hijos izquierdo ni derecho → es una hoja
    if arbol.izquierdo is None and arbol.derecho is None:
        return 1
    
    # Si no es hoja, contamos hojas en subárbol izquierdo + derecho
    return contar_hojas_binario(arbol.izquierdo) + contar_hojas_binario(arbol.derecho)

# Definición de un nodo para Árbol N-ario
class NodoNario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hijos = []  # Lista de hijos (puede tener muchos)

# Creamos un árbol N-ario de ejemplo
#     Raíz
#    /    \
# Hijo1   Hijo2
#   |       |
# Nieto1  Nieto2
raiz_nario = NodoNario("Raíz")
hijo1 = NodoNario("Hijo1")
hijo2 = NodoNario("Hijo2")
raiz_nario.hijos.extend([hijo1, hijo2])
hijo1.hijos.append(NodoNario("Nieto1"))
hijo2.hijos.append(NodoNario("Nieto2"))

# Función para contar hojas en árbol N-ario
def contar_hojas_nario(nodo):
    # Caso base: si el nodo está vacío → 0 hojas
    if nodo is None:
        return 0
    
    # Si no tiene hijos → es una hoja
    if len(nodo.hijos) == 0:
        return 1
    
    # Si tiene hijos → contamos hojas de cada hijo recursivamente
    return sum(contar_hojas_nario(hijo) for hijo in nodo.hijos)

# Ejecución de ejemplos
print("Hojas en árbol binario:", contar_hojas_binario(raiz_bin))  # Esperado: 3 (nodos 4, 5, 3)
print("Hojas en árbol N-ario:", contar_hojas_nario(raiz_nario))  # Esperado: 2 (Nieto1, Nieto2)
