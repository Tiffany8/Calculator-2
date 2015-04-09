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
    """ This function will take the user's input, run a series of mathematical equations
    based on the user's input and return the result of set equations. """

    user_input_str = raw_input('> Please type in 1 operand and up to 2 numbers separated by spaces: ')

    # tokenize the user's input into a list of 3 elements
    tokenized_user_input_str = user_input_str.split(" ")

    # separate first element on list and make it the operator value
    operator_element = tokenized_user_input_str[0]

    # convert remaining elements in list to floats
    num1 = float(tokenized_user_input_str[1])
    num2 = float(tokenized_user_input_str[2])


    # make if, elif, else statement and pull in defs from arithmetic_calc2.py
    

    while 
        if operator_element == 'q':
            print "It worked!"
            break
        else:
            print "It broke :("


    print user_input_str
    print tokenized_user_input_str
    print operator_element
    print num1
    print type(num1)
    print num2
    print type(num2)

calculator()