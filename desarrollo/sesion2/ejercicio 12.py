# Listas vacías para almacenar datos
nombres = []
identificacion = []
tamaño = 3  # Número de personas a registrar

# Bucle para pedir los datos de 3 personas
for i in range(tamaño):
    print(f"Ingrese los datos de la persona {i+1}")
    nombre = input("nombre: ")  # Pide el nombre
    identificacion_input = input("identificacion: ")  # Pide la identificación
    # Guardamos en listas
    nombres.append(nombre)
    identificacion.append(identificacion_input)

# Recorremos y mostramos los datos ingresados
for i in range(tamaño):
    print("nombres:", nombres[i])
    print("identificacion:", identificacion[i])