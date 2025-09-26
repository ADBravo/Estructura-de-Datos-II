import os
with open("nuevo.txt", "w") as f:   # Abre (o crea) el archivo "nuevo.txt" en modo escritura
    f.write("hello world")          # Escribe "hello world" en el archivo (borra el contenido anterior si lo había)
