class SistemaCursos:
    def __init__(self):
        # Diccionario {curso: [prerrequisitos]}
        self.cursos = {}

    def agregar_curso(self, curso, prerequisitos=[]):
        self.cursos[curso] = prerequisitos

    def prerequisitos_de(self, curso):
        return self.cursos.get(curso, [])

    def cursos_iniciales(self):
        # Cursos sin prerrequisitos
        return [curso for curso, prereqs in self.cursos.items() if not prereqs]

    def puede_tomar(self, curso, completados):
        # Se puede tomar si TODOS los prerequisitos ya están completados
        return all(pr in completados for pr in self.cursos.get(curso, []))

    def sugerir_cursos(self, completados):
        # Devuelve cursos que puede tomar dado lo que ya completó
        return [curso for curso in self.cursos if self.puede_tomar(curso, completados)]


# Ejemplo
sistema = SistemaCursos()
sistema.agregar_curso("Programación I")
sistema.agregar_curso("Programación II", ["Programación I"])
sistema.agregar_curso("Algoritmos", ["Programación II"])
sistema.agregar_curso("Bases de Datos", ["Programación II"])

print("Cursos iniciales:", sistema.cursos_iniciales())
print("¿Puede tomar Algoritmos si completó Prog I y II?", sistema.puede_tomar("Algoritmos", ["Programación I", "Programación II"]))
print("Cursos sugeridos con solo Prog I:", sistema.sugerir_cursos(["Programación I"]))