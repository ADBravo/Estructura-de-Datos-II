from collections import deque

class RedSocial:
    def __init__(self):
        # Diccionario {usuario: [amigos]}
        self.red = {}

    def agregar_usuario(self, usuario):
        if usuario not in self.red:
            self.red[usuario] = []

    def conectar(self, u1, u2):
        self.red[u1].append(u2)
        self.red[u2].append(u1)

    def propagar_info(self, inicio, niveles):
        visitados = {inicio}
        cola = deque([(inicio, 0)])
        resultado = {0: [inicio]}

        while cola:
            usuario, nivel = cola.popleft()
            if nivel < niveles:
                for amigo in self.red[usuario]:
                    if amigo not in visitados:
                        visitados.add(amigo)
                        cola.append((amigo, nivel + 1))
                        resultado.setdefault(nivel + 1, []).append(amigo)
        return resultado

    def alcance_total(self, inicio, niveles):
        resultado = self.propagar_info(inicio, niveles)
        return sum(len(lista) for lista in resultado.values())

    def usuario_mayor_alcance(self, niveles):
        return max(self.red, key=lambda u: self.alcance_total(u, niveles))


# Ejemplo
red = RedSocial()
for u in ["A", "B", "C", "D", "E"]:
    red.agregar_usuario(u)

red.conectar("A", "B")
red.conectar("A", "C")
red.conectar("B", "D")
red.conectar("C", "E")

print("Propagación desde A en 2 niveles:", red.propagar_info("A", 2))
print("Alcance total desde A en 2 niveles:", red.alcance_total("A", 2))
print("Usuario con mayor alcance en 2 niveles:", red.usuario_mayor_alcance(2))