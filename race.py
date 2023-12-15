import heapq

def dijkstra(graph, start, end):
    heap = [(0, start)]
    weights = {start: 0}
    paths = {start: []}
    while heap:
        (cost, node) = heapq.heappop(heap)
        if node == end:
            return paths[node], weights[node]
        for edge, weight in graph[node]:
            old_cost = weights.get(edge, float('inf'))
            new_cost = weights[node] + weight
            if new_cost < old_cost:
                weights[edge] = new_cost
                paths[edge] = paths[node] + [edge]
                heapq.heappush(heap, (new_cost, edge))
    return []

graph = {
    'A': [('B', 2), ('C', -3)],
    'B': [('C', 3), ('D', -2)],
    'C': [('B', -4), ('D', -3)],
    'D': [('A', -4)]
}

path, cost = dijkstra(graph, 'A', 'D')
print(' -> '.join(path), ":", cost)
