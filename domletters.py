#!/usr/bin/python3
import sys
import re

def usage():
    """Outputs the correct usage of this program."""
    print("Usage:\n", sys.argv[0], "input.txt")

def isValidWord(word):
    """Checks if the word contains any characters outside [a-zA-Z].
    
    Args:
        word (string): a potentially valid word.

    Returns:
        bool: is the word valid?
    """
    pattern = "[a-zA-Z]"
    for char in word:
        if not re.search(pattern, char):
            return False
    return True

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
    if isValidWord(word):
        print(word)