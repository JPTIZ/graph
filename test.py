from graph import Graph


graph = Graph()
graph.add("Olegário")
graph.add("Tiz")
graph.add("Amigo do tiz")
graph.link("Tiz", "Amigo do tiz")
graph.link("Amigo do tiz", "Tiz")
graph.link("Tiz", "Olegário")
graph.link("Olegário", "Tiz")

#
graph.unlink("Tiz", "Amigo do tiz")
graph.unlink("Amigo do tiz", "Tiz")

print(graph.vertices())
print(graph.order())
print(graph["Olegário"].neighbours)
print(graph["Tiz"].neighbours)
print(graph.random_vertex())
