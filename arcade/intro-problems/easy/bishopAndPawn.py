# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 17:31:25 2020

@author: Logan Rowe

Given the positions of a white bishop and a black pawn on the standard chess 
board, determine whether the bishop can capture the pawn in one move.

The bishop has no restrictions in distance for each move, but is limited to 
diagonal movement. Check out the example below to see how it can move:


Example

For bishop = "a1" and pawn = "c3", the output should be
bishopAndPawn(bishop, pawn) = true.



For bishop = "h1" and pawn = "h3", the output should be
bishopAndPawn(bishop, pawn) = false.



Input/Output

[execution time limit] 4 seconds (py3)

[input] string bishop

Coordinates of the white bishop in the chess notation.

Guaranteed constraints:
bishop.length = 2,
'a' ≤ bishop[0] ≤ 'h',
1 ≤ bishop[1] ≤ 8.

[input] string pawn

Coordinates of the black pawn in the same notation.

Guaranteed constraints:
pawn.length = 2,
'a' ≤ pawn[0] ≤ 'h',
1 ≤ pawn[1] ≤ 8.

[output] boolean

true if the bishop can capture the pawn, false otherwise.
"""

def bishopAndPawn(bishop, pawn):
    '''
    Bishop Rules:
    bishop: g2 --> [7,2]
    bishop[0] and bishop[1] must change by the same ammount to be valid
    bishop[0] and bishop[1] must be in [1:8,1:8]
    '''

    location_dict={
        'a':1,
        'b':2,
        'c':3,
        'd':4,
        'e':5,
        'f':6,
        'g':7,
        'h':8
    }

    bishop=[location_dict[bishop[0]],int(bishop[1])]
    pawn=[location_dict[pawn[0]],int(pawn[1])]

    bishop_potential=[]
    for i in range(1,9):
        for j in range(1,9):
            if abs(i-bishop[0])==abs(j-bishop[1]):
                bishop_potential.append((i,j))

    if (pawn[0],pawn[1]) in bishop_potential:
        return True
    else:
        return False
