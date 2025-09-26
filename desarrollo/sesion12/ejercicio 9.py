# Crear un diccionario anidado
diccionario_anidado = dict(
    persona1=dict(
        nombre="Juan",
        edad=28,
        ciudad="Madrid"
    ),
    persona2=dict(
        nombre="Ana",
        edad=34,
        ciudad="Barcelona"
    )
)

print(diccionario_anidado["persona1"])  # Accede al diccionario de persona1
print(diccionario_anidado["persona2"])  # Accede al diccionario de persona2
