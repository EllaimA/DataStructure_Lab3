# Huffman Node class, with two children per node
class HuffmanNode():
    def __init__(self, left=None, right=None, root=None):
        self.left = left
        self.right = right
        self.root = root    
    def children(self):
        return self.left, self.right    # method that returns both children of the node

