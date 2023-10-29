from pjLibrary import HuffmanNode
from collections import defaultdict
import heapq

def build_frequecny_dict(input_file):
    freq_dict = defaultdict(int)
    with open(input_file) as f:
        for line in f.readlines():
            for c in line:
                # Checks if character is alphanumeric
                if c.isalnum():
                    freq_dict[c.lower()] += 1
    return freq_dict


def build_huffman_tree(input_file=None, freq_dict=None):
    if freq_dict is None and input_file:
        freq_dict = build_frequecny_dict(input_file)

    heap = []
    for data, freq in freq_dict.items():
        node = HuffmanNode(freq, data)
        # print(node)
        heapq.heappush(heap, node)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        new_node = HuffmanNode(left.freq + right.freq, left.data + right.data, left=left, right=right, is_intermediate_node=True)

        # Add the new_node back to heap
        heapq.heappush(heap, new_node)
    
    return heap[0]

def print_huffman_tree(node, code='', print_tree=False):
    # print with in-order traversal
    if node:
        if node.data is not None:
            if print_tree:
                print(f'{node.data}: {node.freq} ')
            else:
                if not node.is_intermediate_node:
                    print(f'{node.data} = {code}') 
        print_huffman_tree(node.left, code + '0', print_tree=print_tree)
        print_huffman_tree(node.right, code + '1', print_tree=print_tree)


if __name__ == '__main__':
    # simple test case
    text_freq_dict = {"X":3, "Y": 1, "Z": 2}
    print_huffman_tree(build_huffman_tree(freq_dict=text_freq_dict))
    print_huffman_tree(build_huffman_tree(freq_dict=text_freq_dict), print_tree=True)
