# from GCD import gcd
from Graph import GraphClass

if __name__ == '__main__':
    num_vertices = 4
    graph = GraphClass.Graph(num_vertices)

    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)

    graph.print_adjacency_list()

    # gcd.gcd(a=18925, b=12450)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
