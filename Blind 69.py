# -*- coding: utf-8 -*-
"""
@author: Oluwayelu Ifeoluwa

Leetcode 230: Kth Smallest Element in a BST
"""

from data_structures.BinaryTree import TreeNode

def kthSmallest(root, k):
    n, stack = 0, []
    curr = root
    
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
            
        curr = stack.pop()
        n += 1
        if n == k:
            return curr.val
        
        curr = curr.right
    
def inorder(root):
    if not root:
        return []
    
    return inorder(root.left) + [root.val] + inorder(root.right)

root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
print(kthSmallest(root, 1))