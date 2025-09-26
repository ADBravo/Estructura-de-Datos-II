---
# 🐍 Python - Estructura de Datos II

Aquí encontrarás una colección de **ejercicios en Python**, cada uno con su código y explicación.
---

## ✨ Ejercicio 1 – Lista de frutas

```python
frutas = ["manzana", "banana", "naranja"]

print(frutas)

for fruta in frutas:
    print(fruta)
```

📘 **Explicación:**
Se define una lista de cadenas y se imprime tanto la lista completa como cada elemento con un bucle `for`.

---

## ✨ Ejercicio 2 – Tupla de frutas

```python
frutas = ("manzana", "banana", "naranja")

print(frutas)

for fruta in frutas:
    print(fruta)
```

📘 **Explicación:**
Se usa una **tupla** (inmutable) en lugar de una lista. El bucle `for` recorre cada fruta.

---

## ✨ Ejercicio 3 – Acceso por índice

```python
frutas = ["manzana", "banana", "naranja"]

print("0:", frutas[0])
print("1:", frutas[1])
print("2:", frutas[2])
```

📘 **Explicación:**
Se accede a cada elemento de la lista mediante su índice.

---

## ✨ Ejercicio 4 – Índices negativos

```python
frutas = ["manzana", "banana", "naranja", "pera", "limon"]

print("1:", frutas[-2])
```

📘 **Explicación:**
Se accede a los elementos desde el final usando índices negativos. `-2` corresponde a `"pera"`.

---

## ✨ Ejercicio 5 – Iteración con índices

```python
frutas = ["manzana", "banana", "naranja", "pera", "limon"]

for i in range(len(frutas)):
    print(frutas[i])
```

📘 **Explicación:**
Se usa `range(len(lista))` para recorrer la lista mediante sus índices.

---

## ✨ Ejercicio 6 – Iteración directa

```python
frutas = ["manzana", "banana", "naranja", "pera", "limon"]

for frutas in frutas:
    print(frutas)
```

📘 **Explicación:**
El bucle recorre directamente los elementos de la lista. (Nota: usar el mismo nombre `frutas` para lista y variable no es recomendable).

---

## ✨ Ejercicio 7 – Iteración con `while`

```python
edades = [20, 41, 6, 18, 23]
indice = 0

while indice < len(edades):
    print(edades[indice])
    indice += 2
```

📘 **Explicación:**
El bucle `while` imprime cada **2 elementos** de la lista de edades.

---

## ✨ Ejercicio 8 – Agregar elementos a la lista

```python
edades = [20, 41, 6, 18, 23]
edades.append(12)
edades.append(22)
edades.append("valery")

indice = 0
while indice < len(edades):
    print(edades[indice])
    indice += 1
```

📘 **Explicación:**
Se agregan elementos con `.append()` y luego se recorren todos con `while`.

---

## ✨ Ejercicio 9 – Concatenación de listas

```python
numeros = [3, 7, 9]
numeros = numeros + [10, 5, 3]
print(numeros)
```

📘 **Explicación:**
Se concatenan listas con el operador `+`.

---

## ✨ Ejercicio 10 – Eliminar elementos con `pop()`

```python
palabras = ["gato", "perro", "Raton", "pez", "iguana", "lagarto"]
palabras.pop(1)
palabras.pop(3)
palabras.pop(-1)
print(palabras)
```

📘 **Explicación:**
`pop(indice)` elimina elementos en posiciones específicas de la lista.

---

## ✨ Ejercicio 11 – Listas paralelas

```python
nombres = ["Daniel", "Alejandro", "jose"]
cedulas = ["123", "456", "789"]

nombres.pop(1)
cedulas.pop(1)

print(nombres)
print(cedulas)

for nombre in nombres:
    print(nombre)
    for cedula in cedulas:
        print(cedula)
```

📘 **Explicación:**
Se eliminan elementos de listas paralelas y se recorren en bucles anidados.

---

## ✨ Ejercicio 12 – Registro de personas

```python
nombres = []
identificacion = []
tamaño = 3

for i in range(tamaño):
    print(f"Ingrese los datos de la persona {i+1}")
    nombre = input("nombre: ")
    identificacion_input = input("identificacion: ")
    nombres.append(nombre)
    identificacion.append(identificacion_input)

for i in range(tamaño):
    print("nombres:", nombres[i])
    print("identificacion:", identificacion[i])
```

