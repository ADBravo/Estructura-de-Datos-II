from pathlib import Path

# Listar todo lo que hay en la carpeta actual
print(list(Path(".").iterdir()))

# Listar lo que hay en una carpeta específica
print(list(Path("carpeta1.0").iterdir()))
