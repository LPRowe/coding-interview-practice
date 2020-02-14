# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 16:18:50 2020

@author: Logan Rowe

Given an integer product, find the smallest positive (i.e. greater than 0) 
integer the product of whose digits is equal to product. If there is no such 
integer, return -1 instead.

Example

For product = 12, the output should be
digitsProduct(product) = 26;
For product = 19, the output should be
digitsProduct(product) = -1.
Input/Output

[execution time limit] 4 seconds (py3)

[input] integer product

Guaranteed constraints:
0 ≤ product ≤ 600.

[output] integer
"""

'''
Thoughts:
    
Let us start with a brute force approach and look for simplifications along the way

1) find all combinations numbers that multiply to equal the given product
2) concatenate the values in each combination
3) return the smallest int(combination))
    
    
This question has a 70% disapproval rating.  Likely because of the way it is worded.

digitsProduct_codesignal will try to meet codesignals interpretation of the question

in my test example below: code signal says 243 should go to 399 instead of 279
furthermore that 450 should go to 2559 instead of 509

these are in direct violation of their example 12 --> 26 which should be 223 according
to codesignal

props to bandorthild for this solution
'''

def digitsProduct(product):
    if product == 0: 
        return 10
    
    for i in range(3600):
        a = 1
        for j in str(i):
            a *= int(j)
        if a == p: 
            return i
        
    return -1
    
    
if __name__=='__main__':
    numbers=[12,19,243,450]
    for number in numbers:
        print(str(number),':',digitsProduct(number))
        print()