📘 **Explicación:**
Se piden datos al usuario y se almacenan en dos listas paralelas.

---

## ✨ Ejercicio 13 – Registro con dirección

```python
nombres = []
identificacion = []
direccion = []
tamaño = 3

for i in range(tamaño):
    print(f"Ingrese los datos de la persona {i+1}")
    nombre = input("nombre: ")
    identificacion_input = input("identificacion: ")
    direccion_input = input("direccion: ")
    nombres.append(nombre)
    identificacion.append(identificacion_input)
    direccion.append(direccion_input)

for i in range(tamaño):
    print("nombres:", nombres[i])
    print("identificacion:", identificacion[i])
    print("direccion:", direccion[i])
```

📘 **Explicación:**
Se extiende el ejercicio anterior para almacenar también la dirección de cada persona.

---

## ✨ Ejercicio 14 – Vector NumPy desde lista

```python
import numpy as np

lst = [10, 20, 30, 40, 50]
vctr = np.array(lst)

print("vector created from a list")
print(vctr)
```

📘 **Explicación:**
Se crea un array de NumPy a partir de una lista de enteros.

---

## ✨ Ejercicio 15 – Vector de frutas con NumPy

```python
import numpy as np

lst = ["manzana", "pera", "naranja", "banano", "limon"]
vctr = np.array(lst)

print("vector frutas")
print(vctr)
```

📘 **Explicación:**
Se crea un vector de cadenas con NumPy.

---

## ✨ Ejercicio 16 – Vector columna de números

```python
import numpy as np

numeros = [[2],
          [4],
          [6],
          [10]]
vctr = np.array(numeros)

print("vector numeros")
print(vctr)
```

📘 **Explicación:**
Una lista de listas se convierte en un **vector columna**.

---

## ✨ Ejercicio 17 – Vector columna de frutas

```python
import numpy as np

frutas = [["manzana"],
          ["pera"],
          ["naranja"]]
vctr = np.array(frutas)

print("vector frutas")
print(vctr)
```

📘 **Explicación:**
Igual al anterior, pero con cadenas.

---

## ✨ Ejercicio 18 – Suma de vectores

```python
import numpy as np

lista1 = [10, 20, 30, 40, 50]
lista2 = [1, 2, 3, 4, 5]

vctr1 = np.array(lista1)
vctr2 = np.array(lista2)

print("verctor lista 1")
print(vctr1)
print("verctor lista 2")
print(vctr2)

vctr_add = vctr1 + vctr2
print("vector suma")
print(vctr_add)
```

📘 **Explicación:**
Se suman dos vectores de igual tamaño, elemento por elemento.

---

## ✨ Ejercicio 19 – Error al sumar vectores de distinto tamaño

```python
import numpy as np

lista1 = [10, 20, 30, 40, 50]
lista2 = [1, 2, 3, 4, 5, 6, 7]

vctr1 = np.array(lista1)
vctr2 = np.array(lista2)

print("vector lista 1")
print(vctr1)
print("vector lista 2")
print(vctr2)

vctr_add = vctr1 + vctr2
print("vector suma")
print(vctr_add)
```

📘 **Explicación:**
La suma falla porque los vectores tienen longitudes diferentes (**broadcasting inválido**).

---

## ✨ Ejercicio 20 – Resta de vectores

```python
import numpy as np

lista1 = [10, 20, 30, 40, 50]
lista2 = [1, 2, 3, 4, 5]

vctr1 = np.array(lista1)
vctr2 = np.array(lista2)

print("vector lista 1")
print(vctr1)
print("vector lista 2")
print(vctr2)

vctr_add = vctr1 - vctr2
print("vector resta")
print(vctr_add)
```

📘 **Explicación:**
Se restan dos vectores elemento por elemento.

---

## ✨ Ejercicio 21 – Multiplicación y división de vectores

```python
import numpy as np

lista1 = [10, 20, 30, 40, 50]
lista2 = [1, 2, 3, 4, 5]

vctr1 = np.array(lista1)
vctr2 = np.array(lista2)

print("vector lista 1")
print(vctr1)
print("vector lista 2")
print(vctr2)

vctr_mult = vctr1 * vctr2
print("vector multiplicacion")
print(vctr_mult)

vctr_div = vctr1 / vctr2
print("vector division")
print(vctr_div)
```

📘 **Explicación:**
Multiplicación y división elemento por elemento entre vectores.

---

