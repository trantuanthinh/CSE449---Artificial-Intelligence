from collections import deque


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=" ")
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)


# Example graph represented as an adjacency list
graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": ["F"], "F": []}

print("DFS:")
dfs(graph, "A")
print("\nBFS:")
bfs(graph, "A")
