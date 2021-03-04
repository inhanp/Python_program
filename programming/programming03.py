# -*- coding: utf-8 -*-
"""
Programming 3 Template

Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: Inhan Park
"""
__version__ = 1

def prefixAgain(string, N):    
    '''
    Given a string, consider the prefix made of the first N chars of the string. Does that
	prefix string appear somewhere else in the string?  Assume that the string is not empty 
	and that N is in the range 1..str.length(). Case is important to the existence of a prefix.
    '''
    prefix = string[:N]
    
    if string[N:].find(prefix) != -1:
        return True
    return False


def greenTicket(a, b, c):
    '''
	You have a green lottery ticket with three integers: a, b, and c.  If all of the numbers 
	are different on it, return 0.  If two of the numbers are the same, return 10.  If all of 
	the numbers are the same, return 20.
	'''
    match = 0
    
    if a == b:
        match += 1
    
    if b == c:
        match += 1
    
    if a == c:
        match += 1
    
    if match == 3:
        return 20
    elif match == 1:
        return 10
    else:
        return 0



######################################################################################

def main():
    # You can test your solutions by calling them from here
    assert prefixAgain("Twiddle", 2) == False, "Does not have repeated prefix"
    assert prefixAgain("boomboom", 3) == True, "Have repeated prefix"
    assert greenTicket(1,1,1) == 20, "All three same"
    assert greenTicket(1,2,1) == 10, "Two are same"
    assert greenTicket(2,2,1) == 10, "Two are same"
    assert greenTicket(1,2,2) == 10, "Two are same"
    assert greenTicket(1,2,3) == 0, "None are same"
   
if __name__ == "__main__":
    main()    