# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 00:51:01 2020

@author: Logan Rowe

You are given an array of integers. On each move you are allowed to increase 
exactly one of its element by one. Find the minimal number of moves required 
to obtain a strictly increasing sequence from the input.

Example

For inputArray = [1, 1, 1], the output should be
arrayChange(inputArray) = 3.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer inputArray

Guaranteed constraints:
3 ≤ inputArray.length ≤ 105,
-105 ≤ inputArray[i] ≤ 105.

[output] integer

The minimal number of moves needed to obtain a strictly increasing 
sequence from inputArray.
It's guaranteed that for the given test cases the answer always fits signed 
32-bit integer type.
"""

'''
Thoughts:
    
lets pass once through the array storing theminimum previous value as prev
and the increments to reach that value will be added to a counter

'''

def arrayChange(inputArray):
    moves=0
    
    prev=inputArray[0]
    for value in inputArray[1:]:
        if value<prev+1:
            moves+=(prev+1)-value
            prev+=1
        else:
            prev=value
    
    return(moves)