def find_eulerian_cycle(graph):
    odd_vertices = []
    for i, neighbors in enumerate(graph.a_list):
        if len(neighbors) % 2 != 0:
            odd_vertices.append(i + 1) 
    
    if odd_vertices:
        print(f"Graf nie ma cyklu Eulera. Wierzchołki o nieparzystym stopniu: {odd_vertices}")
        return
    total_edges = sum(len(neighbors) for neighbors in graph.a_list) // 2
    if total_edges == 0:
        print("Graf nie ma krawędzi.")
        return
    start_vertex = -1
    for i, neighbors in enumerate(graph.a_list):
        if neighbors:
            start_vertex = i
            break
    
    if start_vertex == -1:
        print("Brak wierzchołków z krawędziami.")
        return

    temp_graph = [neighbors.copy() for neighbors in graph.a_list]
    stack = [start_vertex]
    path = []
    
    while stack:
        v = stack[-1]
        if temp_graph[v]: 
            u = temp_graph[v].pop()  
            if v in temp_graph[u]:
                temp_graph[u].remove(v)
            
            stack.append(u)
        else:
            path.append(stack.pop())
    
    remaining_edges = sum(len(neighbors) for neighbors in temp_graph)
    if remaining_edges > 0:
        print("Graf nie jest spójny - nie można znaleźć cyklu Eulera.")
        return
    
    path = path[::-1]

    print("Cykl Eulera:")
    cycle_display = " -> ".join(str(p + 1) for p in path)
    
    
    if len(path) > 1:
        if path[0] == path[-1]:
            print(f"Znaleziono cykl Eulera")
            print(cycle_display)
        else:
            print(f"Nie znaleziono cyklu Eulera")


def find_hamiltonian_cycle(graph):
    n = graph.nodes
    path = []

    def backtrack(v, visited):
        if len(path) == n:
            if path[0] in graph.a_list[path[-1]]:
                path.append(path[0])
                return True
            return False

        for neighbor in graph.a_list[v]:
            if neighbor not in visited:
                visited.add(neighbor)
                path.append(neighbor)
                if backtrack(neighbor, visited):
                    return True
                visited.remove(neighbor)
                path.pop()
        return False

    for start in range(n):
        path = [start]
        if backtrack(start, {start}):
            print("Cykl Hamiltona:")
            print(" -> ".join(str(p + 1) for p in path))
            return
    print("Brak cyklu Hamiltona.")
