# Creamos un conjunto llamado 's' a partir de una lista.
s = set([5,6,7,8])

# Intentamos acceder a un elemento del conjunto usando un índice (s[0]).
# ERROR: TypeError: 'set' object does not support item assignment
# Este error ocurre porque los conjuntos en Python son colecciones desordenadas y no soportan indexación (acceso por posición) ni slicing. No se puede acceder a un elemento de un conjunto usando un índice numérico como en las listas o tuplas.
s [0]