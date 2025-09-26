from pathlib import Path

# Renombrar carpeta
Path("carpeta1.0").rename("carpeta_renombrada1.0")

# Mover carpeta (la coloca dentro de "otra_carpeta1")
Path("carpeta_renombrada1.0").rename("otra_carpeta1/carpeta_renombrada1.0")
