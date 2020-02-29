# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 22:40:25 2020

@author: Logan Rowe
"""

def sum_each_path(start,val,count,s,sum=[]):
    if s in sum:
        return s

    if not start:
        return 0

    val+=start.value
    
    if not start.left and not start.right:
        sum.append(val)
        if val==s:
            count+=1
        if count>0:
            val=s
        print(sum)
        return val
    
    if s in sum:
        return s

    return sum_each_path(start.left,val,count,s,sum=[])+sum_each_path(start.right,val,count,s,sum=[])
    
def hasPathWithGivenSum(t, s):
    return sum_each_path(t,0,0,s)==s