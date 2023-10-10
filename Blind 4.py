# -*- coding: utf-8 -*-
"""
@author: Oluwayelu Ifeoluwa

Leetcode 238: Product of Array except Self
"""

def product(nums):
	res = []

	prefix = 1
	for i in range(len(nums)):
		res.append(prefix)
		prefix *= nums[i]
	
	postfix = 1
	for i in range(len(nums) - 1, -1, -1):
		res[i] *= postfix
		postfix *= nums[i]
		
	return res
	
print(product([1,2,3,4]))