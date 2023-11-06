import re
import os
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

