# Definición de un nodo para Árbol Binario
class NodoBinario:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None   # Hijo izquierdo
        self.derecho = None     # Hijo derecho

# ==============================================
# Creamos un árbol binario de ejemplo
#        1
#       / \
#      2   3
#     / \
#    4   5
# Este árbol está balanceado
# ==============================================
raiz_bin = NodoBinario(1)
raiz_bin.izquierdo = NodoBinario(2)
raiz_bin.derecho = NodoBinario(3)
raiz_bin.izquierdo.izquierdo = NodoBinario(4)
raiz_bin.izquierdo.derecho = NodoBinario(5)

# Función que determina si un árbol está balanceado
def esta_balanceado(arbol):
    # Función auxiliar que devuelve:
    # - la altura del subárbol
    # - si el subárbol está balanceado o no
    def verificar(nodo):
        # Caso base: árbol vacío → altura 0 y está balanceado
        if nodo is None:
            return 0, True
        
        # Calculamos recursivamente la altura y balance de subárbol izquierdo
        izq_altura, izq_bal = verificar(nodo.izquierdo)
        
        # Calculamos recursivamente la altura y balance de subárbol derecho
        der_altura, der_bal = verificar(nodo.derecho)

        # La altura del nodo actual es 1 + la mayor altura entre sus hijos
        altura = 1 + max(izq_altura, der_altura)

        # Un nodo está balanceado si:
        # - la diferencia de alturas de sus hijos es ≤ 1
        # - y sus dos subárboles también están balanceados
        balanceado = abs(izq_altura - der_altura) <= 1 and izq_bal and der_bal

        return altura, balanceado
    
    # Llamamos a la función auxiliar y nos quedamos solo con "si está balanceado"
    return verificar(arbol)[1]

# Ejecución de ejemplo
print("¿Está balanceado el árbol binario?:", esta_balanceado(raiz_bin))  
# Esperado: True