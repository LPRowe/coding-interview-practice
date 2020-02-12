# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 17:24:06 2020

@author: Logan Rowe

Let's define digit degree of some positive integer as the number of times we 
need to replace this number with the sum of its digits until we get to a 
one digit number.

Given an integer, find its digit degree.

Example

For n = 5, the output should be
digitDegree(n) = 0;
For n = 100, the output should be
digitDegree(n) = 1.
1 + 0 + 0 = 1.
For n = 91, the output should be
digitDegree(n) = 2.
9 + 1 = 10 -> 1 + 0 = 1.
Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

Guaranteed constraints:
5 ≤ n ≤ 109.

[output] integer
"""

def digitDegree(n):
    if len(str(n))==1:
        return(0)

    cycle=0
    while len(str(n))>1:
        n=sum([int(digit) for digit in str(n)])
        cycle+=1
    
    return(cycle)