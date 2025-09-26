import os

# Renombrar carpeta
os.rename("carpeta1", "carpeta_renombrada")  

# Mover carpeta (la coloca dentro de "otra_carpeta")
os.rename("carpeta_renombrada", "otra_carpeta/carpeta_renombrada")
