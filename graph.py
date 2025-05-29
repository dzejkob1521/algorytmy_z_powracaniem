class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.a_list = [[] for _ in range(nodes)]

    def add_edge(self, u, v):
        if u < 0 or u >= self.nodes or v < 0 or v >= self.nodes:
            raise ValueError("Nieprawidłowe wierzchołki.")
        if v not in self.a_list[u]:
            self.a_list[u].append(v)

    def edge_exists(self, u, v):
        return v in self.a_list[u]

    def print_graph(self):
        for i, neighbors in enumerate(self.a_list):
            print(f"{i+1}: {' '.join(str(j+1) for j in neighbors)}")



