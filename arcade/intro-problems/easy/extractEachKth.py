# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 16:07:30 2020

@author: Logan Rowe

Given array of integers, remove each kth element from it.

Example

For inputArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and k = 3, the output should be
extractEachKth(inputArray, k) = [1, 2, 4, 5, 7, 8, 10].

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer inputArray

Guaranteed constraints:
5 ≤ inputArray.length ≤ 15,
-20 ≤ inputArray[i] ≤ 20.

[input] integer k

Guaranteed constraints:
1 ≤ k ≤ 10.

[output] array.integer

inputArray without elements k - 1, 2k - 1, 3k - 1 etc.
"""
import numpy as np

def extractEachKth(inputArray, k):
    mask=[idx%k!=0 for idx in range(1,len(inputArray)+1)]

    inputArray=np.array(inputArray)
    outputArray=inputArray[mask]

    return outputArray