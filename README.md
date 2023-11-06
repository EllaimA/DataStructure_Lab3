# DataStructure_Lab3
Huffman Encoding Tree

## The purpose of this program
This program will encode string to binary code and decode binary code to string. It will first build a Huffman Encoding Tree based on a frequency table, then do the encode/decode process.

## Group Members
Aurora Meng, Marc Roube, Koushik Parakulam, Dongyang Liu

### How to run the code
run `python main.py`

The Input_Files contains default input documents(a decode input file, a encode input file and the frequency list). When run, main.py will ask for an input and output directory, if not provided, the default I/O directory will be used.

The program will automatically recognize input files from the input directory and process them accordingly, generating output files in the output directory.

If the Decode_Input file is missing, the program will generate an empty Decoded_Strings file.

If the Encode_Input file is missing, the program will generate an empty Encoded_Binary file.

If the Frequency_List file is missing, the program will generate a frequency list based on the input string first, then parse input files.

Notice 1: Currently, the output directory contains output files we generated. To see the generation process, please delete files in the output directory first, then run the program. 
Notice 2: Our resolve tie is integrated in HuffmanNode class: __lt__(self, other): and PriorityQueue:sorted
