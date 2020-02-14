# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 13:52:37 2020

@author: Logan Rowe
"""

class treeNode:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class binaryTree:
    def __init__(self,root):
        self.root=treeNode(root)
        
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
        Root --> Left --> Right
        
        Preorder print will traverse from the start (likely the root)
        down the left branch until it reaches a leaf, then it will travel back
        up the branch until it sees a right branch it can follow down
        each time it reaches a node with left and right branch it will prioritize
        left and will eventually check the right branches on the way up, once it reaches
        the root again, it will repeat the process on the right branch
        
                1
               / \
              2   3
             / \ / \
            4  5 6  7
           /
          8
         
        preorder_print(self.root,'') --> '1-2-4-8-5-3-6-7-'
        '''
        
        if start:
            traversal+=str(start.value)+'-'
            traversal=self.preorder_print(start.left,traversal)
            traversal=self.preorder_print(start.right,traversal)
        return traversal
    
    def inorder_print(self,start,traversal):
        '''
        Left most first then increment right
        
                
                1
               / \
              2   3
             / \ / \
            4  5 6  7
           /
          8
         
        preorder_print(self.root,'') --> '8-4-2-5-1-6-3-7-'
        '''
        
        if start:
            traversal=self.inorder_print(start.left,traversal)
            traversal+=str(start.value)+'-'
            traversal=self.inorder_print(start.right,traversal)
        return traversal
    
    def postorder_print(self,start,traversal):
        '''
        Left --> Right --> Root

        
                1
               / \
              2   3
             / \ / \
            4  5 6  7
           /
          8
         
        preorder_print(self.root,'') --> '8-4-2-5-6-3-7-1-'
        '''
        
        if start:
            traversal=self.postorder_print(start.left,traversal)
            traversal=self.postorder_print(start.right,traversal)
            traversal+=str(start.value)+'-' #because root is at end of list
        return traversal

if __name__=='__main__':
    tree=binaryTree(6)
    tree.root.left=treeNode(5)
    tree.root.right=treeNode(7)
    tree.root.left.left=treeNode(4)
    tree.root.left.right=treeNode(5.5)
    tree.root.left.left.left=treeNode(3)
    tree.root.right.left=treeNode(6.5)
    tree.root.right.right=treeNode(8)
    
    print(tree.print_tree(tree.root,traversal_type='preorder'))
    print(tree.print_tree(tree.root,traversal_type='inorder'))
    print(tree.print_tree(tree.root,traversal_type='postorder'))