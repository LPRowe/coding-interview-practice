# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 14:21:16 2020

@author: Logan Rowe

Determine if the given character is a digit or not.

Example

For symbol = '0', the output should be
isDigit(symbol) = true;
For symbol = '-', the output should be
isDigit(symbol) = false.
Input/Output

[execution time limit] 4 seconds (py3)

[input] char symbol

A character which is either a digit or not.

[output] boolean

true if symbol is a digit, false otherwise.
[Python3] Syntax Tips
"""

import string

def isDigit(symbol):
    if symbol in string.digits:
        return True
    return False