## ✨ Ejercicio 22 – Producto punto (dot product)

```python
import numpy as np

lista1 = [10, 20, 30, 40, 50]
lista2 = [1, 1, 1, 1, 1]

vctr1 = np.array(lista1)
vctr2 = np.array(lista2)

print("vector lista 1")
print(vctr1)
print("vector lista 2")
print(vctr2)

vctr_dot = vctr1.dot(vctr2)
print("vector producto punto")
print(vctr_dot)
```

📘 **Explicación:**
El producto punto suma las multiplicaciones de los elementos correspondientes.

---

## ✨ Ejercicio 23 – Producto punto con otro vector

```python
import numpy as np

lista1 = [10, 20, 30, 40, 50]
lista2 = [2, 2, 2, 2, 2]

vctr1 = np.array(lista1)
vctr2 = np.array(lista2)

print("vector lista 1")
print(vctr1)
print("vector lista 2")
print(vctr2)

vctr_dot = vctr1.dot(vctr2)
print("vector producto punto")
print(vctr_dot)
```

📘 **Explicación:**
El producto punto multiplica cada elemento por `2` y suma los resultados.

---

## ✨ Ejercicio 24 – Crear un conjunto con `set()`

```python
s = set([5, 4, 6, 8, 8, 1])
print(s)
print(type(s))
```

📘 **Explicación:**
Se crea un conjunto eliminando los duplicados (el `8` repetido). El orden no está garantizado.

---

## ✨ Ejercicio 25 – Crear un conjunto con llaves `{}`

```python
s = {5, 4, 6, 8, 8, 1}
print(s)
print(type(s))
```

📘 **Explicación:**
Se utiliza la sintaxis `{}` para crear el conjunto. Los duplicados también se eliminan.

---

## ✨ Ejercicio 26 – Intentar acceder a un índice

```python
s = set([5, 6, 7, 8])
# s[0]  # ❌ Error: los conjuntos no soportan índices
```

📘 **Explicación:**
Los conjuntos no permiten acceder por índice, ya que no mantienen un orden interno.

---

## ✨ Ejercicio 27 – Error por falta de coma

```python
# lista = ["peru, argentina"]
# s = set(["mexico", "españa" lista])  # ❌ Error de sintaxis
```

📘 **Explicación:**
Falta una coma entre `"españa"` y `lista`, por eso ocurre un `SyntaxError`.

---

## ✨ Ejercicio 28 – Agregar elementos a una lista

```python
lista = ["peru, argentina"]
lista.append("mexico")
lista.append("españa")
print(lista)
```

📘 **Explicación:**
Se usa `append()` para añadir nuevos elementos a la lista.

---

## ✨ Ejercicio 29 – Recorrer un conjunto con `for`

```python
s = set([5, 6, 7, 8])
for ss in s:
    print(ss)
```

📘 **Explicación:**
Se recorren los elementos de un conjunto. El orden de impresión puede variar.

---

## ✨ Ejercicio 30 – Uso incorrecto de nombres de variables

```python
set = [1, 2, 2, 3, 4]
print(len(s))
```

📘 **Explicación:**
Aquí `set` se usa como nombre de variable, lo cual es una mala práctica porque sobreescribe la función integrada `set()`.

---

## ✨ Ejercicio 31 – Conjunto con cadenas

```python
s = {"guitarra", "bajo"}
print("guitarra")
```

📘 **Explicación:**
Se imprime el string `"guitarra"`, no el contenido del conjunto.

---

## ✨ Ejercicio 32 – Unión de conjuntos

```python
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1 | s2)
```

📘 **Explicación:**
Se obtiene la unión de ambos conjuntos → `{1, 2, 3, 4, 5}`.

---

## ✨ Ejercicio 33 – Agregar elementos con `add()`

```python
l = {1, 2}
l.add(3)
print(l)
```

📘 **Explicación:**
El método `add()` añade un nuevo elemento al conjunto.

---

## ✨ Ejercicio 34 – Eliminar elementos con `remove()`

```python
s = {1, 2}
s.remove(2)
print(s)
```

📘 **Explicación:**
El método `remove()` elimina un elemento del conjunto. Si el elemento no existe, genera un `KeyError`.

---

## ✨ Ejercicio 35 – Eliminar elementos con `discard()`

```python
s = {1, 2}
s.discard(3)
print(s)
```

📘 **Explicación:**
`discard()` elimina un elemento si existe. Si no está, no ocurre error.

