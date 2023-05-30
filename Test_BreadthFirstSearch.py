import unittest


class Node:
    def __init__(self, name):
        self.name = name


class Graph:
    def __init__(self):
        self.nodes = []

    def __len__(self):
        return len(self.nodes)

    def createNode(self, name):
        self.nodes.append(Node(name))


class MyTestCase(unittest.TestCase):
    def test_makeEmptyGraph(self):
        graph = Graph()
        self.assertTrue(len(graph) == 0)

    def test_makeGraphOfOneNode(self):
        graph = Graph()
        graph.createNode("A")
        self.assertTrue(len(graph) == 1)


if __name__ == '__main__':
    unittest.main()
