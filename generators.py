import random
import sys
from graph import Graph

def create_hamiltonian_graph(nodes, saturation):
    if nodes <= 10:
        print("Liczba wierzchołków musi być większa niż 10 dla grafu Hamiltona.")
        sys.exit(1)
    graph = Graph(nodes)
    cycle = list(range(nodes))
    random.shuffle(cycle)
    for i in range(nodes):
        u, v = cycle[i], cycle[(i + 1) % nodes]
        graph.add_edge(u, v)
        graph.add_edge(v, u)
    max_edges = nodes * (nodes - 1) // 2
    desired_edges = int(saturation * max_edges / 100)
    edges = set()
    for u in range(nodes):
        for v in graph.a_list[u]:
            if u < v:
                edges.add((u, v))
    degrees = [len(graph.a_list[i]) for i in range(nodes)]

    all_possible = [(i, j) for i in range(nodes) for j in range(i+1, nodes)
                    if not graph.edge_exists(i, j)]
    random.shuffle(all_possible)

    while len(edges) < desired_edges:
        u, v, w = random.sample(range(nodes), 3)
        if (not graph.edge_exists(u, v) and
            not graph.edge_exists(v, w) and
            not graph.edge_exists(w, u)):
            graph.add_edge(u, v)
            graph.add_edge(v, w)
            graph.add_edge(w, u)
            graph.add_edge(v, u)
            graph.add_edge(w, v)
            graph.add_edge(u, w)
            edges.add((min(u, v), max(u, v)))
            edges.add((min(v, w), max(v, w)))
            edges.add((min(w, u), max(w, u)))
            degrees[u] += 2
            degrees[v] += 2
            degrees[w] += 2
    odd_vertices = [i for i in range(nodes) if degrees[i] % 2 != 0]

    while len(odd_vertices) >= 2:
        u = odd_vertices.pop()
        for i, v in enumerate(odd_vertices):
            if not graph.edge_exists(u, v):
                graph.add_edge(u, v)
                graph.add_edge(v, u)
                degrees[u] += 1
                degrees[v] += 1
                edges.add((min(u, v), max(u, v)))
                odd_vertices.pop(i)
                break

    return graph



def create_non_hamiltonian_graph(nodes):
    if nodes <= 1:
        print("Liczba wierzchołków musi być większa niż 1.")
        sys.exit(1)

    graph = Graph(nodes)
    max_edges = nodes * (nodes - 1) // 2
    desired_edges = max_edges * 50 // 100

    edges = [(i, j) for i in range(nodes) for j in range(i + 1, nodes)]
    random.shuffle(edges)

    added = 0
    for u, v in edges:
        if added >= desired_edges:
            break
        graph.add_edge(u, v)
        graph.add_edge(v, u)
        added += 1

    isolated = random.randint(0, nodes - 1)
    graph.a_list[isolated] = []
    for i in range(nodes):
        if isolated in graph.a_list[i]:
            graph.a_list[i].remove(isolated)

    return graph
