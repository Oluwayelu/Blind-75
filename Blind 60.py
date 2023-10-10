# -*- coding: utf-8 -*-
"""
@author: Oluwayelu Ifeoluwa

Leetcode 104: Maximum depth of a binary tree
"""
from collections import deque
from data_structures.BinaryTree import TreeNode

# DFS Recursive Solution


def maxDepth(root):
    if not root:
        return 0

    return 1 + max(maxDepth(root.left), maxDepth(root.right))

# BFS Iterative Solution


def maxDepth_bfs(root):
    if not root:
        return 0

    q = deque([root])
    depth = 0

    while q:
        for _ in range(len(q)):
            node = q.popleft()

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        depth += 1

    return depth

# DFS Iterative Solution


def maxDepth_dfs(root):
    stack = [[root, 1]]
    res = 0

    while stack:
        node, depth = stack.pop()

        if node:
            res = max(res, depth)
            stack.append([node.left, depth + 1])
            stack.append([node.right, depth + 1])
    return res


root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(maxDepth_dfs(root))
