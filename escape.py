import networkx as nx

# Define the graph
G = nx.Graph()
G.add_nodes_from(['bridge', 'engines', 'navigation', 'communication', 'oxygen', 'escape_module'])
G.add_weighted_edges_from([('bridge', 'engines', 1),
                           ('bridge', 'oxygen', 1),
                           ('engines', 'oxygen', 1),
                           ('engines', 'navigation', 1),
                           ('oxygen', 'communication', 1),
                           ('communication', 'navigation', 1),
                           ('navigation', 'escape_module', 1)])

# Define the desired path
desired_path = ['bridge', 'engines', 'oxygen', 'bridge', 'oxygen', 'communication', 'navigation', 'engines', 'navigation', 'escape_module']

# Print the passages in the desired path
for i in range(len(desired_path) - 1):
    print(f"{desired_path[i]} -> {desired_path[i + 1]}")
print("The spacecraft must visit all nodes in this order.🚀")