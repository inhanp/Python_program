# -*- coding: utf-8 -*-
"""
Programming 5 Template

Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: Inhan Park
"""
__version__ = 1

def atFirst(string):    
    '''
    Write a function that implements the following logic: Given a string, return a
    string made of its first 2 chars. If the string length is less than 2, use '@'
    for the missing chars.
    '''
    length = len(string)
    result = ''
    if length == 0:
        result = '@@'
    elif length == 1:
        result = string + '@'
    else:
        result = string[:2]
    
    return result



def makeTags(tag, word):
    '''
	Write a function that implements the following logic: The web is built with 
    HTML strings like "<i>Yay</i>" which draws Yay as italic text. In this example,
    the "i" tag makes <i> and </i> which surround the word "Yay". Given tag and 
    word strings, create the HTML string with tags around the word, e.g. 
    "<i>Yay</i>".
	'''
    first = "<" + tag + ">"
    second = "</" + tag + ">"
    result = first + word + second
    return result



######################################################################################

def main():
    # You can test your solutions by calling them from here
    assert atFirst('') == '@@', 'If string length is 0, return @@'
    assert atFirst('a') == 'a@', "If string length is 1, use '@' for missing chars."
    assert atFirst('ab') == 'ab', 'If string length is 2, return it at it is'
    assert atFirst('abc') == 'ab', 'If string length is more than 2, return first two of it'
    assert makeTags('i', 'Yay') == "<i>Yay</i>"
    assert makeTags('', 'Yay') == "<>Yay</>"
   
if __name__ == "__main__":
    main()    