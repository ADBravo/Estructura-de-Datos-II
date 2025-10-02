import heapq  # Para implementar la cola de prioridad
import random  # Para generar costos aleatorios
import math   # Para la heurística en A*

# --- Representación del Grafo ---
# Usaremos un diccionario donde las claves son los nodos y los valores son
# otros diccionarios que representan los vecinos y el costo de la arista.
# Ejemplo: { 'A': {'B': 5, 'C': 2}, 'B': {'A': 5, 'D': 3}, ... }

# --- Implementación del Algoritmo de Dijkstra ---
def dijkstra(graph, start_node, end_node):
    """
    Implementa el algoritmo de Dijkstra para encontrar el camino más corto
    desde un nodo de inicio a un nodo final en un grafo con costos.

    Args:
        graph (dict): El grafo representado como un diccionario.
        start_node (str): El nodo de inicio.
        end_node (str): El nodo final.

    Returns:
        tuple: Una tupla que contiene:
            - list: El camino más corto encontrado (lista de nodos).
            - float: El costo total del camino más corto.
            - int: La cantidad de nodos expandidos.
    """
    # Distancias iniciales: infinito para todos los nodos excepto el de inicio (0)
    distances = {node: float('inf') for node in graph}
    distances[start_node] = 0

    # Cola de prioridad para almacenar nodos a visitar, ordenados por su distancia
    # Formato: (distancia, nodo)
    priority_queue = [(0, start_node)]

    # Diccionario para rastrear el predecesor de cada nodo en el camino más corto
    predecessors = {}

    # Conjunto de nodos visitados
    visited = set()

    # Contador de nodos expandidos
    expanded_nodes_count = 0

    while priority_queue:
        # Obtener el nodo con la menor distancia de la cola de prioridad
        # heapq.heappop() saca el elemento más pequeño, que es el de menor distancia
        current_distance, current_node = heapq.heappop(priority_queue)

        # Si el nodo ya fue visitado, saltamos para evitar ciclos y trabajo redundante
        if current_node in visited:
            continue

        # Marcamos el nodo como visitado y incrementamos el contador de nodos expandidos
        visited.add(current_node)
        expanded_nodes_count += 1

        # Si hemos llegado al nodo final, reconstruimos el camino y retornamos
        if current_node == end_node:
            path = []
            # Retrocedemos desde el nodo final hasta el de inicio usando los predecesores
            while current_node:
                path.append(current_node)
                current_node = predecessors.get(current_node) # .get() maneja el caso None para el start_node
            return path[::-1], distances[end_node], expanded_nodes_count # Retorna el camino invertido y el costo

        # Explorar los vecinos del nodo actual
        for neighbor, weight in graph.get(current_node, {}).items(): # graph.get() evita KeyError si un nodo no tiene vecinos
            distance = current_distance + weight

            # Si encontramos un camino más corto al vecino a través del nodo actual
            if distance < distances[neighbor]:
                distances[neighbor] = distance # Actualizamos la distancia más corta al vecino
                predecessors[neighbor] = current_node # Registramos que llegamos al vecino desde current_node
                heapq.heappush(priority_queue, (distance, neighbor)) # Añadimos el vecino a la cola de prioridad con su nueva distancia

    # Si el bucle termina y no hemos retornado (es decir, no se encontró el end_node)
    return [], float('inf'), expanded_nodes_count # Retorna un camino vacío, infinito costo y el total de nodos expandidos

# --- Implementación del Algoritmo A* ---
def heuristic(node, goal_node):
    """
    Función heurística simple. En este ejemplo, usaremos una heurística
    que devuelve 0. En un escenario real, esto podría ser la distancia
    euclidiana o Manhattan si tuviéramos coordenadas para los nodos.
    Una heurística informativa (admisible y consistente) mejora A* sobre Dijkstra.
    Para este ejemplo, una heurística trivial es suficiente para mostrar la estructura.
    """
    # Si tuviéramos información de coordenadas (por ejemplo, en un mapa):
    # return abs(node_coords[node][0] - node_coords[goal_node][0]) + abs(node_coords[node][1] - node_coords[goal_node][1])
    # Con la información actual, una heurística de 0 es admisible (nunca sobreestima).
    return 0