---

## ✨ Ejercicio 36 – Eliminar un elemento aleatorio con `pop()`

```python
s = {1, 2}
s.pop()
print(s)
```

📘 **Explicación:**
El método `pop()` elimina un elemento aleatorio del conjunto.

---

## ✨ Ejercicio 37 – Vaciar un conjunto con `clear()`

```python
s = {1, 2}
s.clear()
print(s)
```

📘 **Explicación:**
El método `clear()` elimina todos los elementos, dejando un conjunto vacío.

---

## ✨ Ejercicio 38 – Caso práctico: Habilidades de equipos

```python
habilidades_frontend = {'HTML', 'CSS', 'JavaScript', 'React'}
habilidades_backend = {'Python', 'SQL', 'JavaScript', 'Django'}

print("Habilidades iniciales Frontend:", habilidades_frontend)
print("Habilidades iniciales Backend:", habilidades_backend)

habilidades_frontend.add('Vue.js')
habilidades_backend.remove('Django')

print("Habilidades actualizadas Frontend:", habilidades_frontend)
print("Habilidades actualizadas Backend:", habilidades_backend)

habilidades_totales = habilidades_frontend.union(habilidades_backend)
print("Total de habilidades:", habilidades_totales)

habilidades_comunes = habilidades_frontend.intersection(habilidades_backend)
print("Habilidades en común:", habilidades_comunes)

habilidades_solo_frontend = habilidades_frontend.difference(habilidades_backend)
print("Solo Frontend:", habilidades_solo_frontend)

habilidades_solo_backend = habilidades_backend.difference(habilidades_frontend)
print("Solo Backend:", habilidades_solo_backend)
```

📘 **Explicación:**
Se gestionan las habilidades de dos equipos (frontend y backend) usando operaciones con conjuntos como unión, intersección y diferencia.

---

## ✨ Ejercicio 39 – Crear carpeta con `os.mkdir()`

```python
import os
os.mkdir("nueva_carpeta")
print(os.listdir("."))
```

📘 **Explicación:**
Se crea una nueva carpeta llamada `nueva_carpeta` en el directorio actual y se listan sus contenidos.

---

## ✨ Ejercicio 40 – Crear carpeta con `Path.mkdir()`

```python
from pathlib import Path
Path("nueva_carpeta1").mkdir()
print(list(Path(".").iterdir()))
```

📘 **Explicación:**
Se crea una nueva carpeta usando `pathlib` y luego se listan los elementos del directorio actual.

---

## ✨ Ejercicio 41 – Obtener ruta actual con `os.getcwd()`

```python
import os
print(os.getcwd())
```

📘 **Explicación:**
Muestra la ruta absoluta del directorio de trabajo actual.

---

## ✨ Ejercicio 42 – Obtener ruta actual con `Path.cwd()`

```python
from pathlib import Path
print(Path.cwd())
```

📘 **Explicación:**
Devuelve el directorio de trabajo actual con `pathlib`.

---

## ✨ Ejercicio 43 – Listar archivos con `os.listdir()`

```python
import os
print(os.listdir('.'))
```

📘 **Explicación:**
Muestra una lista de los archivos y carpetas en el directorio actual.

---

## ✨ Ejercicio 44 – Listar archivos con `Path.iterdir()`

```python
from pathlib import Path
for f in Path('.').iterdir():
    print(f)
```

📘 **Explicación:**
Recorre e imprime todos los elementos del directorio actual.

---

## ✨ Ejercicio 45 – Crear archivo con `open()`

```python
import os
with open("nuevo.txt", "w") as f:
    f.write("Hola mundo")
```

📘 **Explicación:**
Crea un archivo `nuevo.txt` y escribe el texto `"Hola mundo"`.

---

## ✨ Ejercicio 46 – Crear archivo con `Path.write_text()`

```python
from pathlib import Path
Path("nuevo1txt").write_text("Hola mundo")
```

📘 **Explicación:**
Crea un archivo y escribe texto directamente usando `pathlib`.

---

## ✨ Ejercicio 47 – Verificar existencia con `os.path.exists()`

```python
import os
print(os.path.exists("nuevo.txt"))
print(os.path.exists("archivo.txt"))
```

📘 **Explicación:**
Comprueba si existen los archivos `nuevo.txt` y `archivo.txt`.

---

## ✨ Ejercicio 48 – Verificar existencia con `Path.exists()`

