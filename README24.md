# Practica 3: BF & DFS Sin terminación

## Profesor : Mauricio Riva Palacio Orozco
## Ayudantes:
- Adrián Felipe Fernández Romero
- Alan Alexis Martínez López
<p>

### Alumnos
Blancas Ochoa Alan -316227364 Carbajal Galicia Hilda Joana -318087223 Fuentes Ortega Diego Tonatiuh -320067660

## Tabla de Contenidos
- [1. Introducción](#1-introducción)
- [2. Uso](#2-uso)
- [3. Estructura de la práctica](#3-estructura)
- [4. Explicación de la implementación](#4-implementacion)

## **1. Introducción**
En esta práctica implementamoas los algortimos dfs y bfs en sus versiones que no detectan terminacion usando de guía el pseudocódigo que se nos dío en la carpeta práctica 3.

## **2.Uso**
- Generamos el entorno virtual

```bash
python3 -m venv venv
```
- Activamos el entorno:
```bash
 source venv/bin/activate
```
- Paquetes:
```bash
pip install -r requirements.txt
```
- Ejecutar Tests con:
```bash
pytest Test.py
```
## **3. Estructura**
En una terminal: 
```bash
tree -I 'node_modules|cache|test_*|__pycache__|.pytest_cache|venv'
```
```
├── Canales
│   ├── Canal.py
│   └── CanalRecorridos.py
├── NodoBFS.py
├── NodoDFS.py
├── Nodo.py
├── README.md
├── requirements.txt
└── Test.py
```

## **4. Implementación**
El proyecto simula los algoritmos BFS y DFS distribuidos utilizando la librería SimPy, que permite modelar sistemas concurrentes mediante procesos y eventos discretos.

- Clases principales

1. Nodo.py 

Define la clase base Nodo, representa un nodo genérico con:

- id_nodo: identificador único del nodo.

- vecinos: lista de nodos conectados directamente.

- canal_entrada y canal_salida: objetos simpy.Store usados para la comunicación.
La clase incluye únicamente getters para acceder a sus atributos.

2. NodoBFS.py
Implementa la clase NodoBFS, que extiende a Nodo y ejecuta el algoritmo Breadth-First Search distribuido (BFS).
El nodo raíz (id = 0) inicia enviando mensajes "GO" a sus vecinos.
Cada nodo, al recibir "GO", define su padre, su nivel y reenvía el mensaje a sus vecinos no visitados.
Cuando todos los mensajes de respuesta "BACK" han llegado, el nodo raíz detecta que el árbol BFS se ha construido completamente.

3. NodoDFS.py
Implementa la clase NodoDFS, heredada de Nodo, que simula el algoritmo Depth-First Search distribuido (DFS).
El nodo raíz comienza enviando "GO" a un vecino (siguiendo la convención de elegir el de menor id).
Los nodos registran los visitados, envían "GO" a vecinos no visitados y responden con "BACK" cuando completan su recorrido.
El proceso termina cuando el nodo raíz ha recibido todas las respuestas y no quedan vecinos por explorar.

4. Canales/CanalRecorridos.py
Define la clase CanalRecorridos, derivada de Canal.
Se encarga de la comunicación one-to-many, permitiendo que un nodo envíe mensajes a múltiples vecinos mediante:
- envia(mensaje, vecinos): distribuye el mensaje a todos los canales de entrada correspondientes.
- crea_canal_de_entrada(): crea un canal de entrada para cada nodo.
Internamente utiliza simpy.Store para almacenar los mensajes enviados en el entorno de simulación.

Flujo de ejecución

- Se inicializa el entorno de simulación con env = simpy.Environment().

- Se crean los canales de comunicación y los nodos con sus conexiones.

- Se ejecuta el proceso bfs(env) o dfs(env) según el algoritmo deseado.

- Los nodos se comunican mediante los mensajes "GO" y "BACK", simulando el comportamiento distribuido del algoritmo.

- Cuando el nodo raíz recibe todas las confirmaciones, el recorrido (BFS o DFS) se considera finalizado.