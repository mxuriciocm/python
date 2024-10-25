from collections import deque, defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.capacity = {}

    def add_edge(self, u, v, w):
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.capacity[(u, v)] = w
        self.capacity[(v, u)] = 0

    def bfs(self, source, sink, parent):
        visited = [False] * self.V
        queue = deque([source])
        visited[source] = True

        while queue:
            u = queue.popleft()

            for v in self.graph[u]:
                if not visited[v] and self.capacity[(u, v)] > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
                    if v == sink:
                        return True
        return False

    def ford_fulkerson(self, source, sink):
        parent = [-1] * self.V
        max_flow = 0

        while self.bfs(source, sink, parent):
            path_flow = float("Inf")
            s = sink

            while s != source:
                path_flow = min(path_flow, self.capacity[(parent[s], s)])
                s = parent[s]

            max_flow += path_flow
            v = sink

            while v != source:
                u = parent[v]
                self.capacity[(u, v)] -= path_flow
                self.capacity[(v, u)] += path_flow
                v = parent[v]

        return max_flow

# A=0,B=1,C=2,D=3,E=4,F=5

g = Graph(6)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 10)
g.add_edge(1, 2, 2)
g.add_edge(1, 3, 4)
g.add_edge(1, 4, 8)
g.add_edge(2, 4, 9)
g.add_edge(3, 5, 10)
g.add_edge(4, 3, 6)
g.add_edge(4, 5, 10)

source = 0
sink = 5
max_flow = g.ford_fulkerson(source, sink)
print(f"El flujo máximo es: {max_flow}")