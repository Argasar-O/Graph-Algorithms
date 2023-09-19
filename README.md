# Graph

## Create Graph
Usage: 
```
graph_representation = {"A": {("B", 1), ("C", 2)}, "B": {("D", 4)}, "C": {("D", 1)}}
graph = Graph(graph_representation: dict[str, set[tuple[str, float]]], is_oriented: bool)
```

## Shortest path problem
### Dijkstra algorithm
```
dijkstra = Dijkstra(graph: Graph)
print(dijkstra.get_shortest_path("A": str (source), "D": str (Dest)))
dijkstra.draw("A")
```

### Bellman-Ford algorithm
```
bellman_ford = BellmanFord(graph: Graph)
print(bellman_ford.get_shortest_path("A": str (source), "D": str (Dest)))
bellman_ford.draw("A")
```