# Creamos un conjunto llamado 's'.
s = {1,2}
# Intentamos eliminar el elemento 3 del conjunto 's' usando el método remove().
# ERROR: KeyError: 3
# Este error ocurre porque el método remove() intenta eliminar un elemento específico del conjunto. Si el elemento especificado (en este caso, 3) no se encuentra en el conjunto, Python lanza un KeyError.
s.remove(3)
# Imprimimos el conjunto modificado (esta línea no se ejecuta debido al error anterior).
print(s)