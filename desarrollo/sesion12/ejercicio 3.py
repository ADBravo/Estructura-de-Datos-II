# Acceder a elementos de un diccionario con [] y con get()
diccionario = dict(
    nombre="Adrián",
    edad=20,
    ciudad="Bogotá",
    intereses=["Programación", "Tecnologia", "Desarrollo"]
)

print(diccionario["nombre"])  # Accede directamente a la clave
print(diccionario.get("nombre"))  # Accede usando get()

print(diccionario["edad"])  # Acceso directo a la clave "edad"
print(diccionario.get("edad"))  # Acceso con get()