```python
from pathlib import Path
print(Path("archivo.txt").exists())
print(Path("nuevo.txt").exists())
```

📘 **Explicación:**
Verifica si existen los archivos utilizando `pathlib`.

---

## ✨ Ejercicio 49 – Eliminar archivo con `os.remove()`

```python
import os
os.remove("nuevo.txt")
```

📘 **Explicación:**
Elimina el archivo `nuevo.txt`.

---

## ✨ Ejercicio 50 – Eliminar archivo con `Path.unlink()`

```python
from pathlib import Path
Path("nuevo1.txt").unlink()
```

📘 **Explicación:**
Elimina un archivo usando `pathlib`.

---

## ✨ Ejercicio 51 – Eliminar carpeta vacía con `os.rmdir()`

```python
import os
os.rmdir("nueva_carpeta")
```

📘 **Explicación:**
Elimina la carpeta `nueva_carpeta`, siempre que esté vacía.

---

## ✨ Ejercicio 52 – Eliminar carpeta vacía con `Path.rmdir()`

```python
from pathlib import Path
Path("nueva_carpeta1").rmdir()
```

📘 **Explicación:**
Elimina una carpeta vacía usando `pathlib`.

---

## ✨ Ejercicio 53 – Renombrar archivo con `os.rename()`

```python
import os
os.rename("nuevo.txt", "renombrado.txt")
```

📘 **Explicación:**
Cambia el nombre del archivo `nuevo.txt` a `renombrado.txt`.

---

## ✨ Ejercicio 54 – Renombrar archivo con `Path.rename()`

```python
from pathlib import Path
Path("nuevo1.txt").rename("renombrado1.txt")
```

📘 **Explicación:**
Renombra el archivo con `pathlib`.

---

## ✨ Ejercicio 55 – Leer archivo con `open()`

```python
import os
with open("nuevo.txt", "r") as f:
    print(f.read())
```

📘 **Explicación:**
Abre y lee el contenido del archivo `nuevo.txt`.

---

## ✨ Ejercicio 56 – Leer archivo con `Path.read_text()`

```python
from pathlib import Path
print(Path("nuevo1.txt").read_text())
```

📘 **Explicación:**
Lee el contenido de un archivo usando `pathlib`.

---

## ✨ Ejercicio 57 – Escribir archivo con `open()`

```python
import os
with open("nuevo.txt", "w") as f:
    f.write("hello world")
```

📘 **Explicación:**
Escribe el texto `"hello world"` en el archivo `nuevo.txt`.

---

## ✨ Ejercicio 58 – Escribir archivo con `Path.write_text()`

```python
from pathlib import Path
Path("nuevo1.txt").write_text("Darian")
```

📘 **Explicación:**
Escribe el texto `"Darian"` en el archivo usando `pathlib`.

---

## ✨ Ejercicio 59 – Obtener ruta absoluta con `os.path.abspath()`

```python
import os
print(os.path.abspath("nuevo.txt"))
```

📘 **Explicación:**
Muestra la ruta absoluta del archivo `nuevo.txt`.

---

## ✨ Ejercicio 60 – Obtener ruta absoluta con `Path.absolute()`

```python
from pathlib import Path
print(Path("nuevo1.txt").absolute())
```

📘 **Explicación:**
Muestra la ruta absoluta del archivo usando `pathlib`.

---

## ✨ Ejercicio 61 – Obtener nombre y extensión con `os.path.splitext()`

```python
import os
print(os.path.splitext("nuevo.txt"))
```

📘 **Explicación:**
Devuelve el nombre y la extensión del archivo en una tupla.

---

## ✨ Ejercicio 62 – Obtener nombre y extensión con `Path.stem` y `Path.suffix`

```python
from pathlib import Path
p = Path("nuevo1.txt")
print(p.stem)
print(p.suffix)
```

📘 **Explicación:**
Obtiene el nombre sin extensión (`stem`) y la extensión (`suffix`) de un archivo.

---

## ✨ Ejercicio 63 – Obtener solo nombre de archivo con `os.path.basename()`

```python
import os
print(os.path.basename("Users/NICOL/OneDrive/Desktop/directorios/Obtener solo el nombre del archivo o del directorio/nuevo.txt"))
```

📘 **Explicación:**
Devuelve únicamente el nombre del archivo desde una ruta completa.

---

## ✨ Ejercicio 64 – Obtener solo nombre de archivo con `Path.name`

