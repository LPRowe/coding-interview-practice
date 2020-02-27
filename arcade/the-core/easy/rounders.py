# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 23:42:50 2020

@author: Logan Rowe

We want to turn the given integer into a number that has only one non-zero digit using a tail rounding approach. This means that at each step we take the last non 0 digit of the number and round it to 0 or to 10. If it's less than 5 we round it to 0 if it's larger than or equal to 5 we round it to 10 (rounding to 10 means increasing the next significant digit by 1). The process stops immediately once there is only one non-zero digit left.

Example

For n = 15, the output should be
rounders(n) = 20;

For n = 1234, the output should be
rounders(n) = 1000.

1234 -> 1230 -> 1200 -> 1000.

For n = 1445, the output should be
rounders(n) = 2000.

1445 -> 1450 -> 1500 -> 2000.

Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

A positive integer.

Guaranteed constraints:
1 ≤ value ≤ 108.

[output] integer

The rounded number.
"""

def rounders(n):
    count=-1
    n=[str(i) for i in str(n)]
    while len(n)>n.count('0')+1:
        if int(n[count])>=5:
            n[count]='0'
            n[count-1]=str(int(n[count-1])+1)
        else:
            n[count]='0'
        count-=1
    return(int(''.join(n)))

print(rounders(1445))
    
    
    
    
    
    
    
    
    
