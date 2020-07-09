'''Defines graph structures.'''
import random
from typing import Set, TypeVar


K = TypeVar('K')


class Vertex:
    '''A graph's vertex.'''
    def __init__(self, key: K):
        self.key = key
        self.neighbours = set()

    def degree(self) -> int:
        '''Returns the vertex's degree.'''
        return len(self.neighbours)


class Graph:
    '''The graph itself.'''
    def __init__(self):
        self.vertices = {}

    # Basic operations

    def add(self, v: Vertex):
        '''Adds a vertex to the graph.

        Args:
            v: Vertex to be add.
        '''
        self.vertices[v] = Vertex(v)

    def remove(self, v: Vertex):
        '''Removes a vertex from the graph.

        Args:
            v: Vertex to be removed.
        '''
        del self.vertices[v]

    def link(self, v1: Vertex, v2: Vertex):
        '''Links two vertices by a bidirectional edge.

        Args:
            v1: First vertex.
            v2: Second vertex.
        '''
        self.vertices[v1].neighbours.add(self.vertices[v2])
        self.vertices[v2].neighbours.add(self.vertices[v1])

    def unlink(self, v1: Vertex, v2: Vertex):
        '''Unlinks two vertices.

        Args:
            v1: First vertex.
            v2: Second vertex.
        '''
        self.vertices[v1].neighbours.discard(self.vertices[v2])
        self.vertices[v2].neighbours.discard(self.vertices[v1])

    def order(self) -> int:
        '''Graph's order.'''
        return len(self.vertices)

    def random_vertex(self) -> Vertex:
        '''Gets a random vertex from the graph.'''
        return random.choice(list(self.vertices.values()))

    def neighbours(self, key: K) -> Set[Vertex]:
        '''Gets a set with a vertex's neighbours.

        Args:
            key: The vertex.
        '''
        return self.vertices[key].neighbours

    def degree(self, key: K) -> int:
        '''Gets a vertex's degree.

        Args:
            key: The vertex.
        '''
        return self.vertices[key].degree()

    # Derived actions

    def regular(self) -> bool:
        '''Checks if the graph is regular.'''
        common_degree = len(self.random_vertex().neighbours)

        for v in self.vertices.values():
            if v.degree() != common_degree:
                return False

        return True

    def complete(self) -> bool:
        '''Checks if the graph is complete.'''
        for _, v in self.vertices.items():
            for _, other_v in self.vertices.items():
                if v != other_v and other_v not in v.neighbours:
                    return False

        return True

    def transitive_closure(self, key: K) -> Set[Vertex]:
        '''Gets the transitive closure starting from the given key.

        Args:
            key: Reference vertex.
        '''
        if isinstance(key, Vertex):
            v = key
        else:
            v = self.vertices[key]
        visited = set()
        return search_transitive_closure(v, visited)

    def connected(self) -> bool:
        '''Checks if the graph is connected. An empty graph is considered
        disconnected.'''
        if not self.vertices:
            return false

        trans = self.transitive_closure(self.vertices[0])
        values = set(self.vertices.values())
        return len(trans ^ values) == 0

    def tree(self) -> bool:
        '''Checks if the graph is a tree.'''
        return self.connected() and not self.has_cycle()

    def has_cycle(self,
            v: Vertex = None,
            prev: Vertex = None,
            visited: Set[Vertex] = None):
        '''Check if the graph has a cycle.

        Args:
            v: Vertex to be checked against visited set.
                        If None, begins searching recursively for a cycle.
            prev: Reference vertex.
            visited: Set of already visited vertices.
        '''
        if v is None:
            v = self.vertices[0]
            return self.has_cycle(v, v, set())

        if v in visited:
            return True

        visited.add(v)
        for v_ in v.neighbours:
            if v_ != prev and self.has_cycle(v_, v, visited):
                return True
        visited.remove(v)

        return False

    # Extra

    def __getitem__(self, key: K) -> Vertex:
        '''Overrides operator [] to get a vertex by a given key.

        Args:
            key: The vertex's key.
        '''
        return self.vertices[key]


def search_transitive_closure(v: Vertex, visited: Set[Vertex]) -> Set[Vertex]:
    '''Searchs for a transitive closure.

    Args:
        v: Reference vertex.
        visited: Already visited vertices.
    '''
    visited.add(v)
    for v_ in v.neighbours:
        if not v_ in visited:
            search_transitive_closure(v_, visited)

    return visited
