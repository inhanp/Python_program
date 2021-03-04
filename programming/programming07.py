# -*- coding: utf-8 -*-
"""
Programming 7 Template

Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: Inhan Park
"""
__version__ = 1

def roundSum(a,b,c):    
    '''
    For this problem, we'll round an int value up to the next multiple of 10 if its
    rightmost digit is 5 or more, so 15 rounds up to 20. Alternately, round down to
    the previous multiple of 10 if its rightmost digit is less than 5, so 12 rounds
    down to 10. Given 3 integers, a, b, and c, return the sum of their rounded values.
    To avoid code repetition, write a separate helper function round10(num) and call
    it 3 times. The helper function definition is provided below.
    '''
    a = round10(a)
    b = round10(b)
    c = round10(c)
    
    return a + b + c

def round10(num):
    '''
    This is where you will write the helper function as described above.
    '''
    temp = num
    
    if temp % 10 < 5:
        temp = temp - (temp%10)
    else :
        temp = temp - (temp%10) + 10
    return temp
            




def makeChocolate(givenSmall, givenBig, goal):
    '''
    We want to make a package of goal kilos of chocolate. We have small bars
    (1 kilo each) and big bars (5 kilos each). Return the number of small bars
    to use, assuming we always use big bars before small bars to reach the total
    goal.  Return -1 if goal kilos can't be made with givenSmall small bars and
    givenBig big bars.  You cannot break a big bar into 5 small bars.
    '''
    if goal >= (5 * givenBig):
        remain = goal - (5 * givenBig)
    else:
        remain = goal % 5
        
    if remain <= givenSmall:
        return remain
        
    return -1
    
    


######################################################################################

def main():
    # You can test your solutions by calling them from here
    assert round10(10) == 10
    assert round10(14) == 10
    assert round10(16) == 20
    assert roundSum(0, 0, 0) == 0
    assert roundSum(1, 10, 14) == 20
    assert makeChocolate(10, 10, 100) == -1
    assert makeChocolate(10, 10, 55) == 5
    assert makeChocolate(10, 10, 45) == 0
   
if __name__ == "__main__":
    main()    