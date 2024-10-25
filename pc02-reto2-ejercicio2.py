import heapq

def prim(graph, start):
    mst = []
    visited = set()
    min_heap = [(0, start)]  

    while min_heap:
        weight, u = heapq.heappop(min_heap)
        if u not in visited:
            visited.add(u)
            mst.append((u, weight))

            for v, w in graph[u]:
                if v not in visited:
                    heapq.heappush(min_heap, (w, v))

    return mst

graph = {
    0: [(1, 7), (2, 8)],
    1: [(0, 7), (2, 3), (3, 6)],
    2: [(0, 8), (1, 3), (3, 4), (4, 2)],
    3: [(1, 6), (2, 4), (4, 5), (5, 1)],
    4: [(2, 2), (3, 5), (5, 4)],
    5: [(3, 1), (4, 4)]
}
mst = prim(graph, 0)
print("Nodos y sus pesos correspondientes en el MST:")
for node, weight in mst:
    print(f"Nodo {node}, Peso {weight}")