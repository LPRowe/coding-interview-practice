# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 15:07:00 2020

@author: Logan Rowe

Given some integer, find the maximal number you can obtain by deleting 
exactly one digit of the given number.

Example

For n = 152, the output should be
deleteDigit(n) = 52;
For n = 1001, the output should be
deleteDigit(n) = 101.
Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

Guaranteed constraints:
10 ≤ n ≤ 106.

[output] integer
"""

def deleteDigit(n):
    n=str(n)
    possible_numbers=[int(n[:idx]+n[idx+1:]) for idx in range(len(n))]
    return(max(possible_numbers))
    
    
    
    
if __name__=='__main__':
    test_digits=[152,1001]
    for digit in test_digits:
        print(deleteDigit(digit))