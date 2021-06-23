#!/usr/bin/python3
import sys

def usage():
    """Outputs the correct usage of this program."""
    print("Usage:\n", sys.argv[0], "input.txt")

# Check for present command line argument.
if len(sys.argv) != 2:
    usage()
    exit(1)

# Open input file.
try:
    filename = sys.argv[1]
    full_input_string = open(filename).read()
except FileNotFoundError:
    print("File:", end=" ");
    print("'", filename, "'", sep="", end=" ")
    print("not found.\nThis can be caused by either a mistype of the filename, or the file still needs to be created.")
    exit(1)

# Split the input string into words.
words = full_input_string.split() 
for word in words:
        print(word)