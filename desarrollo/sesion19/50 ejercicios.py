
# Ejercicios de Estructuras de Datos - Versión corregida
# Se han comentado las descripciones y números de cada ejercicio para evitar errores sintácticos.
# Cada ejercicio incluye el enunciado como comentario seguido del código correspondiente.

# ------------------------------------
# PILAS (10 ejercicios)
# ------------------------------------

# 1. Balanceo de paréntesis
# Enunciado: Implementa una función que verifique si los paréntesis, corchetes y llaves en una expresión están correctamente balanceados.
def balanceo_parentesis(expresion):
    pila = []
    parejas = {')': '(', ']': '[', '}': '{'}
    for caracter in expresion:
        if caracter in '([{':
            pila.append(caracter)
        elif caracter in ')]}':
            if not pila or pila[-1] != parejas[caracter]:
                return False
            pila.pop()
    return len(pila) == 0


# 2. Conversión infijo a postfijo
# Enunciado: Convierte una expresión matemática infija a notación postfija.
def infijo_a_postfijo(expresion):
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    pila = []
    salida = []
    for token in expresion.split():
        if token.isalnum():
            salida.append(token)
        elif token == '(':
            pila.append(token)
        elif token == ')':
            while pila and pila[-1] != '(':
                salida.append(pila.pop())
            if pila:
                pila.pop()
        else:
            while (pila and pila[-1] != '(' and
                   precedencia.get(token, 0) <= precedencia.get(pila[-1], 0)):
                salida.append(pila.pop())
            pila.append(token)
    while pila:
        salida.append(pila.pop())
    return ' '.join(salida)


# 3. Evaluar expresión postfija
# Enunciado: Evalúa una expresión matemática en notación postfija.
def evaluar_postfijo(expresion):
    pila = []
    for token in expresion.split():
        if token.lstrip('-').isdigit():
            pila.append(int(token))
        else:
            b = pila.pop()
            a = pila.pop()
            if token == '+':
                pila.append(a + b)
            elif token == '-':
                pila.append(a - b)
            elif token == '*':
                pila.append(a * b)
            elif token == '/':
                pila.append(a / b)
            elif token == '^':
                pila.append(a ** b)
    return pila[0] if pila else None


# 4. Invertir una lista usando pila
# Enunciado: Invierte una lista usando operaciones de pila.
def invertir_lista_pila(lista):
    pila = []
    for elemento in lista:
        pila.append(elemento)
    lista_invertida = []
    while pila:
        lista_invertida.append(pila.pop())
    return lista_invertida


# 5. Eliminar elementos consecutivos duplicados
# Enunciado: Elimina elementos duplicados consecutivos usando una pila.
def eliminar_consecutivos_duplicados(lista):
    pila = []
    for elemento in lista:
        if not pila or pila[-1] != elemento:
            pila.append(elemento)
    return pila


# 6. Siguiente elemento mayor
# Enunciado: Para cada elemento, encuentra el primer elemento mayor a su derecha.
def siguiente_elemento_mayor(lista):
    pila = []
    resultado = [-1] * len(lista)
    for i in range(len(lista)):
        while pila and lista[pila[-1]] < lista[i]:
            idx = pila.pop()
            resultado[idx] = lista[i]
        pila.append(i)
    return resultado


# 7. Validar secuencia de push/pop
# Enunciado: Verifica si una secuencia es válida para operaciones push/pop.
def validar_secuencia_push_pop(push_seq, pop_seq):
    pila = []
    i = 0
    for num in push_seq:
        pila.append(num)
        while pila and i < len(pop_seq) and pila[-1] == pop_seq[i]:
            pila.pop()
            i += 1
    return not pila and i == len(pop_seq)


