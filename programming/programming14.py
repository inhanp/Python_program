# -*- coding: utf-8 -*-
"""
Programming 14 Template

Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: Inhan Park
"""
__version__ = 1

def allEven(number):    
    '''
    Given a 4-digit integer, determine whether or not each of the four digits is even.  Return
    False if any digit is odd; otherwise, return True.
    '''
    if number % 2 == 1:
        return False
    elif int(number / 10) % 2 == 1:
        return False
    elif int(number / 100) % 2 == 1:
        return False
    elif int(number / 1000) % 2 == 1:
        return False
    return True




def countCharsAndDigits(string):
    '''
    Write a function that takes a string as input, and returns a tuple that contains the number
    of characters (defined as everything that isn't a digit) and the number of digits in the
    string.  For example, the input "Hello world 123!" should return (13,3).
    '''
    character = 0
    digit = 0
    
    for char in string:
        if char.isnumeric():
            digit += 1
        else:
            character += 1
    
    return (character, digit)

######################################################################################

def main():
    # You can test your solutions by calling them from here
    assert allEven(2468)
    assert not allEven(1468)
    assert not allEven(238)
    assert not allEven(2458)
    assert not allEven(2467)
    assert countCharsAndDigits('Hello world 123!') == (13, 3)
    assert countCharsAndDigits('python 9753') == (7, 4)
   
if __name__ == "__main__":
    main()    