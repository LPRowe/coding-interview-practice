# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 19:12:26 2020

@author: Logan Rowe

Construct a square matrix with a size N × N containing integers from 1 to 
N * N in a spiral order, starting from top-left and in clockwise direction.

Example

For n = 3, the output should be

spiralNumbers(n) = [[1, 2, 3],
                    [8, 9, 4],
                    [7, 6, 5]]
Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

Matrix size, a positive integer.

Guaranteed constraints:
3 ≤ n ≤ 100.

[output] array.array.integer
"""

import numpy as np
import matplotlib.pyplot as plt


def spiralNumbers(n):
    global running_count
    
    #numbers to fill array with
    values=[i for i in range(1,n**2+1)]
    
    #net count
    running_count=0
    
    #empty array to fill
    arr=np.full((n,n),0)
    
    #Define the direction in which to fill the array as {direction}_fill starting at row, column
    
    #RIGHT FILL
    def r_fill(arr,row,column,n):
        global running_count 
        
        while column<n:
            if arr[row,column]!=0:
                break
            arr[row,column]=values[running_count]
            running_count+=1
            column+=1
        return(arr,row+1,column-1)
    
    #LEFT FILL
    def l_fill(arr,row,column,n):
        global running_count
        
        while column>=0:
            if arr[row,column]!=0:
                break
            arr[row,column]=values[running_count]
            running_count+=1
            column-=1
        return(arr,row-1,column+1)
    
    #DOWN FILL
    def d_fill(arr,row,column,n):
        global running_count 
        
        while row<n:
            if arr[row,column]!=0:
                break
            arr[row,column]=values[running_count]
            running_count+=1
            row+=1
        return(arr,row-1,column-1)
    
    #UP FILL
    def u_fill(arr,row,column,n):
        global running_count 
        
        while row>=0:
            if arr[row,column]!=0:
                break
            arr[row,column]=values[running_count]
            running_count+=1
            row-=1
        return(arr,row+1,column+1)
    
    
    #always start with a right direction fill
    arr,r,c=r_fill(arr,0,0,n)
    
    #continue to fill in a spiral pattern until there are no zeroes
    while np.min(arr)==0:
        arr,r,c=d_fill(arr,r,c,n)
        arr,r,c=l_fill(arr,r,c,n)
        arr,r,c=u_fill(arr,r,c,n)
        arr,r,c=r_fill(arr,r,c,n)

            
    return(arr)
    
    

if __name__=='__main__':
    arr=spiralNumbers(10)
    print(arr)
    plt.imshow(arr)