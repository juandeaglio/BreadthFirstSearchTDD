from Node import Node


class Tree:
    def __init__(self, root=None):
        self.root = Node()
        self.root = root
        self.treeSize = 0
        if root is not None:
            self.treeSize += 1

    def createNode(self, param):
        pass