# 8. Pila con mínimo en O(1)
# Enunciado: Implementa una pila que devuelva el mínimo en tiempo constante.
class PilaConMinimo:
    def __init__(self):
        self.pila_principal = []
        self.pila_minimos = []

    def push(self, valor):
        self.pila_principal.append(valor)
        if not self.pila_minimos or valor <= self.pila_minimos[-1]:
            self.pila_minimos.append(valor)

    def pop(self):
        if not self.pila_principal:
            return None
        valor = self.pila_principal.pop()
        if self.pila_minimos and valor == self.pila_minimos[-1]:
            self.pila_minimos.pop()
        return valor

    def min(self):
        return self.pila_minimos[-1] if self.pila_minimos else None


# 9. Dos pilas en un array
# Enunciado: Implementa dos pilas usando un solo array.
class DosPilas:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.array = [None] * capacidad
        self.top1 = -1
        self.top2 = capacidad

    def push1(self, valor):
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.array[self.top1] = valor
        else:
            raise IndexError("Pila 1 llena")

    def push2(self, valor):
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.array[self.top2] = valor
        else:
            raise IndexError("Pila 2 llena")

    def pop1(self):
        if self.top1 >= 0:
            valor = self.array[self.top1]
            self.top1 -= 1
            return valor
        return None

    def pop2(self):
        if self.top2 < self.capacidad:
            valor = self.array[self.top2]
            self.top2 += 1
            return valor
        return None


# 10. Ordenar pila
# Enunciado: Ordena una pila usando solo operaciones de pila.
def ordenar_pila(pila):
    pila_temp = []
    while pila:
        temp = pila.pop()
        while pila_temp and pila_temp[-1] > temp:
            pila.append(pila_temp.pop())
        pila_temp.append(temp)
    return pila_temp


# ------------------------------------
# COLAS (10 ejercicios)
# ------------------------------------

# 11. Implementar cola usando pilas
# Enunciado: Implementa una cola usando dos pilas.
class ColaConPilas:
    def __init__(self):
        self.entrada = []
        self.salida = []

    def enqueue(self, valor):
        self.entrada.append(valor)

    def dequeue(self):
        if not self.salida:
            while self.entrada:
                self.salida.append(self.entrada.pop())
        return self.salida.pop() if self.salida else None

    def front(self):
        if not self.salida:
            while self.entrada:
                self.salida.append(self.entrada.pop())
        return self.salida[-1] if self.salida else None


# 12. Cola circular
# Enunciado: Implementa una cola circular con array de tamaño fijo.
class ColaCircular:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.cola = [None] * capacidad
        self.frente = 0
        self.final = -1
        self.tamano = 0

    def enqueue(self, valor):
        if self.tamano == self.capacidad:
            return False
        self.final = (self.final + 1) % self.capacidad
        self.cola[self.final] = valor
        self.tamano += 1
        return True

    def dequeue(self):
        if self.tamano == 0:
            return None
        valor = self.cola[self.frente]
        self.frente = (self.frente + 1) % self.capacidad
        self.tamano -= 1
        return valor

    def front(self):
        return self.cola[self.frente] if self.tamano > 0 else None


# 13. Revertir primeros k elementos
# Enunciado: Invierte los primeros k elementos de una cola.
# Usaremos una cola simple basada en lista para las pruebas.
class ColaSimple:
    def __init__(self):
        self.elementos = []

    def enqueue(self, valor):
        self.elementos.append(valor)

    def dequeue(self):
        return self.elementos.pop(0) if self.elementos else None

    def __len__(self):
        return len(self.elementos)

    def __iter__(self):
        return iter(self.elementos)


def revertir_primeros_k(cola, k):
    pila = []
    # Sacar primeros k elementos a la pila
    for _ in range(min(k, len(cola))):
        pila.append(cola.dequeue())
    # Devolver de la pila a la cola (invertidos)
    while pila:
        cola.enqueue(pila.pop())
    # Mover los elementos restantes al final
    restantes = len(cola) - k if len(cola) > k else 0
    for _ in range(restantes):
        cola.enqueue(cola.dequeue())
    return cola


