# Carrito de compras
carrito = []  # lista vacía donde guardamos los productos

while True:
    print("\n--- Carrito de compras ---")
    print("1) Agregar producto")
    print("2) Eliminar producto")
    print("3) Ver carrito")
    print("4) Salir")
    opcion = input("Elige una opción (1-4): ")

    if opcion == "1":
        producto = input("Nombre del producto a agregar: ").strip()
        if producto:                    # validamos que no sea cadena vacía
            carrito.append(producto)     # usamos .append() para agregar
            print(f"'{producto}' agregado al carrito.")
        else:
            print("No ingresaste un nombre válido.")
    elif opcion == "2":
        if not carrito:
            print("El carrito está vacío.")
        else:
            producto = input("Nombre del producto a eliminar: ").strip()
            if producto in carrito:     # validamos que el producto esté en la lista
                carrito.remove(producto) # usamos .remove() para quitar el primer match
                print(f"'{producto}' eliminado del carrito.")
            else:
                print(f"'{producto}' no está en el carrito.")
    elif opcion == "3":
        if carrito:
            print("Contenido del carrito:")
            for p in enumerate(carrito, 1):
                print(f"{p}")
        else:
            print("El carrito está vacío.")
    elif opcion == "4":
        print("Saliendo... ¡Gracias!")
        break
    else:
        print("Opción inválida. Elige 1, 2, 3 o 4.")