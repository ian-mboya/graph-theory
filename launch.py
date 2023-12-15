class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal_mst(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        return result

nodes = {"engines": 0, "navigation": 1, "communication": 2, "bridge": 3, "oxygen": 4}
edges = [("engines", "oxygen", 15), ("navigation", "communication", 90), ("bridge", "oxygen", 20),
         ("engines", "navigation", 50), ("communication", "bridge", 35), ("oxygen", "communication", 15)]

g = Graph(len(nodes))
for edge in edges:
    u, v, w = edge
    g.add_edge(nodes[u], nodes[v], w)

mst = g.kruskal_mst()

for u, v, weight in mst:
    print(list(nodes.keys())[list(nodes.values()).index(u)], "-", list(nodes.keys())[list(nodes.values()).index(v)])