```python
from pathlib import Path
p = Path("Users/NICOL/OneDrive/Desktop/directorios/Obtener solo el nombre del archivo o del directorio/nuevo1.txt")
print(p.name)
```

📘 **Explicación:**
Obtiene solo el nombre del archivo desde una ruta completa con `pathlib`.

---

## ✨ Ejercicio 65 – Crear subcarpetas con `os.makedirs()`

```python
import os
os.makedirs("carpeta1/carpeta2/carpeta3", exist_ok=True)
```

📘 **Explicación:**
Crea una estructura de carpetas anidadas.

---

## ✨ Ejercicio 66 – Crear subcarpetas con `Path.mkdir(parents=True)`

```python
from pathlib import Path
Path("carpeta1.0/carpeta2.0/carpeta3.0").mkdir(parents=True, exist_ok=True)
```

📘 **Explicación:**
Crea carpetas anidadas con `pathlib`.

---

## ✨ Ejercicio 67 – Eliminar carpeta con `shutil.rmtree()` y `os`

```python
import os
import shutil
shutil.rmtree("carpeta1")
```

📘 **Explicación:**
Elimina la carpeta `carpeta1` junto con todos sus archivos y subcarpetas.

---

## ✨ Ejercicio 68 – Eliminar carpeta con `shutil.rmtree()` y `Path`

```python
from pathlib import Path
import shutil
shutil.rmtree(Path("carpeta1.0"))
```

📘 **Explicación:**
Elimina una carpeta completa usando `pathlib`.

---

## ✨ Ejercicio 69 – Renombrar y mover carpetas con `os.rename()`

```python
import os
os.rename("carpeta1", "carpeta_renombrada")
os.rename("carpeta_renombrada", "otra_carpeta/carpeta_renombrada")
```

📘 **Explicación:**
Primero renombra una carpeta y luego la mueve dentro de otra.

---

## ✨ Ejercicio 70 – Renombrar y mover carpetas con `Path.rename()`

```python
from pathlib import Path
Path("carpeta1.0").rename("carpeta_renombrada1.0")
Path("carpeta_renombrada1.0").rename("otra_carpeta1/carpeta_renombrada1.0")
```

📘 **Explicación:**
Renombra y mueve una carpeta usando `pathlib`.

---

## ✨ Ejercicio 71 – Listar archivos de carpetas con `os.listdir()`

```python
import os
print(os.listdir("."))
print(os.listdir("carpeta1"))
```

📘 **Explicación:**
Lista archivos del directorio actual y de una carpeta específica.

---

## ✨ Ejercicio 72 – Listar archivos de carpetas con `Path.iterdir()`

```python
from pathlib import Path
print(list(Path(".").iterdir()))
print(list(Path("carpeta1.0").iterdir()))
```

📘 **Explicación:**
Lista archivos y carpetas usando `pathlib`.

---

## ✨ Ejercicio 73 – Crear un diccionario básico

```python
diccionario = {
    "nombre": "Juan",
    "edad": 28,
    "ciudad": "Madrid",
    "intereses": ["fútbol", "cine", "música"]
}

print(diccionario)
```

📘 **Explicación:**
Se crea un diccionario con claves y valores de distintos tipos: cadenas, enteros y listas.

---

## ✨ Ejercicio 74 – Crear un diccionario con `dict()`

```python
diccionario = dict(
    nombre="Adrián",
    edad=20,
    ciudad="Bogotá",
    intereses=["Programación", "Tecnologia", "Desarrollo"]
)

print(diccionario)
```

📘 **Explicación:**
Se utiliza la función `dict()` para crear un diccionario.

---

## ✨ Ejercicio 75 – Acceder a elementos del diccionario

```python
diccionario = dict(
    nombre="Adrián",
    edad=20,
    ciudad="Bogotá",
    intereses=["Programación", "Tecnologia", "Desarrollo"]
)

print(diccionario["nombre"])
print(diccionario.get("nombre"))

print(diccionario["edad"])
print(diccionario.get("edad"))
```

📘 **Explicación:**
Se accede a los valores usando tanto `[]` como el método `get()`.

---

## ✨ Ejercicio 76 – Modificar valores en el diccionario

```python
diccionario = dict(
    nombre="Adrián",
    edad=20,
    ciudad="Bogotá",
    intereses=["Programación", "Tecnologia", "Desarrollo"]
)

diccionario["nombre"] = "Andres"
print(diccionario)
```

