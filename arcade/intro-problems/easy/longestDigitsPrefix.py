# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 17:19:34 2020

@author: Logan Rowe

Given a string, output its longest prefix which contains only digits.

Example

For inputString = "123aa1", the output should be
longestDigitsPrefix(inputString) = "123".

Input/Output

[execution time limit] 4 seconds (py3)

[input] string inputString

Guaranteed constraints:
3 ≤ inputString.length ≤ 100.

[output] string

[Python3] Syntax Tips
"""
import string

def longestDigitsPrefix(inputString):
    idx=0
    digits=string.digits
    for character in inputString:
        if character in digits:
            idx+=1
        else:
            break
    
    return(inputString[:idx])