# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 00:46:50 2020

@author: Logan Rowe

Sudoku is a number-placement puzzle. 
The objective is to fill a 9 × 9 grid with numbers in such a way that each 
column, each row, and each of the nine 3 × 3 sub-grids that compose the grid 
all contain all of the numbers from 1 to 9 one time.

Implement an algorithm that will check whether the given grid of numbers 
represents a valid Sudoku puzzle according to the layout rules described above. 
Note that the puzzle represented by grid does not have to be solvable.

grid = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
        ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
        ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
        ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
        ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
        ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
        ['.', '.', '.', '5', '.', '.', '.', '7', '.']]

the output should be
sudoku2(grid) = true;

grid = [['.', '.', '.', '.', '2', '.', '.', '9', '.'],
        ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
        ['7', '1', '.', '.', '7', '5', '.', '.', '.'],
        ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
        ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
        ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
        ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
        ['.', '2', '.', '.', '3', '.', '.', '.', '.']]
the output should be
sudoku2(grid) = false.
"""

'''
thoughts:

I feel that there is a more elegant solution at hand...

but simply checking the rows, checking the columns, then checking each
3 by 3 sub-region for any duplicate numbers (or any values that are not 1 - 9)
seems straight forward and fast enough considering all tested sudokus will only
be 9 by 9


net coding time: 45 minutes
'''

import numpy as np
from itertools import product

def sudoku2(grid):
    grid=np.array(grid)
    # =============================================================================
    # Check Rows
    # =============================================================================
    for row in grid:
        values=set(row)
        values.discard('.')
        if values!=None:
            values=list(values)
            for value in values:
                if list(row).count(value)>1:
                    print('row failure')
                    return(False)

    # =============================================================================
    # Check Columns
    # =============================================================================
    columns=[grid[:,i] for i in range(grid.shape[0])]
    for column in columns:
        values=set(column)
        values.discard('.')
        if values!=None:
            values=list(values)
            for value in values:
                if list(column).count(value)>1:
                    print('column failure')
                    return(False)

    # =============================================================================
    # Check Boxes
    # =============================================================================
    dx,dy=3,3 #the length and height of each smaller box
    boxes=[grid[i*dx:(i+1)*dx,j*dy:(j+1)*dy] for (i,j) in product(range(0,3),range(0,3))]
    for box in boxes:
        values=set(box.reshape(-1,))
        values.discard('.')
        if values!=None:
            values=list(values)
            for value in values:
                if list(box.reshape(-1,)).count(value)>1:
                    print('box failure')
                    return(False)
    
    return True
    
if __name__ == '__main__':
    grid1=[['.', '.', '.', '1', '4', '.', '.', '2', '.'],
        ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
        ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
        ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
        ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
        ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
        ['.', '.', '.', '5', '.', '.', '.', '7', '.']]
    
    grid2=[['.', '.', '.', '.', '2', '.', '.', '9', '.'],
        ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
        ['7', '1', '.', '.', '7', '5', '.', '.', '.'],
        ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
        ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
        ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
        ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
        ['.', '2', '.', '.', '3', '.', '.', '.', '.']]
    
    print(sudoku2(grid1))
    print()
    print(sudoku2(grid2))
