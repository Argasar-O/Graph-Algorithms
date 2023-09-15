class Node:
    __links: set[tuple[str, float]]

    def __init__(self, _id: str):
        self.__id = _id
        self.__links = {(_id, 0)}

    def get_id(self):
        return self.__id

    def add_link(self, node: str, cost: float):
        self.__links.add((node, cost))

    def get_links_sorted(self):
        return sorted(self.__links, key=lambda x: x[1])

    def get_neighbor(self):
        return map(lambda x: x[0], self.__links)


class Graph:
    def __init__(self, graph_representation: dict[str, set[tuple[str, float]]], is_oriented: bool):
        self.nodes: dict[str, Node] = dict()
        for key in graph_representation:
            if key not in self.nodes:
                self.nodes[key] = Node(key)
            for link in graph_representation[key]:
                self.nodes[key].add_link(link[0], link[1])
                if not is_oriented:
                    if link[0] not in self.nodes:
                        self.nodes[link[0]] = Node(link[0])
                    self.nodes[link[0]].add_link(key, link[1])
                else:
                    if link[0] not in self.nodes:
                        self.nodes[link[0]] = Node(link[0])

    def get_cost(self, node1: str, node2: str) -> float:
        for link in self.nodes[node1].get_links_sorted():
            if link[0] == node2:
                return link[1]

    def get_node(self, node_id):
        return self.nodes[node_id]

    def draw(self):
        for node in self.nodes:
            print(self.nodes[node].get_id() + " " + str(self.nodes[node].get_links_sorted()))
