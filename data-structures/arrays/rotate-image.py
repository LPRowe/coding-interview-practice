# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 00:17:31 2020

@author: Logan Rowe
"""

'''
Note: Try to solve this task in-place (with O(1) additional memory), 
since this is what you'll be asked to do during an interview.

You are given an n x n 2D matrix that represents an image. 
Rotate the image by 90 degrees (clockwise).

For

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
the output should be

rotateImage(a) =
    [[7, 4, 1],
     [8, 5, 2],
     [9, 6, 3]]
'''

'''
Thoughts:
    
we know it is a square matrix (n x n) so lets see if we can find a pattern
that uses the dimensions of the matrix to relate the start index to the 
rotated index

0,0 --> 0,2
0,1 --> 1,2
2,0 --> 0,0
1,1 --> 1,1
1,2 --> 2,1


rule is ( start_index[1] , (n-1)-start_index[0] )
    (a[column] , (n-1)-a[row])

net coding time: 15 minutes
'''

import numpy as np

def rotateImage(a):
    n=a.shape[0]
    b=np.full((n,n),0)
    r=0
    while r < n:
        c=0
        while c < n:
            b[c,(n-1)-r]=a[r,c]
            c+=1
        r+=1
    return(b)
    
    

    
    
if __name__ == '__main__':
    a=np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
    
    print(a)
    print()
    print(rotateImage(a))
    print('\nyay')