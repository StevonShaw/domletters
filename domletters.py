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

def countDominateLetter(word):
    """Counts the occurences of each letter in the word, and returns the highest count seen.
    
    Args:
        word (string): the string to be analyzed.

    Returns:
        int: the number of times the highest seen character has appeared.
    """
    # Build map of characters to ints. Representing a letters and the number of times that letter was seen.
    characters_seen = dict()
    for char in word.lower():
        if char in characters_seen:
            characters_seen[char] += 1
        else:
            characters_seen[char] = 1
    
    # Find the highest occurance of a letter.
    highest = 0
    for char in characters_seen.keys():
        if characters_seen[char] > highest:
            highest = characters_seen[char]
    return highest

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

# Split the input string into words.
words = full_input_string.split() 

# Sum the count of each valid words' dominate letter.
total = 0
for word in words:
    if isValidWord(word):
        total += countDominateLetter(word)


print("The count of all the dominate letters in each valid word is:", total)
