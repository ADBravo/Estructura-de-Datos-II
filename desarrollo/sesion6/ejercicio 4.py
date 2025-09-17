# Definimos una lista llamada 'lista'.
lista = ["peru, argentina"]

# Intentamos crear un conjunto 's' a partir de una lista que contiene la variable 'lista' sin una coma.
# ERROR: SyntaxError: invalid syntax. Perhaps you forgot a comma?
# Este error de sintaxis ocurre porque al intentar pasar "mexico", "españa" y la variable 'lista' dentro de los corchetes para crear una lista para el conjunto, falta una coma entre "españa" y 'lista'.
s = set(["mexico","españa" lista])