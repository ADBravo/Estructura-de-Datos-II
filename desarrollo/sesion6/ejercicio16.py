# 1. Inicialización: Crea dos conjuntos (sets) para representar las habilidades iniciales de cada equipo:
habilidades_frontend = {'HTML', 'CSS', 'JavaScript', 'React'}
habilidades_backend = {'Python', 'SQL', 'JavaScript', 'Django'}

print("Habilidades iniciales del equipo de Frontend:", habilidades_frontend)
print("Habilidades iniciales del equipo de Backend:", habilidades_backend)
print("-" * 30) # Separador para mejor legibilidad

# 2. Actualización de Equipos:
# Un nuevo desarrollador se une al equipo de Frontend con la habilidad de 'Vue.js'.
habilidades_frontend.add('Vue.js')
# Para este proyecto, el equipo de Backend no usará Django. Elimina la habilidad 'Django'.
habilidades_backend.remove('Django')

print("Habilidades actualizadas del equipo de Frontend:", habilidades_frontend)
print("Habilidades actualizadas del equipo de Backend:", habilidades_backend)
print("-" * 30) # Separador para mejor legibilidad

# 3. Análisis de Habilidades:
# Calcula y muestra el conjunto total de habilidades únicas disponibles en la empresa (la unión de ambos equipos).
habilidades_totales = habilidades_frontend.union(habilidades_backend)
print("Conjunto total de habilidades únicas:", habilidades_totales)

# Identifica y muestra las habilidades que ambos equipos tienen en común (la intersección).
habilidades_comunes = habilidades_frontend.intersection(habilidades_backend)
print("Habilidades en común:", habilidades_comunes)

# Determina y muestra las habilidades que son exclusivas del equipo de Frontend (la diferencia).
habilidades_solo_frontend = habilidades_frontend.difference(habilidades_backend)
print("Habilidades exclusivas de Frontend:", habilidades_solo_frontend)

# Opcional: Habilidades exclusivas de Backend
habilidades_solo_backend = habilidades_backend.difference(habilidades_frontend)
print("Habilidades exclusivas de Backend:", habilidades_solo_backend)