# -*- coding: utf-8 -*-
"""
@author: Oluwayelu Ifeoluwa

Leetcode 54: Spiral Matrix
"""


def spiralOrder(matrix):
    res = []
    left, right = 0, len(matrix[0])
    top, bottom = 0, len(matrix)

    while left < right and top < bottom:

        # from top-left to top-right
        for i in range(left, right):
            res.append(matrix[top][i])
        top += 1

        # from top-right to bottom-right
        for i in range(top, bottom):
            res.append(matrix[i][right - 1])
        right -= 1

        # from bottom-right to bottom-left
        for i in range(right - 1, left - 1, -1):
            res.append(matrix[bottom - 1][i])
        bottom -= 1

        # from bottom-left to top-left
        for i in range(bottom - 1, top - 1, -1):
            res.append(matrix[i][left])
        left += 1

    return res


print(spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