# 14. Generar números binarios
# Enunciado: Genera los primeros n números binarios usando una cola.
def generar_numeros_binarios(n):
    if n <= 0:
        return []
    resultado = []
    cola = ["1"]
    for _ in range(n):
        actual = cola.pop(0)
        resultado.append(actual)
        cola.append(actual + "0")
        cola.append(actual + "1")
    return resultado


# 15. Cola de prioridad simple
# Enunciado: Implementa una cola de prioridad usando listas.
class ColaPrioridadSimple:
    def __init__(self):
        self.elementos = []

    def enqueue(self, valor, prioridad):
        self.elementos.append((valor, prioridad))
        self.elementos.sort(key=lambda x: x[1])

    def dequeue(self):
        if not self.elementos:
            return None
        return self.elementos.pop(0)[0]

    def front(self):
        return self.elementos[0][0] if self.elementos else None


# 16. Cola con dos stacks eficiente (versión simplificada)
class ColaEficiente:
    def __init__(self):
        self.stack_entrada = []
        self.stack_salida = []

    def enqueue(self, valor):
        self.stack_entrada.append(valor)

    def dequeue(self):
        if not self.stack_salida:
            while self.stack_entrada:
                self.stack_salida.append(self.stack_entrada.pop())
        return self.stack_salida.pop() if self.stack_salida else None

    def _transferir(self):
        while self.stack_entrada:
            self.stack_salida.append(self.stack_entrada.pop())

    def front(self):
        if not self.stack_salida:
            self._transferir()
        return self.stack_salida[-1] if self.stack_salida else None


# 17. Intercalar colas
def intercalar_colas(cola1, cola2):
    resultado = []
    while cola1 and cola2:
        resultado.append(cola1.pop(0))
        resultado.append(cola2.pop(0))
    resultado.extend(cola1)
    resultado.extend(cola2)
    return resultado


# 18. Revertir cola recursivamente
def revertir_cola_recursiva(cola):
    if not cola:
        return
    frente = cola.pop(0)
    revertir_cola_recursiva(cola)
    cola.append(frente)


# 19. Problema del puente (simulación simple)
class Puente:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.cola_entrada = []
        self.puente = []

    def llegar_vehiculo(self, vehiculo):
        if len(self.puente) < self.capacidad:
            self.puente.append(vehiculo)
            # print(f"{vehiculo} entra al puente")
        else:
            self.cola_entrada.append(vehiculo)
            # print(f"{vehiculo} espera en cola")

    def salir_vehiculo(self):
        if not self.puente:
            return None
        vehiculo = self.puente.pop(0)
        if self.cola_entrada:
            siguiente = self.cola_entrada.pop(0)
            self.puente.append(siguiente)
        return vehiculo


# 20. Cola con máximo en O(1)
from collections import deque


class ColaConMaximo:
    def __init__(self):
        self.cola_principal = deque()
        self.cola_maximos = deque()

    def enqueue(self, valor):
        self.cola_principal.append(valor)
        while self.cola_maximos and self.cola_maximos[-1] < valor:
            self.cola_maximos.pop()
        self.cola_maximos.append(valor)

    def dequeue(self):
        if not self.cola_principal:
            return None
        valor = self.cola_principal.popleft()
        if self.cola_maximos and valor == self.cola_maximos[0]:
            self.cola_maximos.popleft()
        return valor

    def max(self):
        return self.cola_maximos[0] if self.cola_maximos else None


# ------------------------------------
# LISTAS (10 ejercicios)
# ------------------------------------

# 21. Intersección de listas ordenadas
def interseccion_listas_ordenadas(lista1, lista2):
    i, j = 0, 0
    resultado = []
    while i < len(lista1) and j < len(lista2):
        if lista1[i] == lista2[j]:
            resultado.append(lista1[i])
            i += 1
            j += 1
        elif lista1[i] < lista2[j]:
            i += 1
        else:
            j += 1
    return resultado


