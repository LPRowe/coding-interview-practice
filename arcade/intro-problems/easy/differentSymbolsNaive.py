# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 16:22:22 2020

@author: Logan Rowe

Given a string, find the number of different characters in it.

Example

For s = "cabca", the output should be
differentSymbolsNaive(s) = 3.

There are 3 different characters a, b and c.

Input/Output

[execution time limit] 4 seconds (py3)

[input] string s

A string of lowercase English letters.

Guaranteed constraints:
3 ≤ s.length ≤ 1000.

[output] integer
"""

def differentSymbolsNaive(s):
    return(len(set(s)))
