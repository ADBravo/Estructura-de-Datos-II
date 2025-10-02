# Árbol de decisión para clasificar animales usando conjuntos
# Los conjuntos permiten verificaciones rápidas de pertenencia

class NodoDecision:
    # Clase para nodos de decisión con conjuntos de respuestas válidas
    def __init__(self, pregunta, respuestas_validas):
        self.pregunta = pregunta  # Pregunta a realizar
        self.respuestas_validas = set(respuestas_validas)  # Conjunto de respuestas válidas
        self.hijos = {}  # Diccionario: respuesta -> siguiente nodo
        self.resultado = None  # Resultado final si es nodo hoja
    
    def agregar_hijo(self, respuesta, nodo):
        # Agregar un hijo al árbol de decisión
        if respuesta in self.respuestas_validas:
            self.hijos[respuesta] = nodo
        else:
            print(f"⚠️ Error: '{respuesta}' no es una respuesta válida")
    
    def es_hoja(self):
        # Verificar si es un nodo hoja (nodo final con resultado)
        return self.resultado is not None

# Construir el árbol de decisión para clasificar animales
# Estructura del árbol:
#                   ¿Tiene pelo?
#                   /         \
#                 Sí          No
#                 /            \
#         ¿Es grande?      ¿Puede volar?
#          /    \            /      \
#        Sí     No         Sí       No
#        |      |          |        |
#      Oso   Gato      Pájaro   Serpiente

# Crear nodos hoja (resultados finales)
nodo_oso = NodoDecision("", [])
nodo_oso.resultado = "🐻 Es un oso"

nodo_gato = NodoDecision("", [])
nodo_gato.resultado = "🐱 Es un gato"

nodo_pajaro = NodoDecision("", [])
nodo_pajaro.resultado = "🐦 Es un pájaro"

nodo_serpiente = NodoDecision("", [])
nodo_serpiente.resultado = "🐍 Es una serpiente"

# Crear nodos de decisión intermedios
nodo_grande = NodoDecision("¿Es grande?", {'si', 'no'})
nodo_grande.agregar_hijo('si', nodo_oso)
nodo_grande.agregar_hijo('no', nodo_gato)

nodo_volar = NodoDecision("¿Puede volar?", {'si', 'no'})
nodo_volar.agregar_hijo('si', nodo_pajaro)
nodo_volar.agregar_hijo('no', nodo_serpiente)

# Crear nodo raíz
raiz = NodoDecision("¿Tiene pelo?", {'si', 'no'})
raiz.agregar_hijo('si', nodo_grande)
raiz.agregar_hijo('no', nodo_volar)

# Función para recorrer el árbol y clasificar
def clasificar(nodo):
    # Si llegamos a un nodo hoja, mostrar resultado
    if nodo.es_hoja():
        print(f"\n🎯 Resultado: {nodo.resultado}")
        return
    
    # Hacer la pregunta y obtener respuesta
    print(f"\n❓ {nodo.pregunta}")
    print(f"   Respuestas válidas: {', '.join(nodo.respuestas_validas)}")
    respuesta = input("   Tu respuesta: ").lower().strip()
    
    # Validar respuesta usando el conjunto
    if respuesta not in nodo.respuestas_validas:
        print(f"   ⚠️ Respuesta inválida. Por favor usa: {nodo.respuestas_validas}")
        return clasificar(nodo)  # Volver a preguntar
    
    # Continuar con el siguiente nodo según la respuesta
    siguiente_nodo = nodo.hijos.get(respuesta)
    if siguiente_nodo:
        clasificar(siguiente_nodo)

# Ejecutar el clasificador
print("=== 🔍 Clasificador de Animales ===")
print("Responde las preguntas para identificar el animal\n")
# clasificar(raiz)  # Descomentar para ejecutar de forma interactiva

# Demostración con respuestas predefinidas
print("Ejemplo 1: Animal con pelo, grande")
print("Resultado esperado: Oso")