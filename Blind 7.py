# -*- coding: utf-8 -*-
"""
@author: Oluwayelu Ifeoluwa

Leetcode 153: Find minimum in rotated Sorted Array
"""


def findMin(nums):
    res = nums[0]
    l, r = 0, len(nums) - 1

    while l < r:
        if nums[l] < nums[r]:
            res = min(res, nums[l])
            break

        mid = l + (r - l) // 2
        res = min(res, nums[mid])

        if nums[mid] >= nums[r]:
            l = mid + 1
        else:
            r = mid - 1

    return res


print(findMin([3, 4, 5, 1, 2]))
