# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 22:09:37 2020

@author: Logan Rowe

Check if all digits of the given integer are even.

Example

For n = 248622, the output should be
evenDigitsOnly(n) = true;
For n = 642386, the output should be
evenDigitsOnly(n) = false.
Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

Guaranteed constraints:
1 ≤ n ≤ 109.

[output] boolean

true if all digits of n are even, false otherwise.
[Python3] Syntax Tips
"""

def evenDigitsOnly(n):
    n=str(n)
    for integer in n:
        if integer%2!=0:
            return False
    return Truedef evenDigitsOnly(n):
    n=str(n)
    for integer in n:
        if int(integer)%2!=0:
            return False
    return True