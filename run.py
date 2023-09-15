from dijkstra import Dijkstra
from graph import Graph

graph_representation = {"A": {("B", 1), ("C", 2)}, "B": {("D", 4)}, "C": {("D", 1)}}
graph = Graph(graph_representation, True)
graph.draw()

dijkstra = Dijkstra(graph)
print(dijkstra.get_shortest_path("E", "E"))
dijkstra.draw("A")
dijkstra.draw("D")