# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 14:45:09 2020

@author: Logan Rowe

binary_search_tree:
    -each node has at most two children
    -the right child is always larger than the parent
    -the left shild is always less than the parent
    
    
bst property:
    -every note on the right subtree must be larger than the current node
    -and the vice-versa for left subtrees

"""

class treeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Binary_Search_Tree:
    
    def __init__(self,root=None):
        self.root=root
        self.val=0
        
    def insert(self,data):
        '''
        Inserts the data at the appropriate location per the rules of a
        binary search tree
        '''        
        if self.root==None:
            self.root=treeNode(data)
        else:
            #Use a helper method for insertion
            self._insert(data,self.root)
            
    def _insert(self,data,curr_node):
        '''
        Recursive helper method for insert
        '''
        if data < curr_node.data:
            if curr_node.left==None:
                curr_node.left=treeNode(data)
            else:
                curr_node=curr_node.left
                self._insert(data,curr_node)
        elif data > curr_node.data:
            if curr_node.right==None:
                curr_node.right=treeNode(data)
            else:
                curr_node=curr_node.right
                self._insert(data,curr_node)
        else:
            #No duplicates allowed!
            print('value is already present in the tree')

            
    def _find(self,data,curr_node):
        '''
        Recursive helper method for find
        '''
        
        if data>curr_node.data and curr_node.right:
            return(self._find(data,curr_node.right))
        
        if data<curr_node.data and curr_node.left:
            return(self._find(data,curr_node.left))
            
        if data==curr_node.data:
            return True
        
        #will return none if never found)
        
                
    def find(self,data):
        '''
        Returns True if value is in the tree
        Returns False if the value is not in the tree
        '''
        #make sure the tree is not empty
        if self.root:
            #check to see if the value is in the tree
            is_found = self._find(data,self.root)
            if is_found:
                return True
            return False
        else:
            #the tree is empty
            return None
        
    def print_tree(self,start,traversal_type='preorder'):
        if traversal_type=='preorder':
            return(self.preorder_print(start,''))
        elif traversal_type=='inorder':
            return(self.inorder_print(start,''))
        elif traversal_type=='postorder':
            return(self.postorder_print(start,''))
        else:
            print('traversal_type must be one of: "preorder", "inorder"')
            return False
    
    def preorder_print(self,start,traversal):
        '''
        Node --> Left --> Right
        '''
        if start:
            traversal+=str(start.data)+'-'
            traversal=self.preorder_print(start.left,traversal)
            traversal=self.preorder_print(start.right,traversal)
        return(traversal)
        
    def inorder_print(self,start,traversal):
        '''
        Left --> Node --> Right
        '''
        if start:
            traversal=self.inorder_print(start.left,traversal)
            traversal+=str(start.data)+'-'
            traversal=self.inorder_print(start.right,traversal)
        return(traversal)
            
    def postorder_print(self,start,traversal):
        '''
        Left --> Right
        '''
        if start:
            traversal=self.postorder_print(start.left,traversal)
            traversal=self.postorder_print(start.right,traversal)
            traversal+=str(start.data)+'-'
        return(traversal)
        
    def bst_property(self,start):
        '''
        Returns True if the tree meets the bst_property requirements
        Returns False if not
        '''
        
        #An in_order print will be in sorted order if bst_property exists
        in_order=str(self.inorder_print(start,''))
        in_order=[int(value) for value in in_order.split('-')[:-1]]
        if in_order == sorted(in_order):
            return True
        return False
    
    
    def inorder_print_tree(self):
        '''
        redundant other way to do an in order print
        '''
        if self.root:
            self._inorder_print_tree(self.root)
    
    def _inorder_print_tree(self,cur_node):
        '''
        helper function for the redundant inorder_print_tree
        '''
        if cur_node:
            self._inorder_print_tree(cur_node.left)
            print(str(cur_node.data))
            self._inorder_print_tree(cur_node.right)

    def sum_all_elements(self,start):
        if not start:
            return 0
        else:
            return start.data+self.sum_all_elements(start.left)+self.sum_all_elements(start.right)
    
    def sum_each_path(self,start,val,sums=[]):
        if not start:
            print('a')
            return 0
        
        val+=start.data
        
        if not start.left and not start.right:
            sums.append(val)
            print('b')
            return sums
        
        print('c')
        return self.sum_each_path(start.left,val,sums=sums)+self.sum_each_path(start.right,val,sums=sums)
            
            
        


if __name__=='__main__':
    '''
        4
       / \
      2   8
         / \
        5   10
    
    '''
    bst=Binary_Search_Tree()
    values=[4,2,8,5,10]
    for value in values:
        bst.insert(value)
    
    for t_type in ['preorder','inorder','postorder']:
        print(bst.print_tree(bst.root,traversal_type=t_type))
            
    print()
    print(bst.bst_property(bst.root))
    print()
    
    print(bst.inorder_print_tree())
    
    #print(bst.sum_of_each_path(bst.root))
    
    print()
    
    print(bst.sum_all_elements(bst.root))
    
    print()
    
    print(bst.sum_each_path(bst.root,0))