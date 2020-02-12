# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 15:22:54 2020

@author: Logan Rowe

CodeMaster has just returned from shopping. He scanned the check of the items 
he bought and gave the resulting string to Ratiorg to figure out the total 
number of purchased items. Since Ratiorg is a bot he is definitely going to 
automate it, so he needs a program that sums up all the numbers which appear 
in the given input.

Help Ratiorg by writing a function that returns the sum of numbers that appear 
in the given inputString.

Example

For inputString = "2 apples, 12 oranges", the output should be
sumUpNumbers(inputString) = 14.

Input/Output

[execution time limit] 4 seconds (py3)

[input] string inputString

Guaranteed constraints:
0 ≤ inputString.length ≤ 105.

[output] integer
"""

import string

def sumUpNumbers(inputString):
    #Let us filter out all non-digit values without breaking up the given numbers
    numbers=''
    for character in inputString:
        if character in string.digits:
            numbers+=character
        else:
            numbers+=','
            
    #now lets convert all numbers to integers and add them up    
    total=sum([int(char) for char in numbers.split(',') if char!=''])
    
    return(total)
    
if __name__=='__main__':
    print(sumUpNumbers("2 apples, 12 oranges"))