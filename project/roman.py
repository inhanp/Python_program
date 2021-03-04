# roman.py
"""
Detect valid Roman numerals

Refer to the instructions on Canavs for more information.

"I have neither given nor received help on this assignment."
author: INHAN PARK
"""
__version__ = 1

def valid_numeral(test_case):
    
    if type(test_case) != str:
        return False
    
    num = 0
    
    bool_I = False
    bool_X = False
    
    #Check whether test_case is empty.
    #If empty, return False
    if not test_case:
        return False
    
    for ch in test_case:
        
        #If test_case contain space, return False
        if ch == " ":
            return False
        
        #If test_case contains other than I, V, X, L, C, D, M, return False
        if ch not in ["I", "V", "X", "L", "C", "D", "M"]:
            return False
        
        #If V, L, D are placed in sequence, return False
        if num >= 1:
            if ch == test_case[num - 1] and (ch == "V" or ch == "L" or ch =="D"):
                return False
        
        #If four same roman numbers are placed in sequence, return False
        if num >= 3:
            if ch == test_case[num - 3] and ch == test_case[num - 2] and ch == test_case[num - 1]:
                return False
            
        #Check whether larger roman number appear later than smaller number
        if num >= 1:
            #M cannot appear after I since M is larger than I
            if ch == "M" and bool_I:
                return False
            #M cannot appear after X since M is larger than X
            if ch == "M" and bool_X:
                return False
            #C cannot appear after I since C is larger than I
            if ch == "C" and bool_I:
                return False
            
        #Check whether I appeared in test_case
        if ch == "I" and not bool_I:
            bool_I = True
            
        #Check whether X appeared in test_case
        if ch == "X" and not bool_X:
            bool_X = True
        
        
        #Rule 5, 6
        if num >= 1:
            #Only C and M can appear before M
            if ch == "M" and test_case[num - 1] not in ["C", "M"] :
                return False
            #Only C and M can apppear before D
            elif ch == "D" and test_case[num - 1] not in ["C", "M"] :
                return False
            #I, V, L cannot appear before C
            elif ch == "C" and test_case[num - 1] in ["I", "V", "L"] :
                return False
            #I, V cannot appear before L
            elif ch == "L" and test_case[num - 1] in ["I", "V"] :
                return False
            #V cannot appear before X
            elif ch == "X" and test_case[num - 1] in ["V"] :
                return False
            
        if num >= 2:
            #If more than two I are in a row, no other roman number can come after it
            if test_case[num - 2] == "I" and test_case[num - 1] == "I" and ch != "I":
                return False
            #If more than two X are in a row, C cannot be after it
            if test_case[num - 2] == "X" and test_case[num - 1] == "X" and ch == "C":
                return False
            #If more than two C are in a row, M cannot be after it
            if test_case[num - 2] == "C" and test_case[num - 1] == "C" and ch == "M":
                return False
            pass
            
        num = num + 1
        
    return True


def main():
    testValidNumeral_1_1()
    testValidNumeral_1_2()
    testValidNumeral_2_1()
    testValidNumeral_3_1()
    testValidNumeral_5_1()
    testValidNumeral_6_1()
    testValidNumeral_7_1()
    testValidNumeral_4_1()
    pass



###############################################################

# Here is where you will write your test case functions
    
# If it receive empty string, return False
def testValidNumeral_1_1():
    assert valid_numeral("    ") == False, "empty string is invalid"
    assert valid_numeral("") == False, "empty string is invalid"

#If it receive other than alphabet, return False
def testValidNumeral_1_2():
    assert valid_numeral(1) == False, "Only receive alphabetic characters"
    assert valid_numeral("V1") == False, "Only receive alphabetic characters"

#If it receive characters other than I,V,X,L,C,D,M, return False
def testValidNumeral_2_1():
    assert valid_numeral("IAV") == False, "Only characters I, V, X, L, C, D, M"
    assert valid_numeral("MDCLXVIA") == False, "Only characters I, V, X, L, C, D, M"
    
#If string have 4 same characters in a row, return False
def testValidNumeral_3_1():
    assert valid_numeral("IIII") == False, "4 same characters in a row"
    assert valid_numeral("IVIIII") == False, "4 same characters in a row"
    assert valid_numeral("XXXX") == False, "4 same characters in a row"
    
#Characters in string should appear from largest to smallest
def testValidNumeral_4_1():
    assert valid_numeral("IIV") == False, "largest to smallest"
    assert valid_numeral("VL") == False, "Largest to smallest"
    assert valid_numeral("IXCM") == False, "Largest to smallest"
    assert valid_numeral("VM") == False, "Largest to smallest"
    
#Small valued symbol can be placed at the front of a large valued symbol
#only if that small value symbol is I, X, C, M.
def testValidNumeral_5_1():
    assert valid_numeral("IX") == True, "Can be at fron only if I, X, C, M"
    assert valid_numeral("IV") == True, "Can be at fron only if I, X, C, M"
    assert valid_numeral("XL") == True, "Can be at fron only if I, X, C, M"
    assert valid_numeral("XC") == True, "Can be at fron only if I, X, C, M"
    assert valid_numeral("CM") == True, "Can be at fron only if I, X, C, M"
    
#In a case of rule 5, only V and X can come after I, L and C after X, D and M after C.
def testValidNumeral_6_1():
    assert valid_numeral("IL") == False, "Can be at front of L and C only if X"
    assert valid_numeral("IC") == False, "Can be at front of L and C only if X"
    assert valid_numeral("ID") == False, "Can be at front of L and C only if X"
    assert valid_numeral("IM") == False, "Can be at front of L and C only if X"
    assert valid_numeral("XD") == False, "Can be at front of L and C only if X"
    assert valid_numeral("XM") == False, "Can be at front of L and C only if X"
    
#Only I, X, C, M can have a sequence of same symbols in a row (power of 10)
def testValidNumeral_7_1():
    assert valid_numeral("III") == True, "Only I, X, C, M can have a sequence in a row"
    assert valid_numeral("VVI") == False, "Only I, X, C, M can have a sequence in a row"
    assert valid_numeral("LL") == False, "Only I, X, C, M can have a sequence in a row"
    assert valid_numeral("DD") == False, "Only I, X, C, M can have a sequence in a row"

    
###############################################################    
    
if __name__ == "__main__":
    main()    