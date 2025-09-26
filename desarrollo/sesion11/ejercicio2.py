from pathlib import Path
Path("nueva_carpeta1").mkdir()      # Crea una carpeta llamada "nueva_carpeta1"
print(list(Path(".").iterdir()))    # Lista los elementos (archivos/carpetas) en el directorio actual
