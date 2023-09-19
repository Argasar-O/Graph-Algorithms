from Graph.node import Node


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

    def get_edges(self):
        edges = []
        for node in self.nodes:
            node_edges = self.nodes[node].get_links()
            for edge in node_edges:
                edges.append((node, edge[0], edge[1]))
        return edges

    def draw(self):
        for node in self.nodes:
            print(self.nodes[node].get_id() + " " + str(self.nodes[node].get_links_sorted()))
