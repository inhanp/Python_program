# -*- coding: utf-8 -*-
"""
Programming 16 Template

Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: Inhan Park
"""
__version__ = 1

def robotMovement(commands):    
    '''
    Given a list of commands, which are formatted as strings in the form "DIRECTION<space>DISTANCE"
    (for example, "UP 2" or "RIGHT 14"), and assuming that the robot always begins at the (0,0)
    origin, write a function that returns a tuple containing the final (x,y) position of the robot
    after all commands have been executed.  Directions will always be UP, DOWN, LEFT, and RIGHT,
    while distances can be positive integers or floats.  Not providing any commands leaves the robot
    at the (0,0) origin.  (Hint: remember that you can split strings by any character, such as a
    space.)
    '''
    x = 0
    y = 0
    
    for command in commands:
        
        direction = command.split()[0]
        distance = float(command.split()[1])
    
        if direction == "UP":
            y = y + distance
        elif direction == "DOWN":
            y = y - distance
        elif direction == "LEFT":
            x = x - distance
        elif direction == "RIGHT":
            x = x + distance
        
    return x, y 




def robotMovementTrace(commands):
    '''
    Given a list of commands, which are formatted as strings in the form "DIRECTION<space>DISTANCE"
    (for example, "UP 2" or "RIGHT 14"), and assuming that the robot always begins at the (0,0)
    origin, write a function that returns a tuple containing (1) the total driving distance that
    the robot traveled while running the commands and (2) the Euclidean distance between its
    endpoint and the (0,0) origin.  To compute the Euclidean distance, think about computing the
    hypotenuse of a right triangle (alternatively, use the standard Euclidean distance formula with
    a (0,0) point:  https://en.wikipedia.org/wiki/Euclidean_distance#Two_dimensions).  Both values
    returned in the tuple will always be positive.
    '''
    total_dist = 0
    euclid_dist = 0
    x = 0
    y = 0
    
    for command in commands:
        
        direction = command.split()[0]
        distance = float(command.split()[1])
    
        if direction == "UP":
            y = y + distance
        elif direction == "DOWN":
            y = y - distance
        elif direction == "LEFT":
            x = x - distance
        elif direction == "RIGHT":
            x = x + distance
        
        total_dist = total_dist + distance
        
    euclid_dist = (x**2 + y**2)**0.5
    
    return total_dist, euclid_dist




######################################################################################

def main():
    # You can test your solutions by calling them from here
    assert robotMovement(["UP 2", "LEFT 6"]) == (-6.0, 2.0)
    assert robotMovementTrace(["UP 3", "LEFT 4"]) == (7.0, 5.0)
   
if __name__ == "__main__":
    main()    