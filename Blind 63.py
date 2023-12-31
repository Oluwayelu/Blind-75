# -*- coding: utf-8 -*-
"""
@author: Oluwayelu Ifeoluwa

Leetcode 124: Binary Tree Maximum Path Sum
"""
from data_structures.BinaryTree import TreeNode


def maxPathSumm(root):
    res = [root.val]

    def dfs(root):
        if not root:
            return 0

        leftMax = dfs(root.left)
        rightMax = dfs(root.right)
        leftMax = max(leftMax, 0)
        rightMax = max(rightMax, 0)

        res[0] = max(res[0], root.val + leftMax + rightMax)
        return root.val + max(leftMax, rightMax)
    dfs(root)
    return res[0]


root = TreeNode(1, TreeNode(2), TreeNode(3))

print(maxPathSumm(root))
