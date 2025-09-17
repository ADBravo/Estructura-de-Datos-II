
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
