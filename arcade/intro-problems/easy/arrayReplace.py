# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 20:13:26 2020

@author: Logan Rowe

Given an array of integers, replace all the occurrences of elemToReplace with 
substitutionElem.

Example

For inputArray = [1, 2, 1], elemToReplace = 1, and substitutionElem = 3, 
the output should be
arrayReplace(inputArray, elemToReplace, substitutionElem) = [3, 2, 3].

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer inputArray

Guaranteed constraints:
0 ≤ inputArray.length ≤ 104,
0 ≤ inputArray[i] ≤ 109.

[input] integer elemToReplace

Guaranteed constraints:
0 ≤ elemToReplace ≤ 109.

[input] integer substitutionElem

Guaranteed constraints:
0 ≤ substitutionElem ≤ 109.

[output] array.integer
"""

import numpy as np
def arrayReplace(inputArray, elemToReplace, substitutionElem):
    inputArray=np.array(inputArray)
    inputArray[inputArray==elemToReplace]=substitutionElem
    return(inputArray) 
    
if __name__=='__main__':
    inputArray=np.array([1,2,1])
    elemToReplace=1
    substitutionElem=3
    print(arrayReplace(inputArray,elemToReplace,substitutionElem))