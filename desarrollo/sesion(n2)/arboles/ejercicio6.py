# Definimos una clase para representar un nodo de un árbol binario
class NodoBinario:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

# Función para calcular la altura de un árbol binario
def altura(arbol):
    # Caso base: si el árbol está vacío, su altura es 0
    if arbol is None:
        return 0
    # Recursivamente calculamos la altura de los subárboles izquierdo y derecho
    altura_izquierda = altura(arbol.izquierdo)
    altura_derecha = altura(arbol.derecho)
    # La altura del árbol es 1 + la altura máxima de sus subárboles
    return 1 + max(altura_izquierda, altura_derecha)

# Ejemplo de uso
raiz = NodoBinario(1)
raiz.izquierdo = NodoBinario(2)
raiz.derecho = NodoBinario(3)
raiz.izquierdo.izquierdo = NodoBinario(4)
raiz.izquierdo.derecho = NodoBinario(5)

print("Altura del árbol:", altura(raiz))  # Salida esperada: 3