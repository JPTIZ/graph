from random import random


class Vertex:
    def __init__(self):
        self.neighbours = []

    def degree(self):
        return len(self.neighbours)


class Graph:
    def __init__(self):
        self.data = {}

    # Operações básicas

    def add(self, v):
        self.data[v] = Vertex()

    def remove(self, v):
        del self.data[v]

    def link(self, v1, v2):
        self.data[v1].neighbours.append(v2)

    def unlink(self, v1, v2):
        self.data[v1].neighbours.remove(v2)

    def order(self):
        return len(self.data)

    def vertices(self):
        return self.data.keys()

    def random_vertex(self):
        return self.data[int(random() * len(self.data))]

    def __getitem__(self, key):
        return self.data[key]

    # Ações derivadas

    def regular(self):
        pass

    def complete(self):
        pass

    def transitive_closure(self):
        pass

    def connected(self):
        pass

    def tree(self):
        pass


