# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 23:11:04 2020

@author: Logan Rowe
Given a sorted array of integers a, your task is to determine which element of 
a is closest to all other values of a. In other words, find the element x in a, 
which minimizes the following sum:

abs(a[0] - x) + abs(a[1] - x) + ... + abs(a[a.length - 1] - x)
(where abs denotes the absolute value)

If there are several possible answers, output the smallest one.

Example

For a = [2, 4, 7], the output should be absoluteValuesSumMinimization(a) = 4.

for x = 2, the value will be abs(2 - 2) + abs(4 - 2) + abs(7 - 2) = 7.
for x = 4, the value will be abs(2 - 4) + abs(4 - 4) + abs(7 - 4) = 5.
for x = 7, the value will be abs(2 - 7) + abs(4 - 7) + abs(7 - 7) = 8.
The lowest possible value is when x = 4, so the answer is 4.

For a = [2, 3], the output should be absoluteValuesSumMinimization(a) = 2.

for x = 2, the value will be abs(2 - 2) + abs(3 - 2) = 1.
for x = 3, the value will be abs(2 - 3) + abs(3 - 3) = 1.
Because there is a tie, the smallest x between x = 2 and x = 3 is the answer.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer a

A non-empty array of integers, sorted in ascending order.

Guaranteed constraints:
1 ≤ a.length ≤ 1000,
-106 ≤ a[i] ≤ 106.

[output] integer

An integer representing the element from a that minimizes the sum of its 
absolute differences with all other elements.
"""

import numpy as np

def fcn(a,idx):
    '''
    evalutate function at a[idx]
    '''
    f=0
    x=a[idx]
    for element in a:
        f+=abs(element-x)
    return(f)

def absoluteValuesSumMinimization(a):
    #all functions evaluated at a[idx]
    sums=[fcn(a,idx) for idx in range(len(a))]
    
    #convert to an array because a will likely be given as a list
    a=np.array(a)
    
    #return the smallest value in array a that minimizes the function
    return(np.min(a[np.where(sums==np.min(sums))]))
    
    