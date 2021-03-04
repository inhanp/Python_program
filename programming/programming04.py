# -*- coding: utf-8 -*-
"""
Programming 4 Template

Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: Inhan Park
"""
__version__ = 1

def extraEnd(string):    
    '''
    Given a string, return a new string made of 3 copies of the last 2 characters of the 
    original string. The original string's length will be at least 2.
    '''
    temp = string[-2:]
    temp = temp + temp + temp
    return temp



def without2(string):
    '''
	Given a string, if the same 2-character substring appears at both its beginning and 
    end, return the contents of the string without the 2-character substring at the beginning. 
    For example, "HelloHe" yields "lloHe". Note that the 2-character substring at the 
    beginning may overlap with the one at the end, so "Hi" yields "". If the two characters 
    at the start and end of the string do not match each other, return the original string 
    unchanged.
	'''
    if string[:2] == string[-2:]:
        return string[2:]
    return string


######################################################################################

def main():
    # You can test your solutions by calling them from here
    assert extraEnd("example") == 'lelele', "return 3 copies of the last 2 characters of the original string"
    assert without2("HelloHe") == 'lloHe', 'remove 2-character substring at beginning if same with 2-character at end'
    assert without2('lloHe') == 'lloHe', 'return original string if 2-character substring at begninning and end not match'
   
if __name__ == "__main__":
    main()    