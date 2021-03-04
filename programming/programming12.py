# -*- coding: utf-8 -*-
"""
Programming 12 Template

Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: Inhan Park
"""
__version__ = 1

def repeatFront(s, n):    
    '''
    Given a string s and an int n, return a string made of the first n characters of the string,
    followed by the first n-1 characters of the string, then the first n-2, and so on. You may
    assume that n is between 0 and the length of the string, inclusive (i.e. n >= 0 and
    n <= len(s)).
    '''
    result = ''
    
    while n > 0:
        result += s[:n]
        n -= 1
        
    return result
        




def repeatSeparator(word, sep, count):
    '''
    Given two strings, word and a separator sep, return a big string made of count occurrences of
    the word, each separated by the separator string.  n=1 produces only one copy of word, while
    n=0 produces the empty string.
    '''
    result = ''
    
    for x in range(count):
        result += word
        
        if x != count - 1:
            result += sep
    
    return result



######################################################################################

def main():
    # You can test your solutions by calling them from here
    assert repeatFront('integer', 3) == 'intini'
    assert repeatSeparator('integer', 'num', 3) == 'integernumintegernuminteger'
   
if __name__ == "__main__":
    main()    