# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 15:33:49 2020

@author: Logan Rowe

Given a rectangular matrix containing only digits, calculate the number of 
different 2 × 2 squares in it.

Example

For

matrix = [[1, 2, 1],
          [2, 2, 2],
          [2, 2, 2],
          [1, 2, 3],
          [2, 2, 1]]
the output should be
differentSquares(matrix) = 6.

Here are all 6 different 2 × 2 squares:

1 2
2 2
2 1
2 2
2 2
2 2
2 2
1 2
2 2
2 3
2 3
2 1
Input/Output

[execution time limit] 4 seconds (py3)

[input] array.array.integer matrix

Guaranteed constraints:
1 ≤ matrix.length ≤ 100,
1 ≤ matrix[i].length ≤ 100,
0 ≤ matrix[i][j] ≤ 9.

[output] integer

The number of different 2 × 2 squares in matrix.
"""

'''
The previous method that checked whether a sub-matrix was already seen was
too expensive (timewise)

This method adds tuples to a set and will be rejected if it is already in the set
'''

import numpy as np

def submatrix_from_matrix(matrix,row,column):
    return((matrix[row][column],matrix[row][column+1],matrix[row+1][column],matrix[row+1][column+1]))

def differentSquares(matrix):    
    height,width=np.array(matrix).shape
        
    #track all unique matrices with a list
    square_matrices=set()
    
    for row in range(height-1):
        for column in range(width-1):
            square_matrices.add(submatrix_from_matrix(matrix,row,column))
                    
    return(len(square_matrices))
    
    
if __name__=='__main__':
    matrix = [[1, 2, 1],
          [2, 2, 2],
          [2, 2, 2],
          [1, 2, 3],
          [2, 2, 1]]
    print(differentSquares(matrix))