📘 **Explicación:**
Se cambia el valor asociado a la clave `"nombre"`.

---

## ✨ Ejercicio 77 – Agregar una nueva clave al diccionario

```python
diccionario = dict(
    nombre="Adrián",
    edad=20,
    ciudad="Bogotá",
    intereses=["Programación", "Tecnologia", "Desarrollo"]
)

diccionario["dirección"] = "calle 123"
print(diccionario)
```

📘 **Explicación:**
Se añade una nueva clave `"dirección"` al diccionario.

---

## ✨ Ejercicio 78 – Recorrer solo las claves

```python
diccionario = dict(
    nombre="Adrián",
    edad=20,
    ciudad="Bogotá",
    intereses=["Programación", "Tecnologia", "Desarrollo"]
)

for clave in diccionario:
    print(f"{clave}")
```

📘 **Explicación:**
Un bucle `for` recorre únicamente las claves del diccionario.

---

## ✨ Ejercicio 79 – Recorrer solo los valores

```python
diccionario = dict(
    nombre="Adrián",
    edad=20,
    ciudad="Bogotá",
    intereses=["Programación", "Tecnologia", "Desarrollo"]
)

for item in diccionario.values():
    print(f"{item}")
```

📘 **Explicación:**
Se recorren únicamente los valores del diccionario con `values()`.

---

## ✨ Ejercicio 80 – Recorrer claves y valores

```python
diccionario = dict(
    nombre="Adrián",
    edad=20,
    ciudad="Bogotá",
    intereses=["Programación", "Tecnologia", "Desarrollo"]
)

for clave, item in diccionario.items():
    print(f"{clave}: {item}")
```

📘 **Explicación:**
Se recorren claves y valores con el método `items()`.

---

## ✨ Ejercicio 81 – Diccionarios anidados

```python
diccionario_anidado = dict(
    persona1=dict(
        nombre="Juan",
        edad=28,
        ciudad="Madrid"
    ),
    persona2=dict(
        nombre="Ana",
        edad=34,
        ciudad="Barcelona"
    )
)

print(diccionario_anidado["persona1"])
print(diccionario_anidado["persona2"])
```

📘 **Explicación:**
Un diccionario puede contener otros diccionarios dentro.

---

## ✨ Ejercicio 82 – Vaciar un diccionario

```python
mi_diccionario = {"a": 1, "b": 2, "c": 3}
mi_diccionario.clear()

print(mi_diccionario)
```

📘 **Explicación:**
El método `clear()` elimina todos los elementos del diccionario.

---

## ✨ Ejercicio 83 – Usar `get()` con valor por defecto

```python
mi_diccionario = {"a": 1, "b": 2, "c": 3}

print(mi_diccionario.get("b"))
print(mi_diccionario.get("d", "No encontrado"))
```

📘 **Explicación:**
`get()` permite acceder a valores y definir un valor predeterminado si la clave no existe.

---

## ✨ Ejercicio 84 – Recorrer un diccionario con `items()`

```python
mi_diccionario = {"a": 1, "b": 2, "c": 3}

for clave, valor in mi_diccionario.items():
    print(f"{clave}: {valor}")
```

📘 **Explicación:**
`items()` devuelve pares clave-valor para iterar.

---

## ✨ Ejercicio 85 – Convertir `items()` en lista

```python
mi_diccionario = {"a": 1, "b": 2, "c": 3}

items = list(mi_diccionario.items())
print(items)
```

📘 **Explicación:**
Los pares clave-valor se convierten en una lista de tuplas.

---

## ✨ Ejercicio 86 – Obtener todas las claves

```python
mi_diccionario = {"a": 1, "b": 2, "c": 3}

claves = mi_diccionario.keys()
print(claves)
print(list(claves))
```

📘 **Explicación:**
El método `keys()` devuelve todas las claves del diccionario.

---

## ✨ Ejercicio 87 – Obtener todos los valores

```python
mi_diccionario = {"a": 1, "b": 2, "c": 3}

valores = mi_diccionario.values()
print(valores)
print(list(valores))
```

📘 **Explicación:**
El método `values()` devuelve todos los valores del diccionario.

---

## ✨ Ejercicio 88 – Eliminar un elemento con `pop()`

```python
mi_diccionario = {"a": 1, "b": 2, "c": 3}

valor = mi_diccionario.pop("b")
print(valor)
print(mi_diccionario)
```