# 22. Unión de listas ordenadas
def union_listas_ordenadas(lista1, lista2):
    i, j = 0, 0
    resultado = []
    while i < len(lista1) and j < len(lista2):
        if lista1[i] < lista2[j]:
            resultado.append(lista1[i])
            i += 1
        elif lista1[i] > lista2[j]:
            resultado.append(lista2[j])
            j += 1
        else:
            resultado.append(lista1[i])
            i += 1
            j += 1
    resultado.extend(lista1[i:])
    resultado.extend(lista2[j:])
    # Eliminar duplicados consecutivos si es necesario
    res = []
    for x in resultado:
        if not res or res[-1] != x:
            res.append(x)
    return res


# 23. Rotar lista
def rotar_lista(lista, k):
    if not lista:
        return lista
    k = k % len(lista)
    return lista[-k:] + lista[:-k]


# 24. Mover ceros al final
def mover_ceros_al_final(lista):
    no_ceros = [x for x in lista if x != 0]
    ceros = [0] * (len(lista) - len(no_ceros))
    return no_ceros + ceros


def mover_ceros_al_final_inplace(lista):
    pos = 0
    for i in range(len(lista)):
        if lista[i] != 0:
            lista[pos], lista[i] = lista[i], lista[pos]
            pos += 1


# 25. Encontrar duplicados
def encontrar_duplicados(lista):
    vistos = set()
    duplicados = set()
    for elemento in lista:
        if elemento in vistos:
            duplicados.add(elemento)
        else:
            vistos.add(elemento)
    return list(duplicados)


# 26. Producto máximo de sublista
def producto_maximo_sublista(lista):
    if not lista:
        return 0
    max_producto = lista[0]
    min_producto = lista[0]
    resultado = lista[0]
    for i in range(1, len(lista)):
        if lista[i] < 0:
            max_producto, min_producto = min_producto, max_producto
        max_producto = max(lista[i], max_producto * lista[i])
        min_producto = min(lista[i], min_producto * lista[i])
        resultado = max(resultado, max_producto)
    return resultado


# 27. Lista de Pascal (fila específica)
def fila_triangulo_pascal(n):
    if n == 0:
        return [1]
    fila_anterior = [1]
    for i in range(1, n + 1):
        fila_actual = [1]
        for j in range(1, i):
            fila_actual.append(fila_anterior[j - 1] + fila_anterior[j])
        fila_actual.append(1)
        fila_anterior = fila_actual
    return fila_anterior


# 28. Combinar k listas ordenadas
import heapq


def combinar_listas_ordenadas(listas):
    heap = []
    resultado = []
    for i, lista in enumerate(listas):
        if lista:
            heapq.heappush(heap, (lista[0], i, 0))
    while heap:
        valor, lista_idx, elem_idx = heapq.heappop(heap)
        resultado.append(valor)
        if elem_idx + 1 < len(listas[lista_idx]):
            siguiente_valor = listas[lista_idx][elem_idx + 1]
            heapq.heappush(heap, (siguiente_valor, lista_idx, elem_idx + 1))
    return resultado


# 29. Subconjuntos
def generar_subconjuntos(lista):
    resultado = [[]]
    for elemento in lista:
        nuevos_subconjuntos = []
        for subconjunto in resultado:
            nuevos_subconjuntos.append(subconjunto + [elemento])
        resultado.extend(nuevos_subconjuntos)
    return resultado


# 30. Mayor rectángulo en histograma
def mayor_rectangulo_histograma(alturas):
    pila = []
    max_area = 0
    i = 0
    while i < len(alturas):
        if not pila or alturas[i] >= alturas[pila[-1]]:
            pila.append(i)
            i += 1
        else:
            top = pila.pop()
            ancho = i if not pila else i - pila[-1] - 1
            area = alturas[top] * ancho
            max_area = max(max_area, area)
    while pila:
        top = pila.pop()
        ancho = i if not pila else len(alturas) - pila[-1] - 1
        area = alturas[top] * ancho
        max_area = max(max_area, area)
    return max_area


# ------------------------------------
# LISTAS ENLAZADAS SIMPLES (10 ejercicios)
# ------------------------------------

