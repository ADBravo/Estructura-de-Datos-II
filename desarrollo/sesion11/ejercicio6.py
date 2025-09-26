from pathlib import Path
for f in Path('.').iterdir():   # Itera sobre cada archivo y carpeta en el directorio actual
    print(f)                    # Imprime la ruta completa de cada archivo/carpeta
