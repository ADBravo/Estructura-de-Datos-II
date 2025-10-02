# Sistema de votación por color
colores = {"rojo": 0, "azul": 0, "verde": 0, "amarillo": 0}  
# Diccionario: cada clave es un color y su valor es el número de votos (inicia en 0).

while True:
    print("\nColores disponibles para votar:")
    for c in colores:  
        # Al recorrer un diccionario directamente, 'c' toma solo las claves (los nombres de colores).
        print(c)
    
    voto = input("Escribe el color por el que quieres votar (o 'salir'): ").strip().lower()
    # .strip() elimina espacios al inicio/final y .lower() convierte todo a minúsculas
    # → Esto hace más flexible la comparación (ej: "Rojo " → "rojo").

    if voto == "salir":
        break  # Salimos del bucle si el usuario ya no quiere votar.

    if voto in colores:            # Comprobamos si el color escrito existe en el diccionario.
        colores[voto] += 1         # Accedemos al valor de la clave y sumamos 1 voto.
        print(f"Voto registrado para '{voto}'.")
    else:
        print("Opción inválida, elige uno de los colores mostrados.")

print("\nResultado final de la votación:")
for color, votos in colores.items():  
    # .items() devuelve pares (clave, valor), aquí color=clave y votos=valor.
    print(f"{color}: {votos} votos")
