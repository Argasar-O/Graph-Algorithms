from Graph.graph import Graph


class Dijkstra:
    __saveBySource: dict[str, dict]

    def __init__(self, graph: Graph):
        self.__dist = None
        self.__prev = None
        self.graph = graph
        self.__saveBySource = {}

    def __run_algorithm(self, source: str):
        if source not in self.__saveBySource:
            self.__initialization(source)
            not_passed_node = list(self.graph.nodes.keys())
            while len(not_passed_node) > 0:
                node1 = self.find_min(not_passed_node)
                if node1 is None:
                    break
                del not_passed_node[not_passed_node.index(node1)]
                for node2 in self.graph.get_node(node1).get_neighbor():
                    self.__update_dist(node1, node2)
            self.__saveBySource[source] = {"dist": self.__dist, "prev": self.__prev}
        else:
            self.__dist = self.__saveBySource[source]["dist"]
            self.__prev = self.__saveBySource[source]["prev"]

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

    def find_min(self, not_passed_node: [str]) -> str:
        mini = float("inf")
        node = None
        for test_node in not_passed_node:
            if self.__dist[test_node] < mini:
                mini = self.__dist[test_node]
                node = test_node
        return node

    def draw(self, source: str):
        self.__run_algorithm(source)
        print(self.__dist)
        return self.__dist, self.__prev

    def __update_dist(self, node1: str, node2: str):
        cost = self.graph.get_cost(node1, node2)
        if self.__dist[node2] > self.__dist[node1] + cost:
            self.__dist[node2] = self.__dist[node1] + cost
            self.__prev[node2] = node1
