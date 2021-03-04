# -*- coding: utf-8 -*-
"""
Programming 10 Template

Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: Inhan Park
"""
__version__ = 1

def zipZap(zapper):    
    '''
    Given a string zapper, find all places in the original string where a three-letter combination
    starting with "z" and ending with "p" occurs.  Return a string where, for all such three-letter
    sequences, the middle letter has been removed.  For example, a string like "zipXzap" would
    produce a result of "zpXzp".
    '''
    if len(zapper) < 3:
        return zapper
    
    result = ''
    
    x = 0
    
    while x < len(zapper):
        if (x < len(zapper) - 2) and zapper[x] == 'z' and zapper[x + 2] == 'p':
            result += zapper[x] + zapper[x + 2]
            x += 3
        else:
            result += zapper[x]
            x += 1
    
    return result




def xyBalance(testStr):
    '''
    We'll say that a string is xy-balanced if for all the 'x' characters in the string, there
    exists a 'y' character somewhere later in the string.  So "xxy" is balanced, but "xyx" is
    not.  One "y" can balance multiple "x"s.  Return true if the given string is xy-balanced.
    '''
    numx = -1
    numy = -1
    
    for x in range(len(testStr)):
        if testStr[x] == 'x':
            numx = x
        elif testStr[x] == 'y':
            numy = x
    
    if numx <= numy:
        return True
    return False
        


######################################################################################

def main():
    # You can test your solutions by calling them from here
    assert zipZap('zipXzap') == 'zpXzp'
    assert zipZap('zp') == 'zp'
    assert zipZap('zapp') == 'zpp'
    assert zipZap('zzzz') == 'zzzz'
    assert not xyBalance('x')
    assert xyBalance('xxy')
    assert not xyBalance('xyx')
    assert xyBalance('xyxxxxy')
    assert not xyBalance('aabxb')
    assert xyBalance('bybb')
   
if __name__ == "__main__":
    main()    