# 31. Invertir lista enlazada
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, valor):
        nuevo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def invertir(self):
        anterior = None
        actual = self.cabeza
        while actual:
            siguiente_temp = actual.siguiente
            actual.siguiente = anterior
            anterior = actual
            actual = siguiente_temp
        self.cabeza = anterior

    def imprimir(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")


# 32. Detectar ciclo (usar ListaEnlazada definida arriba)
def tiene_ciclo(lista):
    if not lista.cabeza:
        return False
    lento = lista.cabeza
    rapido = lista.cabeza
    while rapido and rapido.siguiente:
        lento = lento.siguiente
        rapido = rapido.siguiente.siguiente
        if lento == rapido:
            return True
    return False


# 33. Encontrar intersección de dos listas enlazadas
def encontrar_interseccion(lista1, lista2):
    if not lista1.cabeza or not lista2.cabeza:
        return None
    len1, len2 = 0, 0
    actual1, actual2 = lista1.cabeza, lista2.cabeza
    while actual1:
        len1 += 1
        actual1 = actual1.siguiente
    while actual2:
        len2 += 1
        actual2 = actual2.siguiente
    actual1, actual2 = lista1.cabeza, lista2.cabeza
    if len1 > len2:
        for _ in range(len1 - len2):
            actual1 = actual1.siguiente
    else:
        for _ in range(len2 - len1):
            actual2 = actual2.siguiente
    while actual1 and actual2:
        if actual1 == actual2:
            return actual1
        actual1 = actual1.siguiente
        actual2 = actual2.siguiente
    return None


# 34. Eliminar duplicados en lista enlazada ordenada
def eliminar_duplicados_ordenada(lista):
    if not lista.cabeza:
        return
    actual = lista.cabeza
    while actual and actual.siguiente:
        if actual.valor == actual.siguiente.valor:
            actual.siguiente = actual.siguiente.siguiente
        else:
            actual = actual.siguiente


# 35. N-ésimo nodo desde el final
def nesimo_desde_final(lista, n):
    if not lista.cabeza or n <= 0:
        return None
    primero = lista.cabeza
    segundo = lista.cabeza
    for _ in range(n):
        if not primero:
            return None
        primero = primero.siguiente
    while primero:
        primero = primero.siguiente
        segundo = segundo.siguiente
    return segundo.valor if segundo else None


# 36. Suma de números como listas
def sumar_listas_numeros(lista1, lista2):
    def lista_a_numero(lista):
        num = 0
        actual = lista.cabeza
        while actual:
            num = num * 10 + actual.valor
            actual = actual.siguiente
        return num
    num1 = lista_a_numero(lista1)
    num2 = lista_a_numero(lista2)
    suma = num1 + num2
    resultado = ListaEnlazada()
    for digito in str(suma):
        resultado.agregar(int(digito))
    return resultado


# 37. Palíndromo en lista enlazada
def es_palindromo(lista):
    lento = lista.cabeza
    rapido = lista.cabeza
    pila = []
    while rapido and rapido.siguiente:
        pila.append(lento.valor)
        lento = lento.siguiente
        rapido = rapido.siguiente.siguiente
    if rapido:
        lento = lento.siguiente
    while lento:
        if pila.pop() != lento.valor:
            return False
        lento = lento.siguiente
    return True


# 38. Rotar lista enlazada k posiciones a la derecha
def rotar_lista_enlazada(lista, k):
    if not lista.cabeza or k == 0:
        return
    longitud = 0
    actual = lista.cabeza
    while actual:
        longitud += 1
        actual = actual.siguiente
    k = k % longitud
    if k == 0:
        return
    actual = lista.cabeza
    for _ in range(longitud - k - 1):
        actual = actual.siguiente
    nuevo_head = actual.siguiente
    actual.siguiente = None
    tail = nuevo_head
    while tail.siguiente:
        tail = tail.siguiente
    tail.siguiente = lista.cabeza
    lista.cabeza = nuevo_head


# 39. Eliminar nodos alternativos
def eliminar_nodos_alternativos(lista):
    if not lista.cabeza:
        return
    actual = lista.cabeza
    while actual and actual.siguiente:
        actual.siguiente = actual.siguiente.siguiente
        actual = actual.siguiente


# 40. Punto de unión en Y (similar a intersección)
def encontrar_punto_union(lista1, lista2):
    def obtener_longitud(lista):
        longitud = 0
        actual = lista.cabeza
        while actual:
            longitud += 1
            actual = actual.siguiente
        return longitud
    len1 = obtener_longitud(lista1)
    len2 = obtener_longitud(lista2)
    actual1, actual2 = lista1.cabeza, lista2.cabeza
    if len1 > len2:
        for _ in range(len1 - len2):
            actual1 = actual1.siguiente
    else:
        for _ in range(len2 - len1):
            actual2 = actual2.siguiente
    while actual1 and actual2:
        if actual1 == actual2:
            return actual1
        actual1 = actual1.siguiente
        actual2 = actual2.siguiente
    return None


# ------------------------------------
# LISTAS DOBLEMENTE ENLAZADAS (5 ejercicios)
# ------------------------------------

# 41. Implementar LRU Cache
class NodoDoble:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.siguiente = None
        self.anterior = None


class LRUCache:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.cache = {}
        self.head = NodoDoble(0, 0)
        self.tail = NodoDoble(0, 0)
        self.head.siguiente = self.tail
        self.tail.anterior = self.head

    def _agregar_nodo(self, nodo):
        nodo.siguiente = self.head.siguiente
        nodo.anterior = self.head
        self.head.siguiente.anterior = nodo
        self.head.siguiente = nodo

    def _remover_nodo(self, nodo):
        anterior = nodo.anterior
        siguiente = nodo.siguiente
        anterior.siguiente = siguiente
        siguiente.anterior = anterior

    def _mover_a_frente(self, nodo):
        self._remover_nodo(nodo)
        self._agregar_nodo(nodo)

    def get(self, key):
        if key in self.cache:
            nodo = self.cache[key]
            self._mover_a_frente(nodo)
            return nodo.value
        return -1

    def put(self, key, value):
        if key in self.cache:
            nodo = self.cache[key]
            nodo.value = value
            self._mover_a_frente(nodo)
        else:
            if len(self.cache) >= self.capacidad:
                lru = self.tail.anterior
                self._remover_nodo(lru)
                del self.cache[lru.key]
            nuevo_nodo = NodoDoble(key, value)
            self.cache[key] = nuevo_nodo
            self._agregar_nodo(nuevo_nodo)


# 42. Polinomio con lista doble
class Termino:
    def __init__(self, coeficiente, exponente):
        self.coeficiente = coeficiente
        self.exponente = exponente
        self.siguiente = None
        self.anterior = None


class Polinomio:
    def __init__(self):
        self.cabeza = None

    def agregar_termino(self, coeficiente, exponente):
        nuevo = Termino(coeficiente, exponente)
        if not self.cabeza:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo
            nuevo.anterior = actual

    def sumar(self, otro):
        resultado = Polinomio()
        actual1 = self.cabeza
        actual2 = otro.cabeza
        while actual1 and actual2:
            if actual1.exponente == actual2.exponente:
                suma_coef = actual1.coeficiente + actual2.coeficiente
                if suma_coef != 0:
                    resultado.agregar_termino(suma_coef, actual1.exponente)
                actual1 = actual1.siguiente
                actual2 = actual2.siguiente
            elif actual1.exponente > actual2.exponente:
                resultado.agregar_termino(actual1.coeficiente, actual1.exponente)
                actual1 = actual1.siguiente
            else:
                resultado.agregar_termino(actual2.coeficiente, actual2.exponente)
                actual2 = actual2.siguiente
        while actual1:
            resultado.agregar_termino(actual1.coeficiente, actual1.exponente)
            actual1 = actual1.siguiente
        while actual2:
            resultado.agregar_termino(actual2.coeficiente, actual2.exponente)
            actual2 = actual2.siguiente
        return resultado

    def imprimir(self):
        actual = self.cabeza
        while actual:
            print(f"{actual.coeficiente}x^{actual.exponente}", end="")
            if actual.siguiente:
                print(" + ", end="")
            actual = actual.siguiente
        print()


# 43. Navegador web simple (adelante/atrás)
class NavegadorWeb:
    def __init__(self):
        self._pagina_actual = None
        self.historial_atras = []
        self.historial_adelante = []

    def visitar_pagina(self, url):
        if self._pagina_actual:
            self.historial_atras.append(self._pagina_actual)
        self._pagina_actual = url
        self.historial_adelante.clear()

    def atras(self):
        if self.historial_atras:
            self.historial_adelante.append(self._pagina_actual)
            self._pagina_actual = self.historial_atras.pop()
        else:
            return None

    def adelante(self):
        if self.historial_adelante:
            self.historial_atras.append(self._pagina_actual)
            self._pagina_actual = self.historial_adelante.pop()
        else:
            return None

    def obtener_pagina_actual(self):
        return self._pagina_actual


# 44. Playlist de música (doblemente enlazada)
class Cancion:
    def __init__(self, titulo, artista):
        self.titulo = titulo
        self.artista = artista
        self.siguiente = None
        self.anterior = None


class Playlist:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.actual = None

    def agregar_cancion(self, titulo, artista):
        nueva = Cancion(titulo, artista)
        if not self.cabeza:
            self.cabeza = nueva
            self.cola = nueva
            self.actual = nueva
        else:
            self.cola.siguiente = nueva
            nueva.anterior = self.cola
            self.cola = nueva

    def reproducir_siguiente(self):
        if self.actual and self.actual.siguiente:
            self.actual = self.actual.siguiente
        else:
            return None

    def reproducir_anterior(self):
        if self.actual and self.actual.anterior:
            self.actual = self.actual.anterior
        else:
            return None

    def eliminar_cancion_actual(self):
        if not self.actual:
            return
        if self.actual.anterior:
            self.actual.anterior.siguiente = self.actual.siguiente
        else:
            self.cabeza = self.actual.siguiente
        if self.actual.siguiente:
            self.actual.siguiente.anterior = self.actual.anterior
        else:
            self.cola = self.actual.anterior
        siguiente = self.actual.siguiente if self.actual.siguiente else self.cabeza
        self.actual = siguiente

    def mostrar_playlist(self):
        actual = self.cabeza
        while actual:
            marcador = " [ACTUAL]" if actual == self.actual else ""
            print(f"{actual.titulo} - {actual.artista}{marcador}")
            actual = actual.siguiente


# 45. Texto editor con undo (modelo simplificado)
class EstadoTexto:
    def __init__(self, texto):
        self.texto = texto
        self.siguiente = None
        self.anterior = None


class EditorTexto:
    def __init__(self):
        self.estado_actual = EstadoTexto("")
        self.max_historial = 10
        self.contador_estados = 1

    def escribir(self, texto):
        nuevo_estado = EstadoTexto(self.estado_actual.texto + texto)
        nuevo_estado.anterior = self.estado_actual
        self.estado_actual.siguiente = nuevo_estado
        self.estado_actual = nuevo_estado
        self.contador_estados += 1
        if self.contador_estados > self.max_historial:
            viejo = self.estado_actual
            for _ in range(self.max_historial):
                viejo = viejo.anterior
            if viejo:
                viejo.anterior = None

    def deshacer(self):
        if self.estado_actual.anterior:
            self.estado_actual = self.estado_actual.anterior
            return True
        return False

    def rehacer(self):
        if self.estado_actual.siguiente:
            self.estado_actual = self.estado_actual.siguiente
            return True
        return False

    def obtener_texto(self):
        return self.estado_actual.texto


# ------------------------------------
# LISTAS CIRCULARES (5 ejercicios)
# ------------------------------------

# 46. Problema de Josephus (lista circular básica)
class NodoCircular:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None


def problema_josephus(n, k):
    if n == 1:
        return 1
    cabeza = NodoCircular(1)
    actual = cabeza
    for i in range(2, n + 1):
        actual.siguiente = NodoCircular(i)
        actual = actual.siguiente
    actual.siguiente = cabeza
    actual = cabeza
    # Usamos una simulación básica
    while actual.siguiente != actual:
        for _ in range(k - 2):
            actual = actual.siguiente
        actual.siguiente = actual.siguiente.siguiente
        actual = actual.siguiente
    return actual.valor


# 47. Lista circular ordenada (insertar ordenado)
class ListaCircularOrdenada:
    def __init__(self):
        self.cabeza = None

    def insertar_ordenado(self, valor):
        nuevo = NodoCircular(valor)
        if not self.cabeza:
            self.cabeza = nuevo
            nuevo.siguiente = nuevo
            return
        if valor < self.cabeza.valor:
            cola = self.cabeza
            while cola.siguiente != self.cabeza:
                cola = cola.siguiente
            nuevo.siguiente = self.cabeza
            cola.siguiente = nuevo
            self.cabeza = nuevo
            return
        actual = self.cabeza
        while actual.siguiente != self.cabeza and actual.siguiente.valor < valor:
            actual = actual.siguiente
        nuevo.siguiente = actual.siguiente
        actual.siguiente = nuevo

    def imprimir(self):
        if not self.cabeza:
            return
        actual = self.cabeza
        while True:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        print("(cabeza)")


# 48. Dividir lista circular en dos mitades
def dividir_lista_circular(lista):
    if not lista.cabeza or lista.cabeza.siguiente == lista.cabeza:
        return lista, None
    tortuga = lista.cabeza
    liebre = lista.cabeza
    while liebre.siguiente != lista.cabeza and liebre.siguiente.siguiente != lista.cabeza:
        tortuga = tortuga.siguiente
        liebre = liebre.siguiente.siguiente
    cabeza2 = tortuga.siguiente
    tortuga.siguiente = lista.cabeza
    actual = cabeza2
    while actual.siguiente != lista.cabeza:
        actual = actual.siguiente
    actual.siguiente = cabeza2
    lista2 = ListaCircularOrdenada()
    lista2.cabeza = cabeza2
    return lista, lista2


# 49. Verificar lista circular (tortuga y liebre)
def es_lista_circular(lista):
    if not lista.cabeza:
        return False
    tortuga = lista.cabeza
    liebre = lista.cabeza
    while liebre and liebre.siguiente:
        tortuga = tortuga.siguiente
        liebre = liebre.siguiente.siguiente
        if tortuga == liebre:
            return True
    return False


# 50. Rotar lista circular k posiciones
def rotar_lista_circular(lista, k):
    if not lista.cabeza or k == 0:
        return
    longitud = 1
    actual = lista.cabeza
    while actual.siguiente != lista.cabeza:
        longitud += 1
        actual = actual.siguiente
    k = k % longitud
    if k == 0:
        return
    actual = lista.cabeza
    for _ in range(longitud - k - 1):
        actual = actual.siguiente
    lista.cabeza = actual.siguiente


# Fin del archivo: si se importa, no ejecutamos pruebas automáticamente.
if __name__ == "__main__":
    # Pruebas simples demostrativas
    print("Balanceo:", balanceo_parentesis("({[]})"))
    print("Infijo a postfijo:", infijo_a_postfijo("( A + B ) * C"))
    print("Evaluar postfijo:", evaluar_postfijo("3 4 + 2 *"))
    print("Invertir lista:", invertir_lista_pila([1,2,3,4,5]))
    # Lista enlazada ejemplo
    l = ListaEnlazada()
    for i in range(1, 6):
        l.agregar(i)
    l.invertir()
    l.imprimir()
