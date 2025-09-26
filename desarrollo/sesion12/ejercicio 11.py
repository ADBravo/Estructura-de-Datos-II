# Usar get() con claves existentes y no existentes
mi_diccionario = {"a": 1, "b": 2, "c": 3}

print(mi_diccionario.get("b"))  # Devuelve el valor asociado a "b"
print(mi_diccionario.get("d", "No encontrado"))  # Si no existe, devuelve valor por defecto
