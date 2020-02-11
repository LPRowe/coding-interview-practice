# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 17:24:15 2020

@author: Logan Rowe

Given an array of strings, return another array containing all of its longest strings.

Example

For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
allLongestStrings(inputArray) = ["aba", "vcd", "aba"].

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.string inputArray

A non-empty array.

Guaranteed constraints:
1 ≤ inputArray.length ≤ 10,
1 ≤ inputArray[i].length ≤ 10.

[output] array.string

Array of the longest strings, stored in the same order as in the inputArray.
"""

def allLongestStrings(inputArray):
    #Find the longest string in the input array
    L=[len(string) for string in inputArray]
    L=max(L)
    
    #Make a new array consisting of the longest strings in the initial array
    new_L=[string for string in inputArray if len(string)==L]
    
    return(new_L)