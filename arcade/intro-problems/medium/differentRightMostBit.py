# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 00:53:53 2020

@author: Logan Rowe

Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
You're given two integers, n and m. Find position of the rightmost bit in which they differ in their binary representations (it is guaranteed that such a bit exists), counting from right to left.

Return the value of 2position_of_the_found_bit (0-based).

Example

For n = 11 and m = 13, the output should be
differentRightmostBit(n, m) = 2.

1110 = 10112, 1310 = 11012, the rightmost bit in which they differ is the bit at position 1 (0-based) from the right in the binary representations.
So the answer is 21 = 2.

For n = 7 and m = 23, the output should be
differentRightmostBit(n, m) = 16.

710 = 1112, 2310 = 101112, i.e.

00111
10111
So the answer is 24 = 16.

Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

Guaranteed constraints:
0 ≤ n ≤ 230.

[input] integer m

Guaranteed constraints:
0 ≤ m ≤ 230,
n ≠ m.

[output] integer
"""

def differentRightmostBit_long(n, m):
    n=bin(n)[2:][::-1]
    m=bin(m)[2:][::-1]
    p=[int(i[0])^int(i[1]) for i in zip(m,n)]

    
    return 2**p.index(1) if 1 in p else 2**min(len(n)+1,len(m)+1)

def differentRightmostBit(n, m):
    return 2**[int(i[0])^int(i[1]) for i in zip(bin(m)[2:][::-1],bin(n)[2:][::-1])].index(1) if 1 in [int(i[0])^int(i[1]) for i in zip(bin(m)[2:][::-1],bin(n)[2:][::-1])] else 2**min(len(bin(n)[2:][::-1])+1,len(bin(m)[2:][::-1])+1)


if __name__=='__main__':
    n=[11,7,1]
    m=[13,23,0]
    ans=[2,16,1]
    for (i,j) in zip(n,m):
        print(differentRightmostBit(i,j))
