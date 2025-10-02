from collections import deque

class MissionariesCannibalsProblem:
    """
    Representa el problema de los Misioneros y Caníbales.
    Define el estado, las acciones posibles y las restricciones.
    """

    def __init__(self, initial_state=None, goal_state=None):
        """
        Inicializa el problema.

        Args:
            initial_state (tuple, optional): Estado inicial.
                Formato: (misioneros_orilla_inicial, canibales_orilla_inicial, bote_orilla_inicial)
                Donde 0 representa la orilla de inicio y 1 la orilla de destino.
                Defaults to (3, 3, 0) -> 3 misioneros, 3 caníbales, bote en la orilla de inicio.
            goal_state (tuple, optional): Estado objetivo.
                Defaults to (0, 0, 1) -> 0 misioneros, 0 caníbales, bote en la orilla de destino.
        """
        self.initial_state = initial_state if initial_state is not None else (3, 3, 0)
        self.goal_state = goal_state if goal_state is not None else (0, 0, 1)

    def is_valid_state(self, state):
        """
        Verifica si un estado dado es válido según las restricciones.

        Args:
            state (tuple): El estado a verificar.
                Formato: (misioneros_orilla_inicial, canibales_orilla_inicial, bote_orilla_inicial)

        Returns:
            bool: True si el estado es válido, False en caso contrario.
        """
        m_start, c_start, b_start = state
        m_end = 3 - m_start
        c_end = 3 - c_start

        # Restricción 1: Si hay misioneros, no pueden ser superados en número por caníbales.
        # Orilla de inicio
        if m_start > 0 and m_start < c_start:
            return False
        # Orilla de destino
        if m_end > 0 and m_end < c_end:
            return False

        # Las cantidades de misioneros y caníbales deben estar entre 0 y 3.
        if not (0 <= m_start <= 3 and 0 <= c_start <= 3 and 0 <= m_end <= 3 and 0 <= c_end <= 3):
            return False

        return True

    def get_successors(self, state):
        """
        Genera los estados sucesores a partir de un estado dado.

        Args:
            state (tuple): El estado actual.
                Formato: (misioneros_orilla_inicial, canibales_orilla_inicial, bote_orilla_inicial)

        Returns:
            list: Una lista de tuplas (next_state, action_description).
        """
        successors = []
        m_start, c_start, b_start = state
        m_end = 3 - m_start
        c_end = 3 - c_start

        # Definimos las posibles combinaciones de personas que pueden ir en el bote (1 o 2)
        # (misioneros en el bote, caníbales en el bote)
        moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

        # Si el bote está en la orilla de inicio (b_start = 0)
        if b_start == 0:
            for m_move, c_move in moves:
                # Verificamos si hay suficientes personas en la orilla de inicio para el movimiento
                if m_start >= m_move and c_start >= c_move:
                    next_m_start = m_start - m_move
                    next_c_start = c_start - c_move
                    next_m_end = m_end + m_move
                    next_c_end = c_end + c_move
                    next_state = (next_m_start, next_c_start, 1) # Bote se mueve a la orilla de destino
                    if self.is_valid_state(next_state):
                        action_description = f"Llevar {m_move} misionero(s) y {c_move} caníbal(es) a la orilla de destino."
                        successors.append((next_state, action_description))
        # Si el bote está en la orilla de destino (b_start = 1)
        else:
            for m_move, c_move in moves:
                # Verificamos si hay suficientes personas en la orilla de destino para el movimiento
                if m_end >= m_move and c_end >= c_move:
                    next_m_end = m_end - m_move
                    next_c_end = c_end - c_move
                    next_m_start = m_start + m_move
                    next_c_start = c_start + c_move
                    next_state = (next_m_start, next_c_start, 0) # Bote se mueve a la orilla de inicio
                    if self.is_valid_state(next_state):
                        action_description = f"Llevar {m_move} misionero(s) y {c_move} caníbal(es) de vuelta a la orilla de inicio."
                        successors.append((next_state, action_description))

        return successors

    def is_goal_state(self, state):
        """
        Verifica si el estado dado es el estado objetivo.

        Args:
            state (tuple): El estado a verificar.

        Returns:
            bool: True si el estado es el objetivo, False en caso contrario.
        """
        return state == self.goal_state

class Node:
    """
    Representa un nodo en el árbol de búsqueda.
    Contiene el estado, el nodo padre, la acción que llevó a este estado
    y la profundidad del nodo.
    """

    def __init__(self, state, parent=None, action=None):
        """
        Inicializa un nodo.

        Args:
            state (tuple): El estado representado por este nodo.
            parent (Node, optional): El nodo padre. Defaults to None.
            action (str, optional): La acción que llevó a este estado. Defaults to None.
        """
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = 0 if parent is None else parent.depth + 1

    def __eq__(self, other):
        """
        Compara dos nodos basándose en su estado.
        """
        return isinstance(other, Node) and self.state == other.state

    def __hash__(self):
        """
        Permite que los nodos sean utilizados en conjuntos (sets) y diccionarios.
        """
        return hash(self.state)

    def expand(self, problem):
        """
        Genera los nodos sucesores de este nodo.

        Args:
            problem (SearchProblem): La instancia del problema de búsqueda.

        Returns:
            list: Una lista de nodos sucesores.
        """
        successors = problem.get_successors(self.state)
        return [Node(state, self, action) for state, action in successors]

    def get_path(self):
        """
        Reconstruye el camino desde el nodo inicial hasta este nodo.

        Returns:
            list: Una lista de nodos que representan el camino.
        """
        path = []
        current = self
        while current:
            path.append(current)
            current = current.parent
        return path[::-1] # Invertimos para tener el camino desde el inicio

