# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 00:19:23 2020

@author: Logan Rowe

magine a white rectangular grid of n rows and m columns divided into two parts by a diagonal line running from the upper left to the lower right corner. Now let's paint the grid in two colors according to the following rules:

A cell is painted black if it has at least one point in common with the diagonal;
Otherwise, a cell is painted white.
Count the number of cells painted black.

Example

For n = 3 and m = 4, the output should be
countBlackCells(n, m) = 6.

There are 6 cells that have at least one common point with the diagonal and therefore are painted black.



For n = 3 and m = 3, the output should be
countBlackCells(n, m) = 7.

7 cells have at least one common point with the diagonal and are painted black.



Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

The number of rows.

Guaranteed constraints:
1 ≤ n ≤ 105.

[input] integer m

The number of columns.

Guaranteed constraints:
1 ≤ m ≤ 105.

[output] integer

The number of black cells.
"""

'''
This approach works... and i thought it was neatly done

However, for very large inputs the use of itertools product function
takes a long time to run, I will find a more efficient solution.  
'''

from itertools import product

def fcn(n,m,x):
    y=-(n/m)*x+n
    return(y)

def countBlackCells(n, m):
    if n==m:
        return 3*n-2

    #each box is noted by its lower left hand corners cartesian coordinate
    boxes=[i for i in product(range(m),range(n))]
    
    black_box_count=0
    
    #check each box to see if it overlaps with the line
    for box in boxes:
        x1,y1=box
        x2,y2=box[0]+1,box[1]+1
        
        if y1<=fcn(n,m,x1) and y2>=fcn(n,m,x2):
            black_box_count+=1
        
    return black_box_count


n_vals=[3,3,66666]
m_vals=[4,3,88888]
results=[6,7,177774]

for (n,m,r) in zip(n_vals,m_vals,results):
    print(countBlackCells(n,m))
    print(r)
    print()
        
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    