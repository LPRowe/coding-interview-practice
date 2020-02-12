# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 14:49:15 2020

@author: Logan Rowe

Given a position of a knight on the standard chessboard, find the number of 
different moves the knight can perform.

The knight can move to a square that is two squares horizontally and one square 
vertically, or two squares vertically and one square horizontally away from it. 
The complete move therefore looks like the letter L. Check out the image below 
to see all valid moves for a knight piece that is placed on one of the central squares.



Example

For cell = "a1", the output should be
chessKnight(cell) = 2.



For cell = "c2", the output should be
chessKnight(cell) = 6.



Input/Output

[execution time limit] 4 seconds (py3)

[input] string cell

String consisting of 2 letters - coordinates of the knight on an 8 × 8 
chessboard in chess notation.

Guaranteed constraints:
cell.length = 2,
'a' ≤ cell[0] ≤ 'h',
1 ≤ cell[1] ≤ 8.

[output] integer
"""

import numpy as np

def chessKnight(cell):
    #convert cell to numeric (x,y) coordinate
    letters='abcdefgh'
    cell_to_num={letters[idx]:idx+1 for idx in range(len(letters))}
    cell=np.array([cell_to_num[cell[0]],int(cell[1])])
    
    #knights potential moves will update the cell with cell[0]+=2 and cell[1]-=1 for 8 possible  moves
    potential_moves=[
            [2,1],[2,-1],
            [-2,1],[-2,-1],
            [1,2],[1,-2],
            [-1,2],[-1,-2]
            ]
    
    #record whether the knight will be on or off the board after each potential move
    end_cells=[cell+move for move in potential_moves]
    valid_end_cells=sum([True for position in end_cells if position[0]<=8 and position[0]>0 and position[1]<=8 and position[1]>0])
    return(valid_end_cells)

if __name__=='__main__':
    print(chessKnight('a2'))
    