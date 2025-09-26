# Recorrer las claves y valores del diccionario
diccionario = dict(
    nombre="Adrián",
    edad=20,
    ciudad="Bogotá",
    intereses=["Programación", "Tecnologia", "Desarrollo"]
)

for clave, item in diccionario.items():
    print(f"{clave}: {item}")  # Muestra clave y valor
