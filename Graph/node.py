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

    def get_links(self):
        return self.__links

    def get_neighbor(self):
        return map(lambda x: x[0], self.__links)

