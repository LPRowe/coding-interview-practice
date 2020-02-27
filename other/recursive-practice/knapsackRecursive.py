# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 14:39:25 2020

@author: Logan Rowe

Given a knapsack that can only hold 10 kg 

Decide which items to bring to maximize the value

items{item_number:[weight,value],...}
"""

import numpy as np

def packKnapsackNaive(item_number,knapsack_weight):
    if item_number==0 or knapsack_weight>=10:
        result=0
    elif items[item_number][0]>10-knapsack_weight:
        result=packKnapsack(item_number-1,knapsack_weight)
    else:
        temp1=packKnapsack(item_number-1,knapsack_weight)
        temp2=items[item_number][1]+packKnapsack(item_number-1,knapsack_weight+items[item_number][0])
        print(temp1)
        print(temp2)
        result=max(temp1,temp2)
    return result

empty=np.full((5,10),None)
def packKnapsack(item_number,knapsack_weight):
    global empty
    if empty[item_number][knapsack_weight]!=None:
        return empty[item_number][knapsack_weight]
    if item_number==0 or knapsack_weight>=10:
        result=0
    elif items[item_number][0]>10-knapsack_weight:
        result=packKnapsack(item_number-1,knapsack_weight)
    else:
        temp1=packKnapsack(item_number-1,knapsack_weight)
        temp2=items[item_number][1]+packKnapsack(item_number-1,knapsack_weight+items[item_number][0])
        print(temp1)
        print(temp2)
        result=max(temp1,temp2)
    empty[item_number][knapsack_weight]=result
    return result
        
        
        
if __name__=='__main__':
    
    items={
            0:[1,5],
            1:[2,3],
            2:[4,5],
            3:[2,3],
            4:[5,2]
            }
    
    print(packKnapsack(4,0))