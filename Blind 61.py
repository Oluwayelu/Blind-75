# -*- coding: utf-8 -*-
"""
@author: Oluwayelu Ifeoluwa

Leetcode 100: Same Tree
"""

from data_structures.BinaryTree import TreeNode


def sameTree(p, q):
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False

    return (sameTree(p.left, q.left) and
            sameTree(p.right, q.right))


p = TreeNode(1, TreeNode(2), TreeNode(3))
q = TreeNode(1, TreeNode(2), TreeNode(3))

print(sameTree(p, q))
