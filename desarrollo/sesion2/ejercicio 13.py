# Listas vacías para almacenar más datos
nombres = []
identificacion = []
direccion = []
tamaño = 3  # Número de personas a registrar

# Pedimos nombre, identificación y dirección
for i in range(tamaño):
    print(f"Ingrese los datos de la persona {i+1}")
    nombre = input("nombre: ")
    identificacion_input = input("identificacion: ")
    direccion_input = input("direccion: ")
    # Guardamos en listas
    nombres.append(nombre)
    identificacion.append(identificacion_input)
    direccion.append(direccion_input)

# Mostramos la información almacenada
for i in range(tamaño):
    print("nombres:", nombres[i])
    print("identificacion:", identificacion[i])
    print("direccion:", direccion[i])