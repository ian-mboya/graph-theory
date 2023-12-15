import heapq

class Network:
    def __init__(self):
        self.graph = {}
        self.times = {}
        self.visited = set()

    def add_edge(self, node1, node2, time):
        if node1 not in self.graph:
            self.graph[node1] = []
        if node2 not in self.graph:
            self.graph[node2] = []
        self.graph[node1].append((node2, time))
        self.graph[node2].append((node1, time))

    def dijkstra(self, start):
        heap = [(0, start)]
        while heap:
            (current_time, current_node) = heapq.heappop(heap)
            if current_node not in self.visited:
                self.visited.add(current_node)
                self.times[current_node] = current_time
                for (next_node, next_time) in self.graph[current_node]:
                    heapq.heappush(heap, (current_time + next_time, next_node))

    def message_delivery_time(self, start):
        self.dijkstra(start)
        return self.times

if __name__ == "__main__":
    network = Network()

    # Input data
    data = [
        "You - Honza: 3",
        "You - Pepa: 2",
        "Honza - Tomas: 4",
        "Honza - Anna: 4",
        "Pepa - Anna: 1",
        "Pepa - Michal: 2",
        "Tomas - Ondra: 5",
        "Anna - Ondra: 2",
        "Anna - Jirka: 4",
        "Michal - Jirka: 2",
        "Ondra - Jirka: 2"
    ]

    for line in data:
        parts = line.split(':')
        users, time = parts[0].split('-'), int(parts[1].strip())
        network.add_edge(users[0].strip(), users[1].strip(), time)

    start_user = "You"
    delivery_times = network.message_delivery_time(start_user)

    # Output
    sorted_users = sorted(delivery_times.items(), key=lambda x: x[1])
    for user, time in sorted_users:
        print(f"{user}: {time}")
