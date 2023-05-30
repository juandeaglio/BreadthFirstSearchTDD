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