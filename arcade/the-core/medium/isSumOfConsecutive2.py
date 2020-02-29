# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 23:40:11 2020

@author: Logan Rowe

Find the number of ways to express n as sum of some (at least two) consecutive positive integers.

Example

For n = 9, the output should be
isSumOfConsecutive2(n) = 2.

There are two ways to represent n = 9: 2 + 3 + 4 = 9 and 4 + 5 = 9.

For n = 8, the output should be
isSumOfConsecutive2(n) = 0.

There are no ways to represent n = 8.

Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

A positive integer.

Guaranteed constraints:
1 ≤ n ≤ 104.

[output] integer
"""

def isSumOfConsecutive2(n):
    possible_combinations=0
    start=int(n/2)+2
    tail=start
    numbers=[]
    while start>=0:
        if sum(numbers)>n or tail<=0:
            numbers=[]
            start-=1
            tail=start
        elif sum(numbers)<n:
            numbers.append(tail-1)
            tail-=1
        else:
            numbers=[]
            possible_combinations+=1
            start-=1
            tail=start
    return(possible_combinations)                
    
print(isSumOfConsecutive2(9))
print(isSumOfConsecutive2(8))