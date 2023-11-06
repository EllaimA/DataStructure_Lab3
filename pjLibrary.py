import string
from collections import defaultdict
import time


# PriorityQueue class, used for storing nodes
class PriorityQueue:

    def __init__(self) -> None:
        # Initialize an empty priority queue.
        self.queue = []

    def push(self, item):
        # Add an item to the priority queue.
        # Args: item: The item to add to the priority queue.
        self.queue.append(item)
        # Sort the queue after adding the item
        self.queue = sorted(self.queue)

    def pop(self):
        # Remove and return the highest-priority item from the queue.
        # Returns: The highest-priority item.
        # Raises: IndexError: If the queue is empty.
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise IndexError("Queue is empty")

    def is_empty(self):
        # Check if the priority queue is empty.
        # Returns: bool: True if the queue is empty, False otherwise.
        return len(self.queue) == 0

    def size(self):
        # Get the number of elements in the priority queue.
        # Returns: int: The number of elements in the queue.
        return len(self.queue)

    def __str__(self):
        # Get a string representation of the priority queue.
        output = ""
        for s in self.queue:
            output += str(s)
        return output

# Create an alphabet list for resolveTie
alphabet = list(string.ascii_lowercase)

# Huffman Node class, with two children per node
class HuffmanNode:
    """
    Represents a node in a Huffman tree.

    Attributes:
        data: The character or data associated with the node.
        left: The left child node.
        right: The right child node.
        freq: The frequency of the character or data.
        is_internal_node: Indicates whether the node is an internal node (has no character).
    """

    def __init__(self, freq, data=None, left=None, right=None, is_internal_node=False):
        """
            Initializes a HuffmanNode.

            Args:
                freq: The frequency of the character or data.
                data: The character or data associated with the node.
                left: The left child node.
                right: The right child node.
                is_internal_node: Indicates whether the node is an internal node (has no character).
        """
        self.left = left
        self.right = right
        self.data = data
        self.freq = freq
        self.is_internal_node = is_internal_node

    # method that returns both children of the node
    def children(self):
        """
        Returns both children of the node.

        Returns:
            A tuple containing the left and right child nodes.
        """
        return self.left, self.right

    # Compares two HuffmanNodes based on frequency and data.
    def __lt__(self, other):
        # Args: other: Another HuffmanNode to compare.
        # Returns: True if the current node is less than the other node based on frequency and data, otherwise False.
        freq_comp = self.freq < other.freq
        if self.freq == other.freq and self.data and other.data:
            return self.data < other.data
        return freq_comp

    def __str__(self) -> str:
        """
        Returns a string representation of the node.

        Returns:
            A string containing the character or data, followed by its frequency.
        """
        return f'{self.data}: {self.freq} '



# Build a frequency dictionary from an input file.
def build_frequency_dict(input_file):
    # Args: input_file (str): The path to the input file.
    # Returns: default_dict: A dictionary with character frequencies.

    # Initialize a dictionary with default values of 0 for character frequencies
    freq_dict = defaultdict(int)

    # Open the input file
    with open(input_file) as f:
        # start CPU clock for time complexity analysis
        start_time = time.process_time()
        # Iterate through each line in the file
        for line in f.readlines():
            # Iterate through each character in the line
            for c in line:
                # Check if the character is alphanumeric
                if c.isalnum():
                    # Update the frequency of the character (convert to lowercase)
                    freq_dict[c.lower()] += 1
        end_time = time.process_time()    # end CPU clock
        total_time = end_time - start_time  # total elapsed CPU time for function execution
        print(f"Build Frequency Dictionary CPU Time: {total_time}")

    # Return the frequency dictionary
    print(freq_dict)
    return freq_dict


# Build a Huffman tree.
def build_huffman_tree(input_file=None, freq_dict=None):
    # Args_1: input_file (str, optional): The path to the input file.
    # Args_2: freq_dict (dict, optional): A precomputed frequency dictionary.
    # Returns: HuffmanNode: The root node of the Huffman tree.

    # start cpu clock for time complexity analysis
    start_time = time.process_time()
    
    # If a frequency dictionary is not provided, build one from the input file
    if freq_dict is None and input_file:
        freq_dict = build_frequency_dict(input_file)

    # Create a priority queue for Huffman nodes
    pq = PriorityQueue()

    # Iterate through the characters and frequencies in the dictionary
    for data, freq in freq_dict.items():
        # Create a Huffman node for each character and frequency
        node = HuffmanNode(freq, data)
        # Push the node onto the priority queue
        pq.push(node)

    # Continue until there is only one node left in the priority queue
    while pq.size() > 1:
        # Pop the two nodes with the lowest frequencies
        left = pq.pop()
        right = pq.pop()

        # Create a new node that combines the two nodes
        new_node = HuffmanNode(left.freq + right.freq, left.data + right.data, left=left, right=right,
                               is_internal_node=True)

        # Add the new node back to the priority queue
        pq.push(new_node)

    end_time = time.process_time()    # end CPU clock
    total_time = end_time - start_time  # total elapsed CPU time for function execution
    print(f"Build Huffman Tree CPU Time: {total_time}")
    
    # Return the root node of the Huffman tree
    return pq.pop()


# Print the Huffman tree or encode characters with Huffman codes.
def print_huffman_tree(node, freq_code_tuple_list, code='', print_tree=False):
    # Args_1: node (HuffmanNode): The current node in the Huffman tree.
    # Args_2: code (str, optional): The Huffman code generated during traversal.
    # Args_3: print_tree (bool, optional): If True, print the tree structure; if False, print Huffman codes.

    # Start CPU clock for time complexity analysis
    start_time = time.process_time()
    
    # Print the tree with in-order traversal
    if node:
        if node.data is not None:
            if print_tree:
                # Print character and frequency information
                # print(f'{node.data}: {node.freq} ')
                freq_code_tuple_list.append((node.data, node.freq))
            else:
                if not node.is_internal_node:
                    # Print character and its Huffman code
                    # print(f'{node.data} = {code}')
                    freq_code_tuple_list.append((node.data, code))

        # Traverse the left and right subtrees with updated codes
        print_huffman_tree(node.left, freq_code_tuple_list, code + '0', print_tree=print_tree)
        print_huffman_tree(node.right, freq_code_tuple_list, code + '1', print_tree=print_tree)
        return freq_code_tuple_list

    # end CPU clock
    end_time = time.process_time()
    # total elapsed CPU time for function execution
    total_time = end_time - start_time
    print(f"Print Huffman Tree CPU Time: {total_time}")


# Encode a string using Huffman codes
def encode(encode_string, codes):
    # string: The string to be encoded.
    # codes: A list of tuples where each tuple contains a character and its corresponding Huffman code.
    # return: A string representing the encoded binary sequence.

    full_coded_string = ''
    # Iterate through each character in the string.
    for char in encode_string:
        # Find the code for the character and concatenate it to the result string.
        full_coded_string += [char_code_tup[1] for char_code_tup in codes if char_code_tup[0] == char][0]
    return full_coded_string


# Decodes a binary string using the given Huffman tree.
def decode(root, decode_binary):
    # root: The root node of the Huffman tree.
    # decode_binary: The binary string to be decoded.
    # return: The decoded string.

    decoded_output = ""
    # Start at the root of the Huffman tree.
    current_node = root
    # Iterate through each bit in the binary string.
    for bit in decode_binary:
        # Traverse the Huffman tree.
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right
        # Check if the current node is a leaf node.
        if not current_node.is_internal_node:
            # If it's a leaf node, add the character to the output string.
            decoded_output += current_node.data
            # Reset to the root node for the next character.
            current_node = root
    return decoded_output
