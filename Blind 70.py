# -*- coding: utf-8 -*-
"""
@author: Oluwayelu Ifeoluwa

Leetcode 235: Lowest Common Ancestor of a Binary Search Tree
"""

from data_structures.BinaryTree import TreeNode

def lowestCommonAncestor(root, p, q):
    curr = root
    
    while curr:
        if p < root.val and q < root.val:
            curr = curr.left
        elif p > root.val and q > root.val:
            curr = curr.right
        else:
            return curr

def lowestCommonAncestor_recur(root, p, q):
    if p < root.val and q < root.val:
        lowestCommonAncestor_recur(root.left, p, q)
    elif p > root.val and q > root.val:
        lowestCommonAncestor_recur(root.right, p, q)
    else:
        return root.val
    

root = TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))), TreeNode(8, TreeNode(7), TreeNode(9)))
print(lowestCommonAncestor(root, 0, 4 ))