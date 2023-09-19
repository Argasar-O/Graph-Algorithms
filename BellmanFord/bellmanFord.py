from Graph.graph import Graph


class BellmanFord:
    __saveBySource: dict[str, dict]

    def __init__(self, graph: Graph):
        self.__dist = None
        self.__prev = None
        self.graph = graph
        self.__saveBySource = {}

    def __run_algorithm(self, source: str):
        self.__initialization(source)
        edges = self.graph.get_edges()
        for i in range(1, len(self.graph.nodes)-1):
            for edge in edges:
                if self.__dist[edge[0]] + edge[2] < self.__dist[edge[1]]:
                    self.__dist[edge[1]] = self.__dist[edge[0]] + edge[2]
                    self.__prev[edge[1]] = edge[0]

        # Find negative loop
        for edge in edges:
            edge1 = edge[0]
            edge2 = edge[1]
            if self.__dist[edge1] + edge[2] < self.__dist[edge2]:
                self.__prev[edge2] = edge1
                visited = [False] * len(self.graph.nodes)
                visited[edge2] = True
                while not visited[edge1]:
                    visited[edge1] = True
                    edge1 = self.__prev[edge1]
                cycle = [edge1]
                edge2 = self.__prev[edge1]
                while edge2 != edge1:
                    cycle.append(edge2)
                    edge2 = self.__prev[edge2]
                print("Graph have a negative loop : " + str(cycle))

    def get_shortest_path(self, node1: str, node2: str):
        self.__run_algorithm(node1)
        result = []
        temp_node = node2
        try:
            if self.__dist[node2] == float("inf"):
                print("No path possible")
            else:
                while temp_node != node1:
                    result.insert(0, temp_node)
                    temp_node = self.__prev[temp_node]
                result.insert(0, node1)
        except ValueError:
            print("Not result found")
        finally:
            return result

    def __initialization(self, source: str):
        self.__dist = {}
        self.__prev = {}
        for node in self.graph.nodes:
            self.__dist[node] = float("inf") if node != source else 0
            self.__prev[node] = None

    def draw(self, source: str):
        self.__run_algorithm(source)
        print(self.__dist)
        return self.__dist, self.__prev