📘 **Explicación:**
`pop()` elimina una clave y devuelve su valor.

---

## ✨ Ejercicio 89 – Eliminar el último elemento con `popitem()`

```python
mi_diccionario = {"a": 1, "b": 2, "c": 3}

ultimo_item = mi_diccionario.popitem()
print(ultimo_item)
print(mi_diccionario)
```

📘 **Explicación:**
`popitem()` elimina y devuelve el último par clave-valor.

---

## ✨ Ejercicio 90 – Actualizar un diccionario con `update()`

```python
mi_diccionario = {"a": 1, "b": 2}
nuevo_diccionario = {"b": 3, "c": 4}

mi_diccionario.update(nuevo_diccionario)
print(mi_diccionario)
```

📘 **Explicación:**
`update()` actualiza los valores de claves existentes y añade nuevas claves.

---

## ✨ Ejercicio 91 – Crear una tupla

```python
t = (1, 2, 3)
print(t)
```

📘 **Explicación:**
Se crea una tupla con tres elementos y se imprime.

---

## ✨ Ejercicio 92 – Crear una tupla con `tuple()`

```python
t = tuple([1, 2, 3])
print(t)
```

📘 **Explicación:**
El constructor `tuple()` convierte una lista en tupla.

---

## ✨ Ejercicio 93 – Acceder a un elemento por índice

```python
t = (10, 20, 30, 40)
print(t[2])
```

📘 **Explicación:**
Los elementos de una tupla se acceden por índice, empezando desde 0.

---

## ✨ Ejercicio 94 – Desempaquetar una tupla

```python
t = (1, 2, 3)
a, b, c = t
print(a, b, c)
```

📘 **Explicación:**
Se pueden asignar los valores de una tupla a varias variables mediante desempaquetado.

---

## ✨ Ejercicio 95 – Verificar existencia de un valor

```python
t = (5, 10, 15, 20)
print(10 in t)
print(30 in t)
```

📘 **Explicación:**
El operador `in` permite comprobar si un valor está dentro de una tupla.

---

## ✨ Ejercicio 96 – Concatenar tuplas

```python
t1 = (1, 2)
t2 = (3, 4)
t3 = t1 + t2
print(t3)
```

📘 **Explicación:**
El operador `+` concatena tuplas.

---

## ✨ Ejercicio 97 – Repetir una tupla

```python
t = (1, 2)
print(t * 3)
```

📘 **Explicación:**
El operador `*` repite los elementos de una tupla varias veces.

---

## ✨ Ejercicio 98 – Contar elementos con `count()`

```python
t = (1, 2, 2, 3, 2)
print(t.count(2))
```

📘 **Explicación:**
El método `count()` devuelve cuántas veces aparece un valor en la tupla.

---

## ✨ Ejercicio 99 – Encontrar índice con `index()`

```python
t = (10, 20, 30, 40)
print(t.index(30))
```

📘 **Explicación:**
El método `index()` devuelve la posición de un elemento en la tupla.

---

## ✨ Ejercicio 100 – Longitud de una tupla

```python
t = (1, 2, 3, 4, 5)
print(len(t))
```

📘 **Explicación:**
La función `len()` devuelve el número de elementos en la tupla.

---

## ✨ Ejercicio 101 – Tupla anidada

```python
t = (1, (2, 3), (4, 5))
print(t[1][1])
```

📘 **Explicación:**
Se pueden tener tuplas dentro de tuplas y acceder a sus valores mediante índices.

---

## ✨ Ejercicio 102 – Convertir lista en tupla

```python
lista = [1, 2, 3]
t = tuple(lista)
print(t)
```

📘 **Explicación:**
El constructor `tuple()` convierte una lista en una tupla.

---

## ✨ Ejercicio 103 – Convertir tupla en lista

```python
t = (1, 2, 3)
lista = list(t)
print(lista)
```

📘 **Explicación:**
El constructor `list()` convierte una tupla en lista.

---

## ✨ Ejercicio 104 – Tupla con diferentes tipos de datos

```python
t = (1, "hola", 3.5, True)
print(t)
```

📘 **Explicación:**
Las tuplas pueden almacenar datos de distintos tipos.

---

## ✨ Ejercicio 105 – Iterar sobre una tupla

```python
t = ("a", "b", "c")
for i in t:
    print(i)
```

📘 **Explicación:**
Las tuplas se pueden recorrer con un bucle `for`.

---
