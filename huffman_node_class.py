# Huffman Node class, with two children per node
class HuffmanNode():
    def __init__(self, left=None, right=None, root=None, frequency=None):
        self.left = left
        self.right = right
        self.root = root
        self.frequency = frequency
    def children(self):
        return self.left, self.right    # method that returns both children of the node

