# -*- coding: utf-8 -*-
"""
@author: Oluwayelu Ifeoluwa

Leetcode 226: Invert Binary Tree
"""

from data_structures.BinaryTree import TreeNode


def invertTree(root):
    if not root:
        return None

    root.left, root.right = root.right, root.left
    
    invertTree(root.left)
    invertTree(root.right)

    return root


root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(1)),
                TreeNode(7, TreeNode(6), TreeNode(9)))
print(root)
print(invertTree(root))