def bfs(problem):
    """
    Implementación de la Búsqueda en Anchura (BFS).

    Args:
        problem (SearchProblem): La instancia del problema de búsqueda.

    Returns:
        tuple: Una tupla (path, nodes_expanded) donde:
            path (list): La lista de nodos que conforman la solución.
            nodes_expanded (int): La cantidad de nodos expandidos.
            Si no se encuentra solución, retorna (None, nodes_expanded).
    """
    initial_node = Node(problem.initial_state)
    frontier = deque([initial_node]) # Usamos una cola para BFS
    explored = {initial_node.state} # Conjunto para almacenar los estados ya explorados
    nodes_expanded = 0

    while frontier:
        current_node = frontier.popleft() # Sacamos el primer nodo de la cola

        if problem.is_goal_state(current_node.state):
            return current_node.get_path(), nodes_expanded

        nodes_expanded += 1 # Contamos el nodo actual como expandido

        for child_node in current_node.expand(problem):
            if child_node.state not in explored:
                explored.add(child_node.state)
                frontier.append(child_node)

    return None, nodes_expanded # No se encontró solución

def dfs(problem):
    """
    Implementación de la Búsqueda en Profundidad (DFS).

    Args:
        problem (SearchProblem): La instancia del problema de búsqueda.

    Returns:
        tuple: Una tupla (path, nodes_expanded) donde:
            path (list): La lista de nodos que conforman la solución.
            nodes_expanded (int): La cantidad de nodos expandidos.
            Si no se encuentra solución, retorna (None, nodes_expanded).
    """
    initial_node = Node(problem.initial_state)
    frontier = [initial_node] # Usamos una pila (lista en Python) para DFS
    explored = {initial_node.state} # Conjunto para almacenar los estados ya explorados
    nodes_expanded = 0

    while frontier:
        current_node = frontier.pop() # Sacamos el último nodo de la pila

        if problem.is_goal_state(current_node.state):
            return current_node.get_path(), nodes_expanded

        nodes_expanded += 1 # Contamos el nodo actual como expandido

        # Para DFS, añadimos los sucesores al principio de la lista (pila)
        # Esto asegura que exploramos en profundidad.
        # Es importante invertir el orden de los sucesores si queremos
        # que la primera rama explorada sea la que aparece primero en el 'get_successors'.
        # Sin embargo, la lógica de DFS es explorar la primera rama disponible.
        # order_of_children = current_node.expand(problem) # Si queremos un orden específico
        for child_node in reversed(current_node.expand(problem)): # Invertimos para simular el orden de una pila
            if child_node.state not in explored:
                explored.add(child_node.state)
                frontier.append(child_node)

    return None, nodes_expanded # No se encontró solución

def print_solution(path):
    """
    Imprime el camino de solución de forma legible.

    Args:
        path (list): La lista de nodos que conforman la solución.
    """
    if not path:
        print("No se encontró solución.")
        return

    print("Camino de solución:")
    for i, node in enumerate(path):
        m_start, c_start, b_start = node.state
        m_end = 3 - m_start
        c_end = 3 - c_start
        boat_pos = "Inicio" if b_start == 0 else "Destino"
        print(f"Paso {i}: Misioneros Inicio: {m_start}, Caníbales Inicio: {c_start} | Misioneros Destino: {m_end}, Caníbales Destino: {c_end} (Bote en: {boat_pos})")
        if node.action:
            print(f"  Acción: {node.action}")

if __name__ == "__main__":
    problem = MissionariesCannibalsProblem()

    print("--- Resolviendo con BFS ---")
    bfs_path, bfs_nodes_expanded = bfs(problem)
    if bfs_path:
        print_solution(bfs_path)
    print(f"Nodos expandidos por BFS: {bfs_nodes_expanded}\n")

    print("--- Resolviendo con DFS ---")
    dfs_path, dfs_nodes_expanded = dfs(problem)
    if dfs_path:
        print_solution(dfs_path)
    print(f"Nodos expandidos por DFS: {dfs_nodes_expanded}\n")

    print("--- Comparación ---")
    if bfs_nodes_expanded < dfs_nodes_expanded:
        print("BFS expandió menos nodos que DFS.")
    elif dfs_nodes_expanded < bfs_nodes_expanded:
        print("DFS expandió menos nodos que BFS.")
    else:
        print("Ambos algoritmos expandieron la misma cantidad de nodos.")