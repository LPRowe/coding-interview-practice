# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 16:27:34 2020

@author: Logan Rowe
Given array of integers, find the maximal possible sum of some of its k 
consecutive elements.

Example

For inputArray = [2, 3, 5, 1, 6] and k = 2, the output should be
arrayMaxConsecutiveSum(inputArray, k) = 8.
All possible sums of 2 consecutive elements are:

2 + 3 = 5;
3 + 5 = 8;
5 + 1 = 6;
1 + 6 = 7.
Thus, the answer is 8.
Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer inputArray

Array of positive integers.

Guaranteed constraints:
3 ≤ inputArray.length ≤ 105,
1 ≤ inputArray[i] ≤ 1000.

[input] integer k

An integer (not greater than the length of inputArray).

Guaranteed constraints:
1 ≤ k ≤ inputArray.length.

[output] integer

The maximal possible sum.
"""

import numpy as np

def arrayMaxConsecutiveSum(inputArray, k):
    max_sum=sum(inputArray[:k])

    curr_sum=sum(inputArray[:k])
    print(curr_sum)
    for first_value,new_value in zip(inputArray,inputArray[k:]):
        #instead of adding all three numbers every time, just update previous summation
        curr_sum+=new_value-first_value
        
        if curr_sum>max_sum:
            max_sum=curr_sum
    return(max_sum)