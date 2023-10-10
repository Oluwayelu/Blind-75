# -*- coding: utf-8 -*-
"""
@author: Oluwayelu Ifeoluwa

Leetcode 102: Binary Tree Level Order Traversal
"""
from collections import deque
from data_structures.BinaryTree import TreeNode


def levelTraversl(root):
    res = []
    q = deque([root])

    while q:
        level = []

        for _ in range(len(q)):
            node = q.popleft()

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            level.append(node.val)
        res.append(level)
    return res


root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(levelTraversl(root))
