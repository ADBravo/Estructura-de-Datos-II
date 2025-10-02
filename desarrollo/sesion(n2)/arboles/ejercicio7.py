# Definimos un nodo para un árbol N-ario (puede tener varios hijos)
class NodoNario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hijos = []  # Lista de hijos

# Función para buscar un valor en el árbol N-ario
def buscar(nodo, nombre_buscado):
    # Caso base: si el nodo es None, devolvemos False
    if nodo is None:
        return False
    # Si encontramos el nombre, retornamos True
    if nodo.nombre == nombre_buscado:
        return True
    # Recorremos recursivamente todos los hijos
    for hijo in nodo.hijos:
        if buscar(hijo, nombre_buscado):
            return True
    # Si no encontramos nada en este nodo ni en sus hijos
    return False

# Ejemplo de sistema de archivos como árbol
raiz = NodoNario("C:/")
docs = NodoNario("Documentos")
img = NodoNario("Imagenes")
raiz.hijos.extend([docs, img])
docs.hijos.append(NodoNario("archivo1.txt"))
img.hijos.append(NodoNario("foto.jpg"))

print("¿Existe 'foto.jpg'?:", buscar(raiz, "foto.jpg"))  # True
print("¿Existe 'video.mp4'?:", buscar(raiz, "video.mp4"))  # False