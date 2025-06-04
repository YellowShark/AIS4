def dfs(graph, start, end, visited=None):
    if visited is None:
        visited = [start]
    if start == end:
        return visited
    for neighbor in graph.get(start, []): # comment 1
        if neighbor not in visited: # comment 2
            new_path = dfs (graph, neighbor, end, visited + [neighbor]) # comment 3
            if new_path:
                return new_path # comment 4
    return visited

graph = {4: [2], 1: [3], 2: [4]}
path = dfs(graph, 2, 4)
print(len(path) - 1 if path else "Нет пути")