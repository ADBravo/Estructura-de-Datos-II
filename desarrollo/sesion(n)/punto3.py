# Agenda de contactos (clave: nombre, valor: teléfono)
agenda = {}  # Diccionario vacío donde cada clave será el nombre y el valor el teléfono

while True:
    print("\n--- Agenda de contactos ---")
    print("1) Agregar/actualizar contacto")
    print("2) Buscar teléfono por nombre")
    print("3) Mostrar todos los contactos")
    print("4) Salir")
    opcion = input("Elige una opción (1-4): ")

    if opcion == "1":
        nombre = input("Nombre: ").strip()
        telefono = input("Teléfono: ").strip()
        if nombre and telefono:  
            # Validamos que no sean cadenas vacías ("" es False en Python)
            
            # .update({clave: valor}) → si la clave no existe, la agrega;
            # si ya existe, actualiza el valor
            agenda.update({nombre: telefono})
            print(f"Contacto '{nombre}' guardado/actualizado.")
        else:
            print("Nombre o teléfono no válidos.")

    elif opcion == "2":
        nombre = input("Nombre a buscar: ").strip()
        
        # (clave: valor → nombre: teléfono).
        # Si la clave NO existe, devuelve None en lugar de dar error
        telefono = agenda.get(nombre)
        
        if telefono:  # Si existe el valor
            print(f"Teléfono de {nombre}: {telefono}")
        else:
            print(f"No se encontró el contacto '{nombre}'.")

    elif opcion == "3":
        if agenda:  # Un diccionario vacío se evalúa como False
            print("Contactos guardados:")
            
            # .items() devuelve pares (clave, valor) del diccionario
            # Ejemplo: ("Carlos", "12345")
            for i in agenda.items():
                print(i)
        else:
            print("La agenda está vacía.")

    elif opcion == "4":
        print("Saliendo de la agenda.")
        break  # Termina el bucle while True

    else:
        print("Opción inválida.")
