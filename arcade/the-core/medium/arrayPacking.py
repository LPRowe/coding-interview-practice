# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 13:09:37 2020

@author: Logan Rowe

You are given an array of up to four non-negative integers, each less than 256.

Your task is to pack these integers into one number M in the following way:

The first element of the array occupies the first 8 bits of M;
The second element occupies next 8 bits, and so on.
Return the obtained integer M.

Note: the phrase "first bits of M" refers to the least significant bits of 
M - the right-most bits of an integer. For further clarification see the following example.

Example

For a = [24, 85, 0], the output should be
arrayPacking(a) = 21784.

An array [24, 85, 0] looks like [00011000, 01010101, 00000000] in binary.
After packing these into one number we get 00000000 01010101 00011000 
(spaces are placed for convenience), which equals to 21784.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer a

Guaranteed constraints:
1 ≤ a.length ≤ 4,
0 ≤ a[i] < 256.

[output] integer
"""

def arrayPacking(a):
    M=''
    leading_zeros='0'*8
    for value in a[::-1]:
        binary_value=bin(value)[2:]
        M+=leading_zeros[:-len(binary_value)]+binary_value
    return(int(M,2))
    

if __name__=='__main__':
    a = [24, 85, 0]
    print(arrayPacking(a))