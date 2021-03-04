# -*- coding: utf-8 -*-
"""
Programming 17 Template

Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: Inhan Park
"""
__version__ = 1

def listFilter(val):    
    '''
    Create a list that contains the square of all numbers between 1 and 100 (i.e., [1,4,9,16,...]).
    Then, using the val parameter passed into this function, return the number of items in your
    list that are smaller than val.
    '''
    list = []
    for num in range(1, 101):
        list.append(num**2)
    
    result = 0

    for item in list:
        if item < val:
            result += 1
    
    return result



def listFilterSum(val):
    '''
    Create a list that contains the cube of all numbers between 1 and 50 (i.e., [1,8,27,64,...]).
    Then, using the val parameter passed into this function, return the sum of the items in your
    list that are greater than or equal to val.
    '''
    list = []
    for num in range(1, 51):
        list.append(num**3)
        
    result = 0
    
    for item in list:
        if item >= val:
            result += item
    
    return result


######################################################################################

def main():
    # You can test your solutions by calling them from here
    assert listFilter(0) == 0
    assert listFilter(37) == 6
    assert listFilterSum(125000) == 125000
   
if __name__ == "__main__":
    main()    