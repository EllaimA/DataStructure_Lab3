# Import functions
from pjLibrary import user_handler
from pjLibrary import input_file_handler
from pjLibrary import output_file_handler
from pjLibrary import build_huffman_tree
from pjLibrary import print_huffman_tree
from pjLibrary import encode
from pjLibrary import decode
import os

def main():
    # Get the current working directory.
    working_dir = str(os.getcwd())

    # Define the default output and input directories.
    def_output_dir = working_dir + '\\Output_Files'
    def_input_dir = working_dir + '\\Input_Files'

    # Aggregate the default directories into a list.
    all_default_dir = [def_input_dir, def_output_dir]

    # Handle user input for input and output directories.
    input_output_dir = user_handler(all_default_dir)

    # Assign directories for input and output folders.
    input_folder_dir = input_output_dir[0]
    output_folder_dir = input_output_dir[1]

    # Makes new Output folder if it does not exist
    if not os.path.exists(output_folder_dir):
        os.mkdir(output_folder_dir)

    # List all files in the input directory.
    input_files = os.listdir(input_output_dir[0])

    # Process the input files to get the character frequencies, strings to encode, and binaries to decode.
    text_freq_dict, encode_list, decode_list = input_file_handler(input_files, input_folder_dir)

    # Initialize lists and dictionaries for storing output data.
    character_code_tuple_list = []
    pre_order_frequency_tuple_list = []
    decoded_dict = {}
    encoded_dict = {}

    # Define the output files directory paths.
    all_output_files_dir = [output_folder_dir + '\\Character_Code.txt', output_folder_dir + '\\Preorder.txt',
                            output_folder_dir + '\\Decoded_Strings.txt', output_folder_dir + '\\Encoded_Binary.txt']

    # Generate and store the Huffman tree character codes.
    character_code_tuple_list = print_huffman_tree(build_huffman_tree(freq_dict=text_freq_dict),
                                                   character_code_tuple_list)

    # Generate and store the preorder traversal of the Huffman tree with frequencies.
    pre_order_frequency_tuple_list = print_huffman_tree(build_huffman_tree(freq_dict=text_freq_dict),
                                                        pre_order_frequency_tuple_list,
                                                        print_tree=True)

    # Decode the binary strings using the Huffman tree and store the results.
    for decode_binary in decode_list:
        root_node = build_huffman_tree(freq_dict=text_freq_dict)
        decoded_string = decode(root_node, decode_binary)
        decoded_dict[decode_binary] = decoded_string

    # Encode the strings using the Huffman codes and store the results.
    for encode_string in encode_list:
        encoded_binary = encode(encode_string, character_code_tuple_list)
        encoded_dict[encode_string] = encoded_binary

    # Compile all output data into a list.
    all_output_data = [character_code_tuple_list, pre_order_frequency_tuple_list, decoded_dict, encoded_dict]

    # Write the output data to their respective files.
    output_file_handler(all_output_files_dir, all_output_data)


if __name__ == '__main__':
    main()
