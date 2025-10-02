# Registro de usuarios con roles (almacenamos (nombre, rol) como tuplas)
roles_validos = ("admin", "editor", "visitante")  # Tupla fija de roles permitidos
usuarios = []  # Lista donde guardaremos tuplas con la forma (nombre, rol)

while True:
    print("\n--- Registro de usuarios ---")
    nombre = input("Nombre de usuario (o 'salir' para terminar): ").strip()
    
    if nombre:
        # .strip() elimina espacios extra al inicio/final
        # .lower() convierte a minúsculas → así "SALIR", "salir", "Salir" se interpretan igual
        if nombre.lower() == "salir":
            break  # rompemos el ciclo y terminamos el programa

        # Mostramos roles válidos usando .join() para unirlos con comas
        rol = input(f"Rol ({', '.join(roles_validos)}): ").strip().lower()

        # Validamos que el rol ingresado exista dentro de roles_validos
        if rol in roles_validos:              
            usuarios.append((nombre, rol))    # Guardamos una tupla inmutable (nombre, rol)
            print(f"Usuario '{nombre}' registrado con rol '{rol}'.")
        else:
            print(f"Rol inválido. Los roles válidos son: {', '.join(roles_validos)}")

    else:
        print("No ingresaste un nombre válido.")
        
# Mostramos la lista de usuarios registrados
print("\nUsuarios registrados:")

# enumerate devuelve pares (indice, elemento) → aquí (i, (nombre, rol))
# Ejemplo: (1, ("Carlos", "admin"))
# El for hace doble desempaquetado:
#   i = índice de usuario (1, 2, 3, …)
#   (n, r) = la tupla (nombre, rol) → n=nombre, r=rol
for i in enumerate(usuarios, 1):
    print(i)
