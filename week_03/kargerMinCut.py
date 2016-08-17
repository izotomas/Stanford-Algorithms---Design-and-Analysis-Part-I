from numpy.random import choice, seed
import copy


def read_graph(filename):
    f = open(filename, 'r')
    graph = {}
    for line in f.readlines():
        line = line.split('\t')
        graph[int(line[0])] = [int(i) for i in line[1:-1]]
    f.close()
    return graph


def drop_dups(graph, node):
    while node in graph[node]:
        graph[node].remove(node)


def karger(graph):
    while len(graph) > 2:
        node1 = choice(list(graph.keys()))
        node2 = choice(graph[node1])
        edges = graph[node2]
        graph[node1].extend(edges)
        temp = []
        for node in edges:
            temp = graph[node]
            for i in range(len(temp)):
                if temp[i] == node2:
                    temp[i] = node1
            graph[node] = temp
        drop_dups(graph, node1)
        graph.pop(node2)
    return len(graph[list(graph.keys())[0]])


if __name__ == "__main__":
    graph = read_graph('dat.txt')
    min_cut = karger(copy.deepcopy(graph))
    for i in range(100):
        seed()
        x = karger(copy.deepcopy(graph))
        if x < min_cut:
            min_cut = x
    print(min_cut)
