# -*- coding: utf-8 -*-
"""
@author: Oluwayelu Ifeoluwa

Leetcode 105: Construct Binary Tree from Preorder and Inorder Traversal
"""

from data_structures.BinaryTree import TreeNode


def contructTree(preorder, inorder):

    if not preorder or not inorder:
        return None

    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])
    root.left = contructTree(preorder[1:mid + 1], inorder[:mid])
    root.right = contructTree(preorder[mid + 1:], inorder[mid + 1:])
    print(root)
    return root


print(contructTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]))
