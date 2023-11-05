from pjLibrary import HuffmanNode
from collections import defaultdict
from priority_queue import PriorityQueue


def build_frequecny_dict(input_file):
    """Build a frequency dictionary from an input file.

    Args:
        input_file (str): The path to the input file.

    Returns:
        defaultdict: A dictionary with character frequencies.
    """
    # Initialize a dictionary with default values of 0 for character frequencies
    freq_dict = defaultdict(int)
    
    # Open the input file
    with open(input_file) as f:
        start_time = time.process_time()   # start cpu clock for time complexity analysis
        # Iterate through each line in the file
        for line in f.readlines():
            # Iterate through each character in the line
            for c in line:
                # Check if the character is alphanumeric
                if c.isalnum():
                    # Update the frequency of the character (convert to lowercase)
                    freq_dict[c.lower()] += 1
        end_time = time.process_time()    # end cpu clock
        total_time = end_time - start_time  # total elapsed cpu time for function execution
        print(f"Build Frequency Dictionary CPU Time: {total_time}")

    # Return the frequency dictionary
    return freq_dict


def build_huffman_tree(input_file=None, freq_dict=None):
    """Build a Huffman tree.

    Args:
        input_file (str, optional): The path to the input file.
        freq_dict (dict, optional): A precomputed frequency dictionary.

    Returns:
        HuffmanNode: The root node of the Huffman tree.
    """

    start_time = time.process_time()   # start cpu clock for time complexity analysis

    # If a frequency dictionary is not provided, build one from the input file
    if freq_dict is None and input_file:
        freq_dict = build_frequecny_dict(input_file)

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
        new_node = HuffmanNode(left.freq + right.freq, left.data + right.data, left=left, right=right, is_intermediate_node=True)

        # Add the new node back to the priority queue
        pq.push(new_node)

    # Return the root node of the Huffman tree

    end_time = time.process_time()    # end cpu clock
    total_time = end_time - start_time  # total elapsed cpu time for function execution
    print(f"Build Huffman Tree CPU Time: {total_time}")
    return pq.pop()


def print_huffman_tree(node, code='', print_tree=False):
    """Print the Huffman tree or encode characters with Huffman codes.

    Args:
        node (HuffmanNode): The current node in the Huffman tree.
        code (str, optional): The Huffman code generated during traversal.
        print_tree (bool, optional): If True, print the tree structure; if False, print Huffman codes.
    """
    start_time = time.process_time()   # start cpu clock for time complexity analysis

    # Print the tree with in-order traversal
    if node:
        if node.data is not None:
            if print_tree:
                # Print character and frequency information
                print(f'{node.data}: {node.freq} ')
            else:
                if not node.is_intermediate_node:
                    # Print character and its Huffman code
                    print(f'{node.data} = {code}')
        
        # Traverse the left and right subtrees with updated codes
        print_huffman_tree(node.left, code + '0', print_tree=print_tree)
        print_huffman_tree(node.right, code + '1', print_tree=print_tree)
    
    end_time = time.process_time()    # end cpu clock
    total_time = end_time - start_time  # total elapsed cpu time for function execution
    print(f"Print Huffman Tree CPU Time: {total_time}")


if __name__ == '__main__':
    # simple test case
    text_freq_dict = {"X":3, "Y": 1, "Z": 2}
    print_huffman_tree(build_huffman_tree(freq_dict=text_freq_dict))
    print_huffman_tree(build_huffman_tree(freq_dict=text_freq_dict), print_tree=True)
