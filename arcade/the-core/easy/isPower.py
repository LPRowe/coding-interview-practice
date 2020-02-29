# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 23:27:44 2020

@author: Logan Rowe

Determine if the given number is a power of some non-negative integer.

Example

For n = 125, the output should be
isPower(n) = true;
For n = 72, the output should be
isPower(n) = false.
Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

A positive integer.

Guaranteed constraints:
1 ≤ n ≤ 400.

[output] boolean

true if n can be represented in the form ab (a to the power of b) where a and b are some non-negative integers and b ≥ 2, false otherwise.
"""

'''

Thoughts:
    
    n<=400 so lets check all possible powers from 2 to 20
    
    
'''

def isPower(n):
    for pow in range(2,21):
        if round(n**(pow**-1),10)==int(round(n**(pow**-1),10)):
            return True
    return False

print(isPower(125))
print(isPower(72))