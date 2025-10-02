class RedDistribucion:
    def __init__(self):
        # Diccionario de diccionarios {origen: {destino: capacidad}}
        self.red = {}

    def agregar_ruta(self, origen, destino, capacidad):
        if origen not in self.red:
            self.red[origen] = {}
        self.red[origen][destino] = capacidad

    def capacidad_ruta(self, origen, destino):
        return self.red.get(origen, {}).get(destino, None)

    def rutas_salientes(self, origen):
        return self.red.get(origen, {})

    def centro_mayor_capacidad(self):
        # Calcula el centro con mayor suma de capacidades de salida
        return max(self.red, key=lambda x: sum(self.red[x].values()))

    def capacidad_total(self):
        # Suma todas las capacidades de todas las rutas
        return sum(sum(destinos.values()) for destinos in self.red.values())


# Ejemplo
red = RedDistribucion()
red.agregar_ruta("A", "B", 50)
red.agregar_ruta("A", "C", 30)
red.agregar_ruta("B", "D", 40)

print("Capacidad A->B:", red.capacidad_ruta("A", "B"))
print("Rutas salientes de A:", red.rutas_salientes("A"))
print("Centro mayor capacidad:", red.centro_mayor_capacidad())
print("Capacidad total de la red:", red.capacidad_total())