# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 00:00:52 2020

@author: Logan Rowe

We define the middle of the array arr as follows:

if arr contains an odd number of elements, its middle is the element whose index number is the same when counting from the beginning of the array and from its end;
if arr contains an even number of elements, its middle is the sum of the two elements whose index numbers when counting from the beginning and from the end of the array differ by one.
An array is called smooth if its first and its last elements are equal to one another and to the middle. Given an array arr, determine if it is smooth or not.

Example

For arr = [7, 2, 2, 5, 10, 7], the output should be
isSmooth(arr) = true.

The first and the last elements of arr are equal to 7, and its middle also equals 2 + 5 = 7. Thus, the array is smooth and the output is true.

For arr = [-5, -5, 10], the output should be
isSmooth(arr) = false.

The first and middle elements are equal to -5, but the last element equals 10. Thus, arr is not smooth and the output is false.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer arr

The given array.

Guaranteed constraints:
2 ≤ arr.length ≤ 105,
-109 ≤ arr[i] ≤ 109.

[output] boolean

true if arr is smooth, false otherwise.
[Python3] Syntax Tips
"""

import numpy as np
def isSmooth(arr):
    if arr[0]!=arr[-1]:
        return False
    if arr==[]:
        return True
    elif len(arr)%2==1:
        if arr[0]==arr[-1] and arr[0]==arr[int(0.5*len(arr))]:
            return True
    elif len(arr)%2==0:
        if arr[0]==arr[-1] and arr[0]==int(np.sum(arr[int(0.5*len(arr))-1:int(0.5*len(arr))+1])):
            return True
    return False