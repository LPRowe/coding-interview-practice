# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 01:20:09 2020

@author: Logan Rowe

Consider integer numbers from 0 to n - 1 written down along the circle in such a way that the distance between any two neighboring numbers is equal (note that 0 and n - 1 are neighboring, too).

Given n and firstNumber, find the number which is written in the radially opposite position to firstNumber.

Example

For n = 10 and firstNumber = 2, the output should be
circleOfNumbers(n, firstNumber) = 7.



Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

A positive even integer.

Guaranteed constraints:
4 ≤ n ≤ 20.

[input] integer firstNumber

Guaranteed constraints:
0 ≤ firstNumber ≤ n - 1.

[output] integer
"""

def circleOfNumbers(n, firstNumber):
    if firstNumber+int(n/2)>=n:
        return(firstNumber-int(n/2))
    return firstNumber+int(n/2)
