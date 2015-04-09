"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic_calc2 import *


# Your code goes here
# No setup
# repeat forever:
#     read input
#     tokenize input
#     if the first token is 'q', quit
#     otherwise decide which math function to call based on the tokens we read

# first input 3 characters with instructions
# split user entry based on spaces
#giant if, elif, else statement that will look at [0] and depending on what symbol,
    # it will call a function from arithmetic_calc2 (only if enter 'q' it will quit. 
        #else is everything else that doesn't compute)
#print functions return call
# repeat

def calculator():
    user_input_str = raw_input('> Please type in 1 operand and up to 2 numbers separated by spaces: ')
    print user_input_str

calculator()