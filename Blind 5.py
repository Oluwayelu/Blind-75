# -*- coding: utf-8 -*-
"""
@author: Oluwayelu Ifeoluwa

Leetcode 53: Maximum Subarray
"""

def maxSubarray(nums):
	maxSum = nums[0]
	currSum = 0
	
	for n in nums:
		if currSum < 0:
			currSum = 0
		currSum += n
		maxSum = max(maxSum, currSum)

	return maxSum

print(maxSubarray([-2,1,-3,4,-1,2,1,-5,4]))