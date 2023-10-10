# -*- coding: utf-8 -*-
"""
@author: Oluwayelu Ifeoluwa

Leetcode 98: Validate Binary Search Tree
"""

from data_structures.BinaryTree import TreeNode

def isValidBST(root):
    
    def valid(node, left, right):
        if not node:
            return True
        if not (node.val > left and node.val < right):
            return False
        
        return (valid(node.left, left, node.val) and valid(node.right, node.val, right))
    return valid(root, float("-inf"), float("inf"))
        

root = TreeNode(2, TreeNode(1), TreeNode(3))
print(isValidBST(root))