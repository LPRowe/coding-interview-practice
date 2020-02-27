# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 23:55:09 2020

@author: Logan Rowe

When a candle finishes burning it leaves a leftover. makeNew leftovers can be combined to make a new candle, which, when burning down, will in turn leave another leftover.

You have candlesNumber candles in your possession. What's the total number of candles you can burn, assuming that you create new candles as soon as you have enough leftovers?

Example

For candlesNumber = 5 and makeNew = 2, the output should be
candles(candlesNumber, makeNew) = 9.

Here is what you can do to burn 9 candles:

burn 5 candles, obtain 5 leftovers;
create 2 more candles, using 4 leftovers (1 leftover remains);
burn 2 candles, end up with 3 leftovers;
create another candle using 2 leftovers (1 leftover remains);
burn the created candle, which gives another leftover (2 leftovers in total);
create a candle from the remaining leftovers;
burn the last candle.
Thus, you can burn 5 + 2 + 1 + 1 = 9 candles, which is the answer.

Input/Output

[execution time limit] 4 seconds (py3)

[input] integer candlesNumber

The number of candles you have in your possession.

Guaranteed constraints:
1 ≤ candlesNumber ≤ 15.

[input] integer makeNew

The number of leftovers that you can use up to create a new candle.

Guaranteed constraints:
2 ≤ makeNew ≤ 5.

[output] integer
"""

def candles(candlesNumber,makeNew):
    candles=[1]*candlesNumber
    count=0
    for candle in candles:
        count+=1
        if count%makeNew==0:
            candles.append(1)
    return(sum(candles))
    
    
    
    
    
    
    
    
print(candles(5,2))
print('True Value: 9')

print(candles(11,3))
print('True Value: 16')

print(candles(13,5))
print('True Value: 16')

print(candles(12,2))
print('True Value: 23')