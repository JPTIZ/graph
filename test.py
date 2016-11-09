from graph import Graph


def keys(set_):
    keys_ = set()
    for v in set_:
        keys_.add(v.key)
    return keys_


def test(f):
    print('Result ({}): {}'.format(f.__name__, f()))


def test_neighbours():
    graph = Graph()
    graph.add('Olegário')
    graph.add('Tiz')
    graph.add('Amigo do tiz')

    if len(graph.vertices) != 3: return False

    graph.link('Tiz', 'Amigo do tiz')
    graph.link('Tiz', 'Olegário')


    # ------------------------------------------------------

    graph.unlink('Tiz', 'Amigo do tiz')
    graph.unlink('Amigo do tiz', 'Tiz')

    # ------------------------------------------------------

    if set(graph.vertices) != {'Olegário', 'Tiz', 'Amigo do tiz'}: return False
    if keys(graph['Olegário'].neighbours) != {'Tiz'}: return False
    if keys(graph['Tiz'].neighbours) != {'Olegário'}: return False
    if not graph.random_vertex() in graph.vertices.values(): return False

    graph.remove('Amigo do tiz')

    if graph.order() != 2: return False

    return True


def test_regular():
    graph = Graph()

    graph.add(0)
    graph.add(1)
    graph.add(2)

    graph.link(0, 1)
    graph.link(0, 2)

    if graph.regular(): return False 

    graph.link(1, 2)

    return graph.regular()


def test_complete():
    graph = Graph()

    graph.add(0)
    graph.add(1)
    graph.add(2)
    graph.add(3)

    if graph.complete(): return False

    graph.link(0, 1)

    if graph.complete(): return False

    graph.link(0, 2)
    graph.link(0, 3)

    graph.link(1, 2)

    graph.link(2, 3)

    if graph.complete(): return False

    graph.link(1, 3)

    return graph.complete()


def test_transitive_closure():
    graph = Graph()

    graph.add(0)
    graph.add(1)
    graph.add(2)
    graph.add(3)
    graph.add(4)
    graph.add(5)

    if len(graph.transitive_closure(0)) > 1: return False

    graph.link(0, 1)

    if (len(keys(graph.transitive_closure(0)) ^ { 0, 1 }) > 0): return False

    graph.link(2, 3)

    if (len(keys(graph.transitive_closure(2)) ^ { 2, 3 }) > 0): return False

    graph.link(1, 2)

    if (len(keys(graph.transitive_closure(2)) ^ { 0, 1, 2, 3 }) > 0): return False
    if (len(keys(graph.transitive_closure(5)) ^ { 5 }) > 0): return False

    graph.link(4, 4)

    if (len(keys(graph.transitive_closure(4)) ^ { 4 }) > 0): return False

    graph.link(4, 5)

    if (len(keys(graph.transitive_closure(4)) ^ { 4, 5 }) > 0): return False

    return True


def test_connected():
    graph = Graph()

    graph.add(0)
    graph.add(1)
    graph.add(2)
    graph.add(3)
    graph.add(4)
    graph.add(5)

    if graph.connected(): return False

    graph.link(0, 1)

    if graph.connected(): return False

    graph.link(2, 3)
    graph.link(1, 2)
    graph.link(4, 4)
    graph.link(4, 5)

    if graph.connected(): return False

    graph.link(0, 4)

    if not graph.connected(): return False

    return True

def test_tree():
    graph = Graph()

    graph.add(0)
    graph.add(1)
    graph.add(2)
    graph.add(3)
    graph.add(4)
    graph.add(5)

    if graph.tree(): return False

    graph.link(0, 1)
    graph.link(0, 2)
    graph.link(3, 4)
    graph.link(4, 5)

    if graph.tree(): return False

    graph.link(0, 5)

    if not graph.tree(): return False

    graph.link(2, 3)

    if graph.tree(): return False

    graph.unlink(2, 3)
    graph.link(1, 2)

    if graph.tree(): return False

    return True

test(test_neighbours)
test(test_regular)
test(test_complete)
test(test_transitive_closure)
test(test_connected)
test(test_tree)
