# -*- coding: utf-8 -*-
"""
@author: Oluwayelu Ifeoluwa

Leetcode 128: Longest Consequtive Sequence
"""


def longestConsequtive(nums):
    numSet = set(nums)
    longest = 0

    for n in nums:
        if (n - 1) not in numSet:
            length = 0
            while (n + length) in numSet:
                length += 1
            longest = max(length, longest)

    return longest


print(longestConsequtive([100, 4, 200, 1, 3, 2]))
