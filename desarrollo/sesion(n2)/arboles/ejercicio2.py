# Árbol de expresiones matemáticas con tuplas (inmutables)
# Estructura: (operador, operando_izq, operando_der)
# Representa la expresión: (3 + 5) * (2 - 1)

# Crear subexpresión: 3 + 5
suma = ('+', 3, 5)

# Crear subexpresión: 2 - 1
resta = ('-', 2, 1)

# Combinar en expresión principal: (3 + 5) * (2 - 1)
expresion = ('*', suma, resta)

# Función para evaluar el árbol de expresiones
def evaluar(nodo):
    # Si el nodo es un número, devolverlo directamente
    if isinstance(nodo, (int, float)):
        return nodo
    
    # Extraer operador y operandos
    operador, izq, der = nodo
    
    # Evaluar recursivamente los operandos
    valor_izq = evaluar(izq)
    valor_der = evaluar(der)
    
    # Aplicar la operación según el operador
    if operador == '+':
        return valor_izq + valor_der
    elif operador == '-':
        return valor_izq - valor_der
    elif operador == '*':
        return valor_izq * valor_der
    elif operador == '/':
        return valor_izq / valor_der

# Evaluar la expresión completa
resultado = evaluar(expresion)
print(f"Resultado de (3 + 5) * (2 - 1) = {resultado}")  # Salida: 8