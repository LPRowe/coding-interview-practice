# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 22:23:31 2020

@author: Logan Rowe

Given a string, your task is to replace each of its characters by the next 
one in the English alphabet; i.e. replace a with b, replace b with c, etc 
(z would be replaced by a).

Example

For inputString = "crazy", the output should be alphabeticShift(inputString) = "dsbaz".

Input/Output

[execution time limit] 4 seconds (py3)

[input] string inputString

A non-empty string consisting of lowercase English characters.

Guaranteed constraints:
1 ≤ inputString.length ≤ 1000.

[output] string

The resulting string after replacing each of its characters.
"""

import string

def alphabeticShift(inputString):
    alphabet=string.ascii_lowercase
    alphabet_shifted=alphabet[-1]+alphabet[:-1]
    
    alphabet_dict={}
    for (i,j) in zip(alphabet,alphabet_shifted):
        alphabet_dict[j]=i
    
    outputString=''.join([alphabet_dict[letter] for letter in inputString])
    
    return outputString

print(alphabeticShift('crazy'))