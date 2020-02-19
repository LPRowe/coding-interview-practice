# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 11:32:55 2020

@author: Logan Rowe

Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
You're given an arbitrary 32-bit integer n. Take its binary representation, split bits into it in pairs (bit number 0 and 1, bit number 2 and 3, etc.) and swap bits in each pair. Then return the result as a decimal number.

Example

For n = 13, the output should be
swapAdjacentBits(n) = 14.

1310 = 11012 ~> {11}{01}2 ~> 11102 = 1410.

For n = 74, the output should be
swapAdjacentBits(n) = 133.

7410 = 010010102 ~> {01}{00}{10}{10}2 ~> 100001012 = 13310.
Note the preceding zero written in front of the initial number: since both numbers are 32-bit integers, they have 32 bits in their binary representation. The preceding zeros in other cases don't matter, so they are omitted. Here, however, it does make a difference.

Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

Guaranteed constraints:
0 ≤ n < 230.

[output] integer
"""

def swapAdjacentBits_multiline(n):
    pref=bin(n).split('b')[0]+'b'
    suff=bin(n).split('b')[1][::-1]+'0'*len(bin(n).split('b')[1])
    val=pref+''.join([suff[2*idx:2*idx+2][::-1] for idx in range(int(0.5*len(bin(n))))])[::-1]
    return int(val,2)

def swapAdjacentBits(n):
    return int(bin(n).split('b')[0]+'b'+''.join([str(bin(n).split('b')[1][::-1]+'0'*len(bin(n).split('b')[1]))[2*idx:2*idx+2][::-1] for idx in range(int(0.5*len(bin(n))))])[::-1],2)

if __name__=='__main__':
    vals=[13,74]
    output=[14,133]
    for n,out in zip(vals,output):
        print(swapAdjacentBits(n))
        print(swapAdjacentBits(n)==out)
        print()
