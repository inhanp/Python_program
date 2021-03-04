# -*- coding: utf-8 -*-
"""
Programming 6 Template

Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: Inhan Park
"""
__version__ = 1

def caughtSpeeding(speed, isBirthday):    
    '''
    Write a function in Python that implements the following logic: You are driving a little
    too fast, and a police officer stops you. Write code to compute the result, encoded as an
    int value: 0=no ticket, 1=small ticket, or 2=big ticket. If speed is 60 or less, the
    result is 0. If speed is between 61 and 80 inclusive, the result is 1. If speed is 81 or
    more, the result is 2. Unless it is your birthday -- on that day, your speed can be 5 higher
    in all cases.
    '''
    if isBirthday:
        speed = speed - 5
    
    if speed <= 60:
        return 0
    elif speed >= 61 and speed <= 80:
        return 1
    else:
        return 2



def noTeenSum(a, b, c):
    '''
    Write a function in Python that implements the following logic: Given 3 int values, a, b,
    and c, return their sum. However, if any of the input values is a teen -- in the range 13..19
    inclusive--then that value counts as 0, except that 15 and 16 do not count as teens.
    '''
    result = 0
    
    teens = [13, 14, 17, 18, 19]
    
    if a not in teens:
        result = result + a
    
    if b not in teens:
        result = result + b
        
    if c not in teens:
        result = result + c
    
    return result


######################################################################################

def main():
    # You can test your solutions by calling them from here
    assert caughtSpeeding(60, False) == 0, 'If it is not birthday, no ticket for below 60'
    assert caughtSpeeding(80, False) == 1, 'If it is not birthday, small ticket for between 61 and 80'
    assert caughtSpeeding(100, False) == 2, 'If it is not birthday, big ticket for more than 81'
    assert caughtSpeeding(65, True) == 0, 'If it is not birthday, no ticket for below 65'
    assert caughtSpeeding(85, True) == 1, 'If it is not birthday, small ticket for between 66 and 85'
    assert caughtSpeeding(86, True) == 2, 'If it is not birthday, big ticket for more than 86'
    
    assert noTeenSum(11, 12, 10) == 33, 'If none of them are teen, sum all'
    assert noTeenSum(13, 12, 10) == 22, 'If one of them are teen, sum other two'
    assert noTeenSum(11, 13, 14) == 11, 'If two of them are teen, sum one remain'
    assert noTeenSum(13, 14, 18) == 0, 'If all of them are teen, sum none'
   
if __name__ == "__main__":
    main()    