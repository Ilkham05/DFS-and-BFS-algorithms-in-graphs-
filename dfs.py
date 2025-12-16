import time
import random

# Функция для генерации графа в виде списков смежности
def generate_graph(num_nodes, edge_probability=0.1):
    graph = [[] for _ in range(num_nodes)]
    for i in range(num_nodes):
        for j in range(i+1, num_nodes):
            if random.random() < edge_probability:
                graph[i].append(j)
                graph[j].append(i)
    return graph

# Реализация DFS
def dfs(graph, start_node):
    visited = set()
    stack = [start_node]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            # Можно добавить любую обработку узла
            stack.extend([neighbor for neighbor in graph[node] if neighbor not in visited])
    return visited

# Основная функция для измерения времени
def measure_dfs_time(graph, start_node=0):
    start_time = time.perf_counter()
    dfs(graph, start_node)
    end_time = time.perf_counter()
    return end_time - start_time

# Пример использования
num_nodes = 1000
graph = generate_graph(num_nodes, edge_probability=0.05)
elapsed_time = measure_dfs_time(graph)
print(f"DFS выполнен за {elapsed_time:.6f} секунд")