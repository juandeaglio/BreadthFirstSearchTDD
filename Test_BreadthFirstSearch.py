import unittest

from Node import Node
from Tree import Tree


class TreeTests(unittest.TestCase):
    def setUp(self):
        self.tree = Tree()

    def test_makeTree(self):
        self.tree = Tree(Node())
        self.assertTrue(self.tree.treeSize == 1)

class EmptyTreeTests(unittest.TestCase):
    def setUp(self):
        self.tree = Tree()

    def test_makeEmptyTree(self):
        self.assertTrue(self.tree.treeSize == 0)


if __name__ == '__main__':
    unittest.main()
