#!/usr/bin/python3
import re

def wordContainsPattern(word, pattern):
    """Checks if the word contains any characters outside the given pattern.
    
    Args:
        word (string): a potentially valid word.
        pattern (string): a regex pattern string to match against. 

    Returns:
        bool: does the word contain any characters outside the given pattern?
    """
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
    try:
        # Build map of characters to ints. Representing a letter and the number of times that letter was seen.
        characters_seen = dict()
        dominate_char = word.lower()[0]
        for char in word.lower():
            if char in characters_seen:
                characters_seen[char] += 1
            else:
                characters_seen[char] = 1
            # Update highest count seen.
            if  characters_seen[char] > characters_seen[dominate_char]:
                dominate_char = char
        highest = characters_seen[dominate_char]
    except:
        highest = 0
    finally:
        return highest

# Read input file.
input_string = ""
try:
    while True:
        input_string += input()
        input_string += "\n"
except EOFError:
    pass

# Split the input string into words.
words = input_string.split() 

# Sum the count of each valid words' dominate letter.
total = 0
pattern = "[a-zA-Z]"
for word in words:
    if wordContainsPattern(word, pattern):
        total += countDominateLetter(word)

print("The count of all the dominate letters in each valid word is:", total)
