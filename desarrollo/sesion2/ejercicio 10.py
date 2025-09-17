# Lista de palabras
palabras = ["gato", "perro", "Raton", "pez", "iguana", "lagarto"]

# Eliminamos elementos por posición
palabras.pop(1)  # Elimina "perro"
palabras.pop(3)  # Elimina "iguana" (posición cambia después del primer pop)
palabras.pop(-1) # Elimina el último ("lagarto")

print(palabras)  # Muestra lista restante