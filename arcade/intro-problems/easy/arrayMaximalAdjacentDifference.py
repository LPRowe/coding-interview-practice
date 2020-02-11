# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 01:12:01 2020

@author: Logan Rowe

Given an array of integers, find the maximal absolute difference between any 
two of its adjacent elements.

Example

For inputArray = [2, 4, 1, 0], the output should be
arrayMaximalAdjacentDifference(inputArray) = 3.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer inputArray

Guaranteed constraints:
3 ≤ inputArray.length ≤ 10,
-15 ≤ inputArray[i] ≤ 15.

[output] integer

The maximal absolute difference.
"""

import numpy as np

def arrayMaximalAdjacentDifference(inputArray):
    inputArray=np.array(inputArray)
    diff=inputArray[1:]-inputArray[:-1]
    
    minimum=min(diff)
    maximum=max(diff)
    
    if -minimum>maximum:
        return(-minimum)
    else:
        return(maximum)