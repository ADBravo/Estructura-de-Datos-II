class Colaboraciones:
    def __init__(self):
        # Diccionario {empleado: {proyectos}}
        self.empleados = {}

    def agregar_empleado(self, nombre, proyectos):
        self.empleados[nombre] = set(proyectos)

    def empleados_similares(self, empleado):
        # Encuentra empleados que compartan al menos un proyecto
        return [e for e, proy in self.empleados.items() if e != empleado and proy & self.empleados[empleado]]

    def proyectos_no_participa(self, empleado):
        # Todos los proyectos - los del empleado
        todos = set().union(*self.empleados.values())
        return todos - self.empleados[empleado]

    def formar_equipo(self, requeridos):
        # Encuentra empleados que en conjunto cubran los proyectos requeridos
        for e1 in self.empleados:
            for e2 in self.empleados:
                if e1 != e2 and (self.empleados[e1] | self.empleados[e2]) >= requeridos:
                    return e1, e2
        return None

    def grado_colaboracion(self, emp1, emp2):
        return len(self.empleados[emp1] & self.empleados[emp2])


# Ejemplo
colab = Colaboraciones()
colab.agregar_empleado("Ana", ["Proyecto1", "Proyecto2"])
colab.agregar_empleado("Luis", ["Proyecto2", "Proyecto3"])
colab.agregar_empleado("Marta", ["Proyecto4"])

print("Similares a Ana:", colab.empleados_similares("Ana"))
print("Proyectos donde no trabaja Luis:", colab.proyectos_no_participa("Luis"))
print("Equipo para cubrir {P1,P3}:", colab.formar_equipo({"Proyecto1", "Proyecto3"}))
print("Grado colaboración Ana y Luis:", colab.grado_colaboracion("Ana", "Luis"))