import time
import random
from collections import deque

# Функция для генерации графа в виде списков смежности
def generate_graph(num_nodes, edge_probability=0.1):
    graph = [[] for _ in range(num_nodes)]
    for i in range(num_nodes):
        for j in range(i+1, num_nodes):
            if random.random() < edge_probability:
                graph[i].append(j)
                graph[j].append(i)
    return graph

# Реализация BFS
def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            # Можно добавить любую обработку узла
            queue.extend([neighbor for neighbor in graph[node] if neighbor not in visited])
    return visited

# Основная функция для измерения времени BFS
def measure_bfs_time(graph, start_node=0):
    start_time = time.perf_counter()
    bfs(graph, start_node)
    end_time = time.perf_counter()
    return end_time - start_time

# Пример использования
num_nodes = 50
graph = generate_graph(num_nodes, edge_probability=0.05)

elapsed_time_bfs = measure_bfs_time(graph)
print(f"BFS выполнен за {elapsed_time_bfs:.6f} секунд")