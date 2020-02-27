# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 00:57:29 2020

@author: Logan Rowe

Given integers n, l and r, find the number of ways to represent n as a sum of two integers A and B such that l ≤ A ≤ B ≤ r.

Example

For n = 6, l = 2, and r = 4, the output should be
countSumOfTwoRepresentations2(n, l, r) = 2.

There are just two ways to write 6 as A + B, where 2 ≤ A ≤ B ≤ 4: 6 = 2 + 4 and 6 = 3 + 3.

Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

A positive integer.

Guaranteed constraints:
5 ≤ n ≤ 109.

[input] integer l

A positive integer.

Guaranteed constraints:
1 ≤ l ≤ r.

[input] integer r

A positive integer.

Guaranteed constraints:
l ≤ r ≤ 109,
r - l ≤ 106.

[output] integer
"""

def countSumOfTwoRepresentations2(n, l, r):
    if n<2*l or n>2*r:
        return 0
    if n==2*l or n==2*r:
        return 1

    middle=int(0.5*l+r)
    if n>l+r:
        while l+r!=n:
            l+=1
    else:
        while l+r!=n:
            r-=1
    return(int(0.5*(r-l))+1)
    
    

if __name__=='__main__':
    n_=[6,6]
    l_=[4,3]
    r_=[2,3]
    a_=[2,1]
    for (n,l,r,a) in zip(n_,l_,r_,a_):
        print(countSumOfTwoRepresentations2(n,l,r))
    
