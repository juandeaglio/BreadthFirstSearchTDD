import unittest
from Graph import Graph


class BreadthFirstSearch(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()

    def test_makeEmptyGraph(self):
        self.assertTrue(len(self.graph) == 0)

    def test_makeGraphOfOneNode(self):
        self.graph.createNode("A")
        self.assertTrue(len(self.graph) == 1)


if __name__ == '__main__':
    unittest.main()
