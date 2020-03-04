# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 10:48:29 2020

@author: Logan Rowe

Let's say that number a feels comfortable with number b if a ≠ b and b lies in the segment [a - s(a), a + s(a)], where s(x) is the sum of x's digits.

How many pairs (a, b) are there, such that a < b, both a and b lie on the segment [l, r], and each number feels comfortable with the other (so a feels comfortable with b and b feels comfortable with a)?

Example

For l = 10 and r = 12, the output should be
comfortableNumbers(l, r) = 2.

Here are all values of s(x) to consider:

s(10) = 1, so 10 is comfortable with 9 and 11;
s(11) = 2, so 11 is comfortable with 9, 10, 12 and 13;
s(12) = 3, so 12 is comfortable with 9, 10, 11, 13, 14 and 15.
Thus, there are 2 pairs of numbers comfortable with each other within the segment [10; 12]: (10, 11) and (11, 12).

Input/Output

[execution time limit] 4 seconds (py3)

[input] integer l

Guaranteed constraints:
1 ≤ l ≤ r ≤ 1000.

[input] integer r

Guaranteed constraints:
1 ≤ l ≤ r ≤ 1000.

[output] integer

The number of pairs satisfying all the above conditions.
"""

def comfortablePairs(a,l,r):
    xr = sum([int(i) for i in str(a)])
    ub = a + xr
    lb = a - xr
    return [i for i in range(max(lb,l),min(ub+1,r+1))]

def mutuallyComfortable(a,b,comfortable_dict):
    try:
        return ((a in comfortable_dict[b]) and (b in comfortable_dict[a]) and a<b)
    except:
        return False


def comfortableNumbers(l, r):
    comfortable_dict = {}
    # Since b must be greater than a  and a>1 find all a+s(a) and ignore all a-s(a)
    for num in range(l, r+1):
        comfortable_dict[num] = comfortablePairs(num,l,r)
    
    comfortable_pairs=0
    for key in comfortable_dict:
        for val in comfortable_dict[key]:
            if mutuallyComfortable(key,val,comfortable_dict):
                comfortable_pairs+=1
    return comfortable_pairs



print(comfortableNumbers(10,12))
print(comfortableNumbers(12,108))