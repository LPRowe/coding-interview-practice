# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 22:46:03 2020

@author: Logan Rowe

Ticket numbers usually consist of an even number of digits. A ticket number is 
considered lucky if the sum of the first half of the digits is equal to the sum 
of the second half.

Given a ticket number n, determine if it's lucky or not.

Example

For n = 1230, the output should be
isLucky(n) = true;
For n = 239017, the output should be
isLucky(n) = false.
Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

A ticket number represented as a positive integer with an even number of digits.

Guaranteed constraints:
10 ≤ n < 106.

[output] boolean

true if n is a lucky ticket number, false otherwise.
"""

def isLucky(n):
    n=str(n)
    
    #split n into first and second half and make a list containing each number
    first_half=[int(i) for i in n[:int(len(n)/2)]]
    second_half=[int(i) for i in n[int(len(n)/2):]]

    #Check if the sum of the first_half numbers equals the sum of the second_half numbers
    if sum(first_half)==sum(second_half):
        return True
    else:
        return False
     
if __name__=='__main__':
    n=1230
    isLucky(n)