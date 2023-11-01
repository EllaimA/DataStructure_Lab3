import string

# Huffman Node class, with two children per node
class HuffmanNode():
    def __init__(self, freq, data=None, left=None, right=None, is_intermediate_node=False):
        self.left = left
        self.right = right
        self.data = data
        self.freq = freq
        self.is_intermediate_node = is_intermediate_node

    def children(self):
        return self.left, self.right    # method that returns both children of the node
    
    def __lt__(self, other):
        freq_comp = self.freq < other.freq
        if self.freq == other.freq and self.data and other.data:
            return self.data < other.data
        return freq_comp

    def __str__(self) -> str:
        return f'{self.data}: {self.freq} '

# Create a alphabet list
alphabet = list(string.ascii_lowercase)

# Resolve ties by giving single-letter precedence over letter groups then alphabetically
# Pass in two strings needs to be compared
def resolveTie(stringA, stringB):
    # Check which string is shorter, return two strings as a tuple so the shorter
    # string is the first element in the tuple
    if len(stringA) < len(stringB):
        return (stringA, stringB)
    elif len(stringB) < len(stringA):
        return (stringB, stringA)
    # Order strings of the same length alphabetically
    else:
        if stringA.lower() < stringB.lower():
            return (stringA, stringB)
        else:
            return (stringB, stringA)
