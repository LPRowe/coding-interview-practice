# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 01:30:44 2020

@author: Logan Rowe

You are given an array of integers representing coordinates of obstacles 
situated on a straight line.

Assume that you are jumping from the point with coordinate 0 to the right. 
You are allowed only to make jumps of the same length represented by some integer.

Find the minimal length of the jump enough to avoid all the obstacles.

Example

For inputArray = [5, 3, 6, 7, 9], the output should be
avoidObstacles(inputArray) = 4.

Check out the image below for better understanding:



Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer inputArray

Non-empty array of positive integers.

Guaranteed constraints:
2 ≤ inputArray.length ≤ 1000,
1 ≤ inputArray[i] ≤ 1000.

[output] integer

The desired length.
"""

import numpy as np

def avoidObstacles(inputArray):
    inputArray=np.array(inputArray)
    
    hop=2
    while 0 in inputArray%hop:
        hop+=1
    
    return hop
        
    
    
    
    
if __name__=='__main__':
    inputArray=[5, 3, 6, 7, 9]
    print(avoidObstacles(inputArray))