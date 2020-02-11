# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 22:44:51 2020

@author: Logan Rowe

Given two cells on the standard chess board, determine whether they have the 
same color or not.

Example

For cell1 = "A1" and cell2 = "C3", the output should be
chessBoardCellColor(cell1, cell2) = true.



For cell1 = "A1" and cell2 = "H3", the output should be
chessBoardCellColor(cell1, cell2) = false.



Input/Output

[execution time limit] 4 seconds (py3)

[input] string cell1

Guaranteed constraints:
cell1.length = 2,
'A' ≤ cell1[0] ≤ 'H',
1 ≤ cell1[1] ≤ 8.

[input] string cell2

Guaranteed constraints:
cell2.length = 2,
'A' ≤ cell2[0] ≤ 'H',
1 ≤ cell2[1] ≤ 8.

[output] boolean

true if both cells have the same color, false otherwise.
"""

def chessBoardCellColor(cell1, cell2):
    #let us use an odd or even method here
    
    #if letter and number are both odd or both even then dark
    #but if one is odd and the other even then light
    
    letter_to_number={
            'A':1,
            'B':2,
            'C':1,
            'D':2,
            'E':1,
            'F':2,
            'G':1,
            'H':2
            }
    
    if letter_to_number[cell1[0]]%2==int(cell1[1])%2:
        cell1='dark'
    else:
        cell1='light'
        
    if letter_to_number[cell2[0]]%2==int(cell2[1])%2:
        cell2='dark'
    else:
        cell2='light'
    
    if cell1==cell2:
        return True
    else:
        return False