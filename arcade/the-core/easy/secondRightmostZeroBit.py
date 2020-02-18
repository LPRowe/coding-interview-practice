# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 12:40:20 2020

@author: Logan Rowe

Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
Presented with the integer n, find the 0-based position of the second rightmost zero bit in its binary representation (it is guaranteed that such a bit exists), counting from right to left.

Return the value of 2position_of_the_found_bit.

Example

For n = 37, the output should be
secondRightmostZeroBit(n) = 8.

3710 = 1001012. The second rightmost zero bit is at position 3 (0-based) from the right in the binary representation of n.
Thus, the answer is 23 = 8.

Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

Guaranteed constraints:
4 ≤ n ≤ 230.

[output] integer
"""



def secondRightmostZeroBit(n):
    n=bin(n)[2:][::-1]
    string1=n[:n.find('0')+1]
    n2=n[len(string1):]
    string2=n2[:n2.find('0')+1]
    power=len(string1)+len(string2)-1
    return 2**power

def secondRightmostZeroBit_oneLine(n):
    return 2**(len(bin(n)[2:][::-1][:bin(n)[2:][::-1].find('0')+1])+len(bin(n)[2:][::-1][len(bin(n)[2:][::-1][:bin(n)[2:][::-1].find('0')+1]):][:bin(n)[2:][::-1][len(bin(n)[2:][::-1][:bin(n)[2:][::-1].find('0')+1]):].find('0')+1])-1)

if __name__=='__main__':
    n=[37,1073741824,4]
    for val in n:
        print(secondRightmostZeroBit_oneLine(val))
        print()