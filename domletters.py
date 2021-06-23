#!/usr/bin/python3
import sys

def usage():
    """Outputs the correct usage of this program."""
    print("Usage:\n", sys.argv[0], "input.txt")

# Check for present command line argument.
if len(sys.argv) != 2:
    usage()
    exit(1)

