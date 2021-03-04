# -*- coding: utf-8 -*-
"""
Programming 13 Template

Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: Inhan Park
"""
__version__ = 1

def doubleChar(testStr):    
    '''
    Given a string, return a string where for every char in the original, there are two chars.
    '''
    result = ''
    for i in range(len(testStr)):
        result += testStr[i]
        result += testStr[i]
    
    return result




def sumRange(low, high):
    '''
    Given two integers low and high representing a range, return the sum of the integers in
    that range.  For example, if low is 12 and high is 18, the returned values should be the
    sum of 12+13+...+18, which is 105.  If low is greater than high, return 0.
    '''
    result = 0
    
    if (low > high):
        return 0
    
    i = low
    
    while i <= high:
        result += i
        i += 1
    
    return result


######################################################################################

def main():
    # You can test your solutions by calling them from here
    assert doubleChar('test') == 'tteesstt'
    assert doubleChar('ttt') == 'tttttt'
    assert sumRange(5,8) == 26
    assert sumRange(6,4) == 0
   
if __name__ == "__main__":
    main()    