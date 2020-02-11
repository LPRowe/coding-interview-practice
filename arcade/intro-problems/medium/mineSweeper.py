# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 18:02:16 2020

@author: Logan Rowe

In the popular Minesweeper game you have a board with some mines and those 
cells that don't contain a mine have a number in it that indicates the total 
number of mines in the neighboring cells. Starting off with some arrangement 
of mines we want to create a Minesweeper game setup.

Example

For

matrix = [[true, false, false],
          [false, true, false],
          [false, false, false]]
the output should be

minesweeper(matrix) = [[1, 2, 1],
                       [2, 1, 1],
                       [1, 1, 1]]
Check out the image below for better understanding:



Input/Output

[execution time limit] 4 seconds (py3)

[input] array.array.boolean matrix

A non-empty rectangular matrix consisting of boolean values - true if the 
corresponding cell contains a mine, false otherwise.

Guaranteed constraints:
2 ≤ matrix.length ≤ 100,
2 ≤ matrix[0].length ≤ 100.

[output] array.array.integer

Rectangular matrix of the same size as matrix each cell of which contains an 
integer equal to the number of mines in the neighboring cells. Two cells are 
called neighboring if they share at least one corner.
"""

'''
Thoughts:

1) Lets make a duplicate matrix with a border of 0 (False) values
2) Fill output_matrix with the sum of true values in the 8 closest squares
3) return output_matrix
'''

import numpy as np

def minesweeper(matrix):
    matrix=np.array(matrix)
    
    #input is true and false so lets make it python readable
    matrix[matrix=='true']=True
    matrix[matrix=='false']=False
    
    temp=np.full((matrix.shape[0]+2,matrix.shape[1]+2),False)
    
    #fill central squares in temp with given matrix
    temp[1:-1,1:-1]=matrix
    
    output_matrix=np.full(matrix.shape,0)
    
    row=0
    while row < output_matrix.shape[0]:
        column=0
        while column < output_matrix.shape[1]:
        
            #calculate the blurred pixel value from the old image
            mine_count=np.sum(temp[row:row+3,column:column+3])
            
            #If the square itself is a mine subtract 1 so it doesnt count itself
            if matrix[row,column]==True:
                mine_count-=1

            #insert blurred pixel into new_image
            output_matrix[row,column]=mine_count
            column+=1
        row+=1

    return(output_matrix)
    
if __name__=='__main__':
    matrix = [[True, False, False],
          [False, True, False],
          [False, False, False]]
    print(minesweeper(matrix))