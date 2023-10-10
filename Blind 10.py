# -*- coding: utf-8 -*-
"""
@author: Oluwayelu Ifeoluwa

Leetcode 11: Container with most water
"""


def maxArea(height):
    max_area = 0
    l, r = 0, len(height) - 1

    while l < r:
        area = min(height[l], height[r]) * (r - l)
        max_area = max(max_area, area)

        if height[l] > height[r]:
            r -= 1
        else:
            l += 1
    return max_area


print(maxArea([1, 8, 6, 2, 5, 4, 8, 9, 7]))
