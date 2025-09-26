from pathlib import Path
p = Path("nuevo1.txt")
print(p.stem)     # Devuelve el nombre del archivo sin extensión -> "nuevo1"
print(p.suffix)   # Devuelve la extensión del archivo -> ".txt"
