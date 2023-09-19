import unittest

from BellmanFord.bellmanFord import BellmanFord
from Dijkstra.dijkstra import Dijkstra
from Graph.graph import Graph


class RunAlgoTest(unittest.TestCase):

    graph_representation = {"A": {("B", 1), ("C", 2)}, "B": {("D", 4)}, "C": {("D", 1)}}
    graph = Graph(graph_representation, True)

    def test_dijkstra(self):
        algo = Dijkstra(self.graph)
        dist, prev = algo.draw("A")
        self.assertEqual(dist, {'A': 0, 'B': 1, 'C': 2, 'D': 3})
        self.assertEqual(prev, {'A': None, 'C': 'A', 'B': 'A', 'D': 'C'})

    def test_bellman_ford(self):
        algo = BellmanFord(self.graph)
        dist, prev = algo.draw("A")
        self.assertEqual(dist, {'A': 0, 'B': 1, 'C': 2, 'D': 3})
        self.assertEqual(prev, {'A': None, 'C': 'A', 'B': 'A', 'D': 'C'})

if __name__ == '__main__':
    unittest.main()
