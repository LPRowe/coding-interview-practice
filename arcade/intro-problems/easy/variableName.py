# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 22:12:30 2020

@author: Logan Rowe

Correct variable names consist only of English letters, 
digits and underscores and they can't start with a digit.

Check if the given string is a correct variable name.

Example

For name = "var_1__Int", the output should be
variableName(name) = true;
For name = "qq-q", the output should be
variableName(name) = false;
For name = "2w2", the output should be
variableName(name) = false.
Input/Output

[execution time limit] 4 seconds (py3)

[input] string name

Guaranteed constraints:
1 ≤ name.length ≤ 10.

[output] boolean

true if name is a correct variable name, false otherwise.
"""

def variableName(name):
    #Check if the first character is an integer
    if name[0].isdigit():
        return False
    
    for letter in name:
        if letter.isalpha() or letter.isnumeric() or letter=='_':
            continue
        else:
            return False
    
    return True
            
    
    
    
if __name__=='__main__':
    names=["var_1__Int","qq-q","2w2"]
    results=[True,False,False]
    for (name,result) in zip(names,results):
        if variableName(name)==result:
            print('passed test')
        else:
            print(name)