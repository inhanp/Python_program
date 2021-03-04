# -*- coding: utf-8 -*-
"""
Programming 2 template

Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: Inhan Park
"""
__version__ = 1

def squirrelPlay(temperature, isSummer):    
    '''
    Write a function in Python that implements the following logic: The squirrels in Palo Alto 
	spend most of the day playing. In particular, they play if the temperature is between 
	60 and 90 (inclusive), unless it is summer, in which case the upper limit is 100 instead of 90. 
	Given an integer temperature and a Boolean isSummer, return True if the squirrels play 
	and False otherwise.
    '''
    lowLimit = 60
    highLimit = 90
    
    #if it is summer, set upper limit as 100
    if isSummer:
        highLimit = 100

    #check whether temperature is between lower limit and upper limit
    #return True if temperature is in range
    if temperature >= lowLimit and temperature <= highLimit:
        return True
    
    return False



def blackjack(a,b):
    '''
	Write a function in Python that implements the following logic: Given 2 int values a and b 
	greater than 0, return whichever value is nearest to 21 without going over. Return 0 if they 
	both go over.
	'''
    #check whether both a and b go over
    #return 0 if both go over
    if a - 21 > 0 and b - 21 > 0:
        return 0
    
    #if a goes over, return b
    #if b goes over, return a
    if a - 21 > 0:
        return b
    elif b - 21 > 0:
        return a
    
    #if a is closer to 21, return a
    #if b is closer to 21, return b
    #if both are at same distance from 21, return a, since both are same
    if 21 - a > 21 - b:
        return b
    elif 21 - b > 21 - a:
        return a
    else:
        return a



######################################################################################

def main():
    # You can test your solutions by calling them from here
    assert squirrelPlay(100, True) == True, "upper limit is 100 if it is summer"
    assert squirrelPlay(50, True) == False, "lower limit is 60"
    assert squirrelPlay(95, False) == False, "upper limit is 900 if it is not summer"
    assert squirrelPlay(50, False) == False, "lower limit is 60"
    assert blackjack(15, 17) == 17, "17 is closer than 15"
    assert blackjack(22, 1) == 1, "22 goes over, while 1 not"
    assert blackjack(10, 10) == 10, "10 and 10 does not go over"
    assert blackjack(10, 22) == 10, "22 goes over, while 10 not"
    assert blackjack(22, 22) == 0, "22 and 22 go over"
   
if __name__ == "__main__":
    main()    