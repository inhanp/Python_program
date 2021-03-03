# -*- coding: utf-8 -*-
"""
Functions about word reductions

Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: INHAN PARK
"""
__version__ = 1

def endsLy(inString):    
    '''
    Write a function in Python that implements the following logic: Given a string inString, 
	return True if it ends in "ly".  Return False otherwise.
    '''
    if inString[-2:] == "ly":
        return True
    return False



def firstHalf(inString):
    '''
	Given a string of even length, return the first half (the string "woohoo" yields "woo"). 
	'''
    return inString[0:int(len(inString) / 2)]



def starOut(str):
    '''
	Return a version of the given inString, where for every star (*) in the string the star 
	and the character immediately to its left and the character immediately to its right are gone. 
	So "ab*cd" yields "ad" and "ab**cd" also yields "ad".
	'''
    result = ""
    
    for i in range(len(str)):
        if not ((i - 1 >= 0 and str[i - 1] == "*")
                or str[i] == "*" 
                or (i + 1 < len(str) and str[i + 1] == "*")):
            result += str[i]
    return result



def makeOutWord(out, word):
    '''
	Given an out string of length 4, such as "<<>>", and a word, return a new string where the 
	word is in the middle of the out string, e.g. "<<sample>>". 
	'''
    result = ""
    
    result += out[0:int(len(out) / 2)]
    
    result += word
    
    result += out[int(len(out) / 2) : ]
    
    return result




######################################################################################

def main():
    # You can test your solutions by calling them from here
    assert endsLy("ques") == False
    assert endsLy("fairly") == True
    assert firstHalf("woohoo") == "woo"
    assert starOut("ab*cd") == "ad"
    assert starOut("ab**cd") == "ad"
    assert makeOutWord("<<>>", "sample") == "<<sample>>"
   
if __name__ == "__main__":
    main()    
