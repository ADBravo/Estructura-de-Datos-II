# Grafo representado como diccionario: {estación: [conexiones]}
class RedMetro:
    def __init__(self):
        self.grafo = {}

    def agregar_estacion(self, estacion):
        # Si la estación no existe, se agrega con una lista vacía de conexiones
        if estacion not in self.grafo:
            self.grafo[estacion] = []

    def conectar_estaciones(self, est1, est2):
        # Como es un metro, las conexiones son bidireccionales
        if est1 in self.grafo and est2 in self.grafo:
            self.grafo[est1].append(est2)
            self.grafo[est2].append(est1)

    def estaciones_conectadas(self, estacion):
        # Devuelve las estaciones directamente conectadas a la dada
        return self.grafo.get(estacion, [])

    def contar_estaciones(self):
        # Número total de estaciones en la red
        return len(self.grafo)

    def estan_directamente_conectadas(self, est1, est2):
        # Verifica si hay conexión directa entre dos estaciones
        return est2 in self.grafo.get(est1, [])


# Ejemplo de uso
metro = RedMetro()
metro.agregar_estacion("A")
metro.agregar_estacion("B")
metro.agregar_estacion("C")
metro.conectar_estaciones("A", "B")
metro.conectar_estaciones("B", "C")

print("Estaciones conectadas a B:", metro.estaciones_conectadas("B"))
print("Total de estaciones:", metro.contar_estaciones())
print("¿A y C están conectadas directamente?", metro.estan_directamente_conectadas("A", "C"))