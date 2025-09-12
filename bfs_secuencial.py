# Computación Distribuida 2024-1
# Práctica 1: BFS Secuencial
# Profesor: Mauricio Riva Palacio Orozco
# Ayudantes: Adrián Felipe Fernández Romero y Alan Alexis Martínez López
# Alumnos: 
# Carbajal Galicia Hilda Joana -318087223
# Fuentes Ortega Diego Tonatiuh -320067660
# Blancas Ochoa Alan -316227364

from collections import deque

def bfs_secuencial(arbol, nodo_inicial):
    """
    Implementación del algoritmo Breadth-First Search (BFS) para recorrer un árbol.

    Parámetros:
    -----------
    arbol : dict
        Representación del árbol como un diccionario de listas de adyacencia.
        Ejemplo:
        {
            'A': ['B', 'C'],
            'B': ['D', 'E'],
            'C': ['F'],
            'D': [],
            'E': [],
            'F': []
        }

    nodo_inicial : str
        Nodo desde el cual inicia el recorrido BFS.

    Retorna:
    --------
    list
        Lista con los nodos visitados en orden BFS.
    """

    visitados = []          # Lista de nodos visitados en orden BFS
    cola = deque([nodo_inicial])  # Cola para manejar los nodos por visitar

    while cola:
        nodo = cola.popleft()   # Sacamos el primer nodo de la cola

        if nodo not in visitados:  # Solo visitamos si aún no lo hemos hecho
            visitados.append(nodo)  # Marcamos como visitado
            cola.extend(arbol[nodo])  # Agregamos los vecinos del nodo a la cola

    return visitados


# Ejemplo de uso:
if __name__ == "__main__":
    # Definimos un árbol como diccionario de listas de adyacencia
    arbol = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': [],
        'F': []
    }

    recorrido = bfs_secuencial(arbol, 'A')
    print("Recorrido BFS:", recorrido)
    # Salida esperada: ['A', 'B', 'C', 'D', 'E', 'F']
