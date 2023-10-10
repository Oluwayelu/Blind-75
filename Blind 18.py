# -*- coding: utf-8 -*-
"""
@author: Oluwayelu Ifeoluwa

Leetcode 300: Longest Increasing Subsequence
"""

def lengthOfLIS(nums):
    res = 0
    
    for i in range(len(nums) - 1):
        curr = 1
        prev = nums[i]
        for j in range(i + 1, len(nums)):
            if prev < nums[j]:
                prev = nums[j]
                curr += 1
        res = max(res, curr)
        
    return res

def lengthOfLIS_DP(nums):
    LIS = [1] * len(nums)
    
    for i in range(len(nums) - 1, -1, -1):
        for j in range(i + 1, len(nums)):
            if nums[i] < nums[j]:
                LIS[i] = max(LIS[i], 1 + LIS[j])
    return max(LIS)

print(lengthOfLIS([1,2,4,3]))