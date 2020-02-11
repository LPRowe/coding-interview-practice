# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 01:40:57 2020

@author: Logan Rowe

Last night you partied a little too hard. Now there's a black and white photo 
of you that's about to go viral! You can't let this ruin your reputation, 
so you want to apply the box blur algorithm to the photo to hide its content.

The pixels in the input image are represented as integers. The algorithm 
distorts the input image in the following way: Every pixel x in the output 
image has a value equal to the average value of the pixel values from the 
3 × 3 square that has its center at x, including x itself. All the pixels 
on the border of x are then removed.

Return the blurred image as an integer, with the fractions rounded down.

Example

For

image = [[1, 1, 1], 
         [1, 7, 1], 
         [1, 1, 1]]
the output should be boxBlur(image) = [[1]].

To get the value of the middle pixel in the input 3 × 3 square: 
    (1 + 1 + 1 + 1 + 7 + 1 + 1 + 1 + 1) = 15 / 9 = 1.66666 = 1. 
    The border pixels are cropped from the final result.

For

image = [[7, 4, 0, 1], 
         [5, 6, 2, 2], 
         [6, 10, 7, 8], 
         [1, 4, 2, 0]]
the output should be

boxBlur(image) = [[5, 4], 
                  [4, 4]]
There are four 3 × 3 squares in the input image, so there should be four 
integers in the blurred output. To get the first value: 
    (7 + 4 + 0 + 5 + 6 + 2 + 6 + 10 + 7) = 47 / 9 = 5.2222 = 5. T
    he other three integers are obtained the same way, then the surrounding 
    integers are cropped from the final result.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.array.integer image

An image, stored as a rectangular matrix of non-negative integers.

Guaranteed constraints:
3 ≤ image.length ≤ 100,
3 ≤ image[0].length ≤ 100,
0 ≤ image[i][j] ≤ 255.

[output] array.array.integer

A blurred image represented as integers, obtained through the process in the description.
"""

'''


'''

import numpy as np

def boxBlur(image):
    image=np.array(image)
    
    #new image slightly smaller (removed border)
    new_image=np.full((image.shape[0]-2,image.shape[1]-2),0)
    
    #iterate over pixels in new image and fill pixel will blurred value from old image
    row=0
    while row < new_image.shape[0]:
        column=0
        while column < new_image.shape[1]:
        
            #calculate the blurred pixel value from the old image
            blurred_pixel=np.mean(image[row:row+3,column:column+3])

            #insert blurred pixel into new_image
            new_image[row,column]=int(blurred_pixel)
            column+=1
        row+=1
        
    return(new_image)

if __name__=='__main__':
    image = np.array([[7, 4, 0, 1], 
                      [5, 6, 2, 2], 
                      [6, 10, 7, 8], 
                      [1, 4, 2, 0]])
    
    print(boxBlur(image))
    
    print()
    
    print(np.array([[5,4],[4,4]]))