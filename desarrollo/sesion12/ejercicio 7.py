# Recorrer solo los valores del diccionario
diccionario = dict(
    nombre="Adrián",
    edad=20,
    ciudad="Bogotá",
    intereses=["Programación", "Tecnologia", "Desarrollo"]
)

for item in diccionario.values():
    print(f"{item}")  # Muestra solo los valores
