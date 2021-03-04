# -*- coding: utf-8 -*-
"""
Programming 15 Template

Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: INHAN PARK
"""
__version__ = 1

def passwordCheck(password):    
    '''
    A website requires the users to input a username and password to register.  Write a function
    to check the validity of passwords provided by new users.  To be valid (return True), a
    password must have (1) at least one capital letter [A-Z], (2) at least one number [0-9],
    (3) at least one lower-case letter [az], and (4) a special character from the list [!@#$%^&*].
    If the password fails to meet any of those conditions, return False.
    '''
    special = ['!','@','#','$','%','^','&','*']
    
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char in special for char in password):
        return False
    return True
        


def flexiblePasswordCheck(password):
    '''
    A website requires the users to input a username and password to register.  Write a function
    to check the validity of passwords provided by new users.  To be valid (return True), a
    password must have at least one capital letter [A-Z], as well as any two of the three properties
    that follow:  (1) at least one number [0-9], (2) at least one lower-case letter [az], and
    (3) a special character from the list [!@#$%^&*].  If the password fails to meet any of
    those conditions, return False.
    '''
    special = ['!','@','#','$','%','^','&','*']
    
    condition = 3
    
    if not any(char.isupper() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        condition -= 1
    if not any(char.islower() for char in password):
        condition -= 1
    if not any(char in special for char in password):
        condition -= 1
    if condition < 2:
        return False
    return True


######################################################################################

def main():
    # You can test your solutions by calling them from here
    assert passwordCheck('123Ab$')
    assert not passwordCheck('123Ab')
    assert not passwordCheck('123b$')
    assert not passwordCheck('124A!')
    assert not passwordCheck('Abv%')
    assert flexiblePasswordCheck('THE123!')
    assert flexiblePasswordCheck('1M!')
    assert flexiblePasswordCheck('1Qb')
    assert flexiblePasswordCheck('b1B')
    assert not flexiblePasswordCheck('BBBBBBB!')
    assert not flexiblePasswordCheck('AAAAAAAb')
    assert not flexiblePasswordCheck('CCCC3')
    assert not flexiblePasswordCheck('ABDDEETG')
   
if __name__ == "__main__":
    main()    