# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 16:19:30 2020

@author: Logan Rowe

Find the leftmost digit that occurs in a given string.

Example

For inputString = "var_1__Int", the output should be
firstDigit(inputString) = '1';
For inputString = "q2q-q", the output should be
firstDigit(inputString) = '2';
For inputString = "0ss", the output should be
firstDigit(inputString) = '0'.
Input/Output

[execution time limit] 4 seconds (py3)

[input] string inputString

A string containing at least one digit.

Guaranteed constraints:
3 ≤ inputString.length ≤ 10.

[output] char
"""

import string

def firstDigit(inputString):
    digits=string.digits
    for character in inputString:
        if character in digits:
            return character