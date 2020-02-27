# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 23:28:48 2020

@author: Logan Rowe

Given an integer n, find the minimal k such that

k = m! (where m! = 1 * 2 * ... * m) for some integer m;
k >= n.
In other words, find the smallest factorial which is not less than n.

Example

For n = 17, the output should be
leastFactorial(n) = 24.

17 < 24 = 4! = 1 * 2 * 3 * 4, while 3! = 1 * 2 * 3 = 6 < 17).

Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

A positive integer.

Guaranteed constraints:
1 ≤ n ≤ 120.

[output] integer
"""

def leastFactorial(n):
    i=1
    val=1
    while val<n:
        i+=1
        val*=i
    return val 

