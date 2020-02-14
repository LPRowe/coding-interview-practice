# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 18:22:37 2020

@author: Logan Rowe

You are given an array of desired filenames in the order of their creation. 
Since two files cannot have equal names, the one which comes later will have 
an addition to its name in a form of (k), where k is the smallest positive 
integer such that the obtained name is not used yet.

Return an array of names that will be given to the files.

Example

For names = ["doc", "doc", "image", "doc(1)", "doc"], the output should be
fileNaming(names) = ["doc", "doc(1)", "image", "doc(1)(1)", "doc(2)"].

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.string names

Guaranteed constraints:
5 ≤ names.length ≤ 1000,
1 ≤ names[i].length ≤ 15.

[output] array.string
"""

def fileNaming(names):
    
    #Iterate through names and check to see if name is pre-existing (at an earlier index)
    index=0
    for name in names:
        count=0
        if name in names[:index]:
            #Since a name is preexisting, count how many times it pre-exists
            count+=names[:index].count(name)
            while names[index]+'('+str(count)+')' in names[:index]:
                count+=1
            
            #update the files name
            names[index]=names[index]+'('+str(count)+')'
        index+=1
        
    return(names)
    
    
if __name__=='__main__':
    names = ["doc", "doc", "image", "doc(1)", "doc"]
    output= ["doc", "doc(1)", "image", "doc(1)(1)", "doc(2)"]
    for (new_name,name_out) in zip(fileNaming(names),output):
        print(new_name,name_out)
        