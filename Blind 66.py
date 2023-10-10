# -*- coding: utf-8 -*-
"""
@author: Oluwayelu Ifeoluwa

Leetcode 578: Subtree of Another Tree
"""


from data_structures.BinaryTree import TreeNode


def isSubTree(root, subRoot):
    if not subRoot:
        return True
    if not root:
        return False

    if sameTree(root, subRoot):
        return True

    return isSubTree(root.left, subRoot) or isSubTree(root.right, subRoot)


def sameTree(root, subRoot):
    if not root and not subRoot:
        return True
    if root and subRoot and root.val != subRoot.val:
        return (sameTree(root.left, subRoot.left) and sameTree(root.right, subRoot.right))

    return False


root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
subRoot = TreeNode(4, TreeNode(1), TreeNode(2))
print(isSubTree(root, subRoot))
