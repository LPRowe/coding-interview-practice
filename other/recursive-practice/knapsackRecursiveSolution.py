# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 14:24:55 2020

@author: Logan Rowe

Given a knapsack that can only hold 5 kg 

Decide which items to bring to maximize the value

items{item_number:[weight,value],...}
"""


def pack_knapsack(items,knapsack_weight):
    global knap_sack_items
    
    item=items.pop()
    
    for item in items:
        if items[item][0]<=5-knapsack_weight:
            knapsack_items[item]=item
            items.pop(item)
            knapsack_weight+=items[item][0]
            pack_knapsack(items,knapsack_weight)
        elif item[item][0]




if __name__=='__main__':
    
    items={
            1:[1,5],
            2:[2,3],
            3:[4,5],
            4:[2,3],
            5:[5,2]
            }
    
    knapsack_items=[0]*len(items)
