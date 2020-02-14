# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 19:57:08 2020

@author: Logan Rowe

Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with 
digits so that each column, each row, and each of the nine 3 × 3 sub-grids that 
compose the grid contains all of the digits from 1 to 9.

This algorithm should check if the given grid of numbers represents a correct 
solution to Sudoku.

Example

For
grid = [[1, 3, 2, 5, 4, 6, 9, 8, 7],
        [4, 6, 5, 8, 7, 9, 3, 2, 1],
        [7, 9, 8, 2, 1, 3, 6, 5, 4],
        [9, 2, 1, 4, 3, 5, 8, 7, 6],
        [3, 5, 4, 7, 6, 8, 2, 1, 9],
        [6, 8, 7, 1, 9, 2, 5, 4, 3],
        [5, 7, 6, 9, 8, 1, 4, 3, 2],
        [2, 4, 3, 6, 5, 7, 1, 9, 8],
        [8, 1, 9, 3, 2, 4, 7, 6, 5]]
the output should be
sudoku(grid) = true;

For
grid = [[1, 3, 2, 5, 4, 6, 9, 2, 7],
        [4, 6, 5, 8, 7, 9, 3, 8, 1],
        [7, 9, 8, 2, 1, 3, 6, 5, 4],
        [9, 2, 1, 4, 3, 5, 8, 7, 6],
        [3, 5, 4, 7, 6, 8, 2, 1, 9],
        [6, 8, 7, 1, 9, 2, 5, 4, 3],
        [5, 7, 6, 9, 8, 1, 4, 3, 2],
        [2, 4, 3, 6, 5, 7, 1, 9, 8],
        [8, 1, 9, 3, 2, 4, 7, 6, 5]]
the output should be
sudoku(grid) = false.

The output should be false: each of the nine 3 × 3 sub-grids should contain all 
of the digits from 1 to 9.
These examples are represented on the image below.



Input/Output

[execution time limit] 4 seconds (py3)

[input] array.array.integer grid

A matrix representing 9 × 9 grid already filled with numbers from 1 to 9.

Guaranteed constraints:
grid.length = 9,
grid[i].length = 9,
1 ≤ grid[i][j] ≤ 9.

[output] boolean

true if the given grid represents a correct solution to Sudoku, false otherwise.
"""

import numpy as np
import string

def boxes(grid):
    boxes=[]
    for idx_x in range(3):
        for idx_y in range(3):
            boxes.append([grid[3*idx_y:3*(idx_y+1),3*idx_x:3*(idx_x+1)]])
    return(boxes)
    
def sudoku(grid):
    grid=np.array(grid)
    
    digits=string.digits[1:]
    digits=[int(digit) for digit in digits]
    
    #check each row 
    for row in grid:
        row=row.tolist()
        for number in digits:
            if number not in row:
                return False
    
    #check each column
    for column in np.transpose(grid):
        column=column.tolist()
        for number in digits:
            if number not in column:
                return False
            
    #check each box
    for box in boxes(grid):
        box=np.reshape(box,(-1,))
        print(box)
        for number in digits:
            if number not in box:
                return False
    
    return(True)
    
if __name__=='__main__':
    grid = [[1, 3, 2, 5, 4, 6, 9, 8, 7],
        [4, 6, 5, 8, 7, 9, 3, 2, 1],
        [7, 9, 8, 2, 1, 3, 6, 5, 4],
        [9, 2, 1, 4, 3, 5, 8, 7, 6],
        [3, 5, 4, 7, 6, 8, 2, 1, 9],
        [6, 8, 7, 1, 9, 2, 5, 4, 3],
        [5, 7, 6, 9, 8, 1, 4, 3, 2],
        [2, 4, 3, 6, 5, 7, 1, 9, 8],
        [8, 1, 9, 3, 2, 4, 7, 6, 5]]
    print(sudoku(grid))