def a_star(graph, start_node, end_node):
    """
    Implementa el algoritmo A* para encontrar el camino más corto
    desde un nodo de inicio a un nodo final en un grafo con costos.

    Args:
        graph (dict): El grafo representado como un diccionario.
        start_node (str): El nodo de inicio.
        end_node (str): El nodo final.

    Returns:
        tuple: Una tupla que contiene:
            - list: El camino más corto encontrado (lista de nodos).
            - float: El costo total del camino más corto.
            - int: La cantidad de nodos expandidos.
    """
    # g_score: costo real desde el inicio hasta este nodo. Inicializado a infinito.
    g_scores = {node: float('inf') for node in graph}
    g_scores[start_node] = 0

    # f_score: costo total estimado desde el inicio hasta el final a través de este nodo. f = g + h
    # Inicializado a infinito para todos, excepto para el start_node.
    f_scores = {node: float('inf') for node in graph}
    f_scores[start_node] = heuristic(start_node, end_node) # f_score del start_node es solo su heurística

    # Cola de prioridad para almacenar nodos a explorar, ordenados por f_score.
    # Formato: (f_score, nodo)
    open_set = [(f_scores[start_node], start_node)]
    # Un conjunto auxiliar para chequear rápidamente si un nodo está en open_set.
    open_set_hash = {start_node}

    # Diccionario para rastrear el predecesor de cada nodo en el camino más corto
    came_from = {}

    # Contador de nodos expandidos
    expanded_nodes_count = 0

    while open_set:
        # Obtener el nodo con el menor f_score de la cola de prioridad
        current_f_score, current_node = heapq.heappop(open_set)
        open_set_hash.remove(current_node) # Lo removemos del conjunto auxiliar

        # Si hemos llegado al nodo final, reconstruimos el camino y retornamos
        if current_node == end_node:
            path = []
            # Retrocedemos desde el nodo final hasta el de inicio usando came_from
            while current_node:
                path.append(current_node)
                current_node = came_from.get(current_node)
            return path[::-1], g_scores[end_node], expanded_nodes_count # Retorna el camino invertido y el costo g_score

        # Explorar los vecinos del nodo actual
        for neighbor, weight in graph.get(current_node, {}).items():
            # Calcular el costo tentativo para llegar al vecino a través del nodo actual
            tentative_g_score = g_scores[current_node] + weight

            # Si este camino (a través de current_node) es mejor que el anterior camino conocido para el vecino
            if tentative_g_score < g_scores[neighbor]:
                came_from[neighbor] = current_node # Actualizamos el predecesor del vecino
                g_scores[neighbor] = tentative_g_score # Actualizamos el costo real hasta el vecino
                f_scores[neighbor] = g_scores[neighbor] + heuristic(neighbor, end_node) # Calculamos el nuevo f_score

                # Si el vecino no está actualmente en el conjunto abierto (open_set), lo añadimos
                if neighbor not in open_set_hash:
                    heapq.heappush(open_set, (f_scores[neighbor], neighbor)) # Lo añadimos a la cola de prioridad
                    open_set_hash.add(neighbor) # Lo añadimos al conjunto auxiliar
                # Si el vecino ya está en open_set, su prioridad (f_score) ya se ha actualizado
                # si es necesario. heapq no soporta actualización directa de prioridades;
                # se pueden añadir duplicados, pero se manejarán al ser extraídos.

        # Incrementamos el contador de nodos expandidos después de procesar un nodo
        # (es decir, cuando lo sacamos del open_set para explorar sus vecinos)
        expanded_nodes_count += 1

    # Si el bucle termina y no hemos retornado (es decir, no se encontró el end_node)
    return [], float('inf'), expanded_nodes_count # Retorna un camino vacío, infinito costo y el total de nodos expandidos

# --- Generación del Grafo ---
def generate_random_graph(num_nodes, avg_degree, max_weight):
    """
    Genera un grafo aleatorio con costos en las aristas.

    Args:
        num_nodes (int): Número de nodos en el grafo.
        avg_degree (float): Grado promedio de los nodos (número de aristas por nodo).
        max_weight (int): Peso máximo aleatorio para las aristas.

    Returns:
        dict: El grafo generado.
    """
    # Crea una lista de nodos con letras ('A', 'B', 'C', ...)
    nodes = [chr(i + 65) for i in range(num_nodes)]
    graph = {node: {} for node in nodes} # Inicializa el diccionario del grafo

    # Calcula el número total de aristas a crear para alcanzar el grado promedio deseado
    # Dividimos por 2 porque cada arista conecta dos nodos
    num_edges_to_create = int(num_nodes * avg_degree / 2)

    # Genera las aristas aleatoriamente
    for _ in range(num_edges_to_create):
        # Selecciona dos nodos distintos al azar
        u, v = random.sample(nodes, 2)

        # Si la arista (u, v) aún no existe en el grafo (evita duplicados y auto-bucles)
        if v not in graph[u]:
            weight = random.randint(1, max_weight) # Genera un peso aleatorio
            graph[u][v] = weight # Añade la arista en una dirección
            graph[v][u] = weight # Añade la arista en la dirección opuesta (grafo no dirigido)

    # Intenta asegurarse de que todos los nodos tengan al menos una conexión si el grafo es pequeño
    # y se generaron pocas aristas inicialmente.
    if num_nodes > 1:
        for node in nodes:
            if not graph[node]: # Si un nodo no tiene vecinos
                potential_neighbors = [n for n in nodes if n != node] # Obtiene todos los demás nodos
                if potential_neighbors:
                    neighbor = random.choice(potential_neighbors) # Elige un vecino al azar
                    weight = random.randint(1, max_weight) # Genera un peso
                    graph[node][neighbor] = weight
                    graph[neighbor][node] = weight # Añade la arista

    return graph

# --- Ejemplo de Ejecución ---
if __name__ == "__main__":
    # Configuración del grafo
    NUM_NODES = 10         # Número de nodos en el grafo
    AVG_DEGREE = 3         # Grado promedio deseado de los nodos
    MAX_WEIGHT = 20        # Peso máximo para las aristas

    # Generar el grafo aleatorio
    graph = generate_random_graph(NUM_NODES, AVG_DEGREE, MAX_WEIGHT)

    # Definir nodo de inicio y final
    start_node = 'A'
    # El último nodo creado se calcula como el carácter ASCII de 65 (para 'A') más el número de nodos menos 1
    end_node = chr(65 + NUM_NODES - 1)

    # Validar que los nodos de inicio y fin existen en el grafo (importante si NUM_NODES es muy pequeño)
    if start_node not in graph or end_node not in graph:
        print(f"Error: Los nodos de inicio ('{start_node}') o final ('{end_node}') no existen en el grafo generado.")
    else:
        print("--- Grafo Generado ---")
        # Imprimir la estructura del grafo
        for node, neighbors in graph.items():
            print(f"{node}: {neighbors}")
        print("-" * 30) # Separador visual

        print(f"Buscando camino más corto de '{start_node}' a '{end_node}'")
        print("-" * 30)

        # --- Ejecución de Dijkstra ---
        print("Ejecutando Algoritmo de Dijkstra...")
        # Llamamos a la función dijkstra y guardamos los resultados
        dijkstra_path, dijkstra_cost, dijkstra_expanded = dijkstra(graph, start_node, end_node)

        print("\n--- Resultados de Dijkstra ---")
        if dijkstra_path: # Si se encontró un camino (la lista no está vacía)
            print(f"Camino más corto: {' -> '.join(dijkstra_path)}") # Une los nodos del camino con '->'
            print(f"Costo total: {dijkstra_cost}")
        else:
            print("No se encontró un camino.")
        print(f"Nodos expandidos: {dijkstra_expanded}")
        print("-" * 30)

        # --- Ejecución de A* ---
        print("Ejecutando Algoritmo A*...")
        # Llamamos a la función a_star y guardamos los resultados
        a_star_path, a_star_cost, a_star_expanded = a_star(graph, start_node, end_node)

        print("\n--- Resultados de A* ---")
        if a_star_path: # Si se encontró un camino
            print(f"Camino más corto: {' -> '.join(a_star_path)}")
            print(f"Costo total: {a_star_cost}")
        else:
            print("No se encontró un camino.")
        print(f"Nodos expandidos: {a_star_expanded}")
        print("-" * 30)

        # --- Comparación de Resultados ---
        print("--- Comparación de Resultados ---")
        if dijkstra_path and a_star_path: # Si ambos algoritmos encontraron un camino
            print("Ambos algoritmos encontraron un camino.")
            print(f"Dijkstra - Camino: {' -> '.join(dijkstra_path)}, Costo: {dijkstra_cost}, Nodos expandidos: {dijkstra_expanded}")
            print(f"A*       - Camino: {' -> '.join(a_star_path)}, Costo: {a_star_cost}, Nodos expandidos: {a_star_expanded}")

            # Verificación de igualdad entre los resultados
            if dijkstra_path == a_star_path and dijkstra_cost == a_star_cost:
                print("\nLos caminos y costos encontrados por ambos algoritmos son idénticos.")
            elif dijkstra_cost == a_star_cost:
                print("\nAmbos algoritmos encontraron el mismo costo mínimo, pero los caminos son diferentes.")
                print("Esto es posible si existen múltiples caminos óptimos con el mismo costo total.")
            else:
                print("\nAdvertencia: Los costos o caminos encontrados por los algoritmos difieren significativamente.")
                print("Esto podría indicar un problema con la implementación de la heurística en A*")
                print("(ej. heurística no admisible) o simplemente la naturaleza de la búsqueda.")
                print("En este ejemplo, con una heurística trivial (siempre 0), A* se comporta muy similar a Dijkstra.")
        elif dijkstra_path:
            print("Dijkstra encontró un camino, pero A* no pudo.")
        elif a_star_path:
            print("A* encontró un camino, pero Dijkstra no pudo.")
        else:
            print("Ninguno de los algoritmos encontró un camino entre los nodos especificados.")
        print("-" * 30)