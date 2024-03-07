class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adjacency_list = {}
        # loop iterate each vertex
        for i in range(num_vertices):
            self.adjacency_list[i] = []

    def add_edge(self, source, destination):
        self.adjacency_list[source].append(destination)
        self.adjacency_list[destination].append(source)

    def print_adjacency_list(self):
        for vertex in self.adjacency_list:
            print(f"Vertex {vertex}: {' -> '.join(map(str, self.adjacency_list[vertex]))}")
