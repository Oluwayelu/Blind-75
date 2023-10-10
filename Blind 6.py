# -*- coding: utf-8 -*-
"""
@author: Oluwayelu Ifeoluwa

Leetcode 152: Maximum Product Subarray
"""

def maxProduct(nums):
	res = float("-inf")
	currMax, currMin = 1,1
	
	for n in nums:
		currMax, currMin = max(n * currMax, n * currMin, n), min(n * currMax, n * currMin, n)
		
		res = max(res, currMax)
	return res

print(maxProduct([2,3,-2,4]))