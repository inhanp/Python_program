# -*- coding: utf-8 -*-
"""
Programming 9 Template

Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: Inhan Park
"""
__version__ = 1

def theEnd(string,front):    
    '''
    Write a function in Python that implements the following logic: Given a string, return a
    string of length 1 from its front, unless front is false, in which case return a string
    of length 1 from its back. The input string will be non-empty.
    '''
    if front:
        return string[:1]
    else:
        return string[-1]
        





def evenlySpaced(a,b,c):
    '''
    Write a function in Python that implements the following logic: Given three integers,
    a, b, and c, one of them is small, one is medium, and one is large. Return True if the three
    values are evenly spaced, so the difference between small and medium is the same as the
    difference between medium and large.  Return False otherwise.
    '''
    if a > b:
        temp = a
        a = b
        b = temp
        
    if b > c:
        temp = b
        b = c
        c = temp
        
    if a > b:
        temp = a
        a = b
        b = temp
        
    return (b - a) == (c - b)
        


######################################################################################

def main():
    # You can test your solutions by calling them from here
    assert theEnd('frontend', True) == 'f', 'return first 1 of string if front is true'
    assert theEnd('frontend', False) == 'd', 'return last 1 of string if front is false'
    assert evenlySpaced(5,1,3) == True, '1, 3, 5 are evenly spaced'
    assert evenlySpaced(5,3,1) == True, '1, 3, 5 are evenly spaced'
    assert evenlySpaced(1,3,5) == True, '1, 3, 5 are evenly spaced'
    assert evenlySpaced(1,5,3) == True, '1, 3, 5 are evenly spaced'
    assert evenlySpaced(3,5,1) == True, '1, 3, 5 are evenly spaced'
    assert evenlySpaced(3,1,5) == True, '1, 3, 5 are evenly spaced'
    assert evenlySpaced(8,1,4) == False, '1, 4, 8 are not evenly spaced'
   
if __name__ == "__main__":
    main()    