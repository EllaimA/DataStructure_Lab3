import string
import os
import re
from collections import defaultdict
from priority_queue import PriorityQueue
import time

# Huffman Node class, with two children per node
class HuffmanNode():
    def __init__(self, freq, data=None, left=None, right=None, is_internal_node=False):
        self.left = left
        self.right = right
        self.data = data
        self.freq = freq
        self.is_internal_node = is_internal_node

    # method that returns both children of the node
    def children(self):
        return self.left, self.right

    def __lt__(self, other):
        freq_comp = self.freq < other.freq
        if self.freq == other.freq and self.data and other.data:
            return self.data < other.data
        return freq_comp

    def __str__(self) -> str:
        return f'{self.data}: {self.freq} '

# Create an alphabet list
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

def user_handler(all_default_dir):
    """
    Handles user input for directories.

    Prompts the user to provide input and output directories. If no input is
    given, defaults are used. Checks if provided paths are valid directories.

    Args:
    all_default_dir: A list containing the default directories for input and output.

    Returns:
    input_output_dir: A list containing the directories for input and output.
    """
    input_output_name = ['Input', 'Output']
    input_output_dir = []
    for input_output, default_dir in zip(input_output_name, all_default_dir):
        print('\nDefault '+input_output+' Directory: ' + default_dir + '\n')
        directory = input('Please provide a '+input_output+' directory, if none is provided default will be used: ')
        while True:
            if not directory:
                directory = default_dir  # Use the default directory if none is provided
                break
            elif os.path.isdir(directory):
                break  # Break the loop if a valid directory is provided
            else:
                print('\nProvided Directory is not a valid path')
                print('\nDefault '+input_output+' Directory: ' + default_dir + '\n')
                directory = input('Please provide a '+input_output+' directory, if none is provided default will be used: ')
        input_output_dir.append(directory)

    return input_output_dir

def input_file_handler(input_files, input_file_dir):
    """
    Processes input files to extract frequency data, encoded, and decoded strings.

    Reads each file, parses the frequency of characters if present, collects binary
    strings assumed to be coded messages, and gathers plain text to be encoded.

    Args:
    input_files: A list of file names to be processed.
    input_file_dir: The directory where input files are located.

    Returns:
    A tuple containing the frequency dictionary, list of strings to encode, and list of binary strings to decode.
    """
    text_freq_dict = {}
    decode_list = []
    encode_list = []
    for file in input_files:
        with open(input_file_dir+'\\'+file) as new_file:
            for line in new_file:
                new_line = line.rstrip().lstrip() # strips extraneous white space
                if new_line != '\n': # makes sure line is not empty

                    # Finds lines associated with Frequency_list by '-' delimiter
                    if '-' in new_line:
                        characters_frequency = new_line.split('-')
                        characters = characters_frequency[0].rstrip().lstrip()
                        frequency = characters_frequency[1].rstrip().lstrip()
                        if frequency.isdigit():
                            text_freq_dict[characters] = int(frequency)  # Add to frequency dictionary

                    # Finds lines associated with Decode_Input by 01 binary characters
                    elif all(value in "01" for value in new_line):
                        decode_list.append(new_line)  # Add to list for decoding

                    # Finds lines associated with Encode_Input
                    else:
                        new_line = new_line.replace(' ', '') # Strips out spaces
                        new_line = re.sub(r'[^\w\s]', '', new_line) # Strips out punctuation
                        encode_list.append(new_line.upper())  # Add to list for encoding
    return text_freq_dict, encode_list, decode_list

def output_file_handler(all_output_files_dir, all_output_data):
    """
    Writes provided data to output files in a formatted manner.

    Depending on the type of file, formats and writes the character codes, preorder
    traversal data, or the Huffman encoding/decoding result to the file.

    Args:
    all_output_files_dir: A list containing directories of the output files.
    all_output_data: A list of data corresponding to each output file.
    """
    for file, data in zip(all_output_files_dir, all_output_data):
        with open(file, 'w') as outfile:
            for value in data:
                if 'Character_Code' in file:
                    outfile.write(str(value[0])+' = '+ str(value[1]))  # Write character codes
                elif 'Preorder' in file:
                    outfile.write(str(value[0]) + ' : ' + str(value[1]))  # Write preorder traversal
                else:
                    # Format and write the Huffman encoding/decoding result
                    largest_key = max(len(x) for x in data.keys())
                    largest_value = max(len(x) for x in data.values())
                    # Formats based on largest key, value pair for column output
                    outfile.write(("{:<"+str(largest_key)+"} ---> {:<"+str(largest_value)+"}").format(value, data.get(value)))
                outfile.write('\n')  # New line after each entry


def build_frequency_dict(input_file):
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
        start_time = time.process_time() # start CPU clock for time complexity analysis 
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
    while pq.qsize() > 1:
        # Pop the two nodes with the lowest frequencies
        left = pq.pop()
        right = pq.pop()

        # Create a new node that combines the two nodes
        new_node = HuffmanNode(left.freq + right.freq, left.data + right.data, left=left, right=right,
                               is_internal_node=True)

        # Add the new node back to the priority queue
        pq.pop(new_node)

    end_time = time.process_time()    # end CPU clock
    total_time = end_time - start_time  # total elapsed CPU time for function execution
    print(f"Build Huffman Tree CPU Time: {total_time}")
    
    # Return the root node of the Huffman tree
    return pq.pop()


def print_huffman_tree(node, freq_code_tuple_list, code='', print_tree=False):
    """Print the Huffman tree or encode characters with Huffman codes.

    Args:
        node (HuffmanNode): The current node in the Huffman tree.
        code (str, optional): The Huffman code generated during traversal.
        print_tree (bool, optional): If True, print the tree structure; if False, print Huffman codes.
    """
    start_time = time.process_time()   # Start CPU clock for time complexity analysis
    
    # Print the tree with in-order traversal
    if node:
        if node.data is not None:
            if print_tree:
                # Print character and frequency information
                #print(f'{node.data}: {node.freq} ')
                freq_code_tuple_list.append((node.data, node.freq))
            else:
                if not node.is_internal_node:
                    # Print character and its Huffman code
                    #print(f'{node.data} = {code}')
                    freq_code_tuple_list.append((node.data, code))

        # Traverse the left and right subtrees with updated codes
        print_huffman_tree(node.left, freq_code_tuple_list, code + '0', print_tree=print_tree)
        print_huffman_tree(node.right, freq_code_tuple_list, code + '1', print_tree=print_tree)
        return freq_code_tuple_list
        
    end_time = time.process_time()    # end CPU clock
    total_time = end_time - start_time  # total elapsed CPU time for function execution
    print(f"Print Huffman Tree CPU Time: {total_time}")


# Encode the string using Huffman codes
def encode(string, codes):
    """
    Encodes a string using the given Huffman codes.

    string: The string to be encoded.
    codes: A list of tuples where each tuple contains a character and its corresponding Huffman code.
    return: A string representing the encoded binary sequence.
    """
    full_coded_string = ''
    # Iterate through each character in the string.
    for char in string:
        # Find the code for the character and concatenate it to the result string.
        full_coded_string += [char_code_tup[1] for char_code_tup in codes if char_code_tup[0] == char][0]
    return full_coded_string

def decode(root, decode_binary):
    """
    Decodes a binary string using the given Huffman tree.

    root: The root node of the Huffman tree.
    decode_binary: The binary string to be decoded.
    return: The decoded string.
    """
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



