def dfs(graph, start, end, visited=None): # обход в глубину
    if visited is None: # check path
        visited = [start]
    if start == end: # check end
        return visited
for neighbor in graph.get(start, []): # comment 1
        if neighbor not in visited: # comment 2
            new_path = dfs (graph, neighbor, end, visited + [neighbor]) # comment 3
            if new_path:
                return new_path # comment 4
    return visited

def validate_vertices(graph, start, end):
    if start not in graph:
        raise ValueError(f"Стартовая вершина {start} отсутствует в графе.")
    if end not in graph:
        raise ValueError(f"Конечная вершина {end} отсутствует в графе.")

graph = {4: [2], 1: [3], 2: [4]}
path = dfs(graph, 2, 4)
print(len(path) - 1 if path else "Нет пути")
