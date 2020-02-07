# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 12:41:53 2020

@author: Logan Rowe

Followed a tutorial to learn the basic functions such as append, length, display
and get

Then challenged myself to improve on the list structure by adding functions such
as fastAppend which is O(1) instead of O(n) and insert
"""

class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class linked_list:
    def __init__(self):
        self.head=node()
        self.tail=self.head
        
    def append(self,data):
        new_node = node(data)
        current_node=self.head
        while current_node.next!=None:
            current_node=current_node.next
        current_node.next=new_node
        self.tail=new_node
        
    def fastAppend(self,data):
        new_node=node(data)
        self.tail.next=new_node
        self.tail=new_node
        

    def length(self):
        idx=0
        current_node=self.head
        while current_node.next!=None:
            idx+=1
            current_node=current_node.next
        return(idx)
        
    def display(self):
        '''
        display the current contents of the list
        '''
        elems = []
        current_node=self.head
        while current_node.next!=None:
            current_node=current_node.next
            elems.append(current_node.data)
        return(elems)
    
    def get(self,index):
        '''
        return the data point at a given index
        '''
        L=self.length()
        if index>=L:
            print("Requested index is out of range.\nMax range is:",str(L))
            return(None)
            
        idx=0
        current_node=self.head
        while True:
            current_node=current_node.next
            if idx==index: 
                return(current_node.data)
            idx+=1
            
    def erase(self,index):
        '''
        remove the node at given index from list
        '''
        idx=0
        current_node=self.head
        while idx<index:
            current_node=current_node.next
            idx+=1
            
        #change connection to skip the node to be erased    
        current_node.next=current_node.next.next
        
    def insert(self,data,index):
        '''
        Insert a new node into the list at given index with given data value
        '''
        new_node=node(data)
        
        idx=0
        current_node=self.head
        while idx<index:
            current_node=current_node.next
            idx+=1
        
        new_node.next=current_node.next
        current_node.next=new_node
        

if __name__ == '__main__':
    
    #Test get and display functions
    my_list=linked_list()
    for i in [1,3,55,3,3,5,6,6,6,6,43,3,7]:
        my_list.append(i)
    
    print(my_list.display())
    print(my_list.get(2))
    
    
    #Test erase function
    my_list.erase(2)
    print(my_list.display())
    
    
    #Test insertion function
    my_list.insert(56,2)
    print(my_list.display())
    
    
    #Test fast append function (this should be O(1) instead of O(n))
    my_list.fastAppend(4)
    my_list.fastAppend(5)
    print(my_list.display())
    
    
        
