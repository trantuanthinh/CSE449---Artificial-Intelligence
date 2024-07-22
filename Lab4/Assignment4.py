from collections import deque


def dfs(graph, start):
    visited = set()
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            stack.extend(
                [neighbor for neighbor in graph[vertex] if neighbor not in visited]
            )


def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            queue.extend(
                [neighbor for neighbor in graph[vertex] if neighbor not in visited]
            )


class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, from_node, to_node):
        if from_node in self.graph:
            self.graph[from_node].append(to_node)
        else:
            self.graph[from_node] = [to_node]

    def display_graph(self):
        for node, edges in self.graph.items():
            print(f"{node} -> {', '.join(edges)}")


graph = Graph()

graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_node("D")

graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "C")
graph.add_edge("B", "D")
graph.add_edge("C", "D")
graph.add_edge("D", "A")

graph.display_graph()

start_vertex = "D"
print(f"\nDFS Traversal starting from vertex '{start_vertex}':")
dfs(graph.graph, start_vertex)

print(f"\nBFS Traversal starting from vertex '{start_vertex}':")
bfs(graph.graph, start_vertex)
