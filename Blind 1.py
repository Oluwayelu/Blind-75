# -*- coding: utf-8 -*-
"""
@author: Oluwayelu Ifeoluwa

Leetcode 1: Two sum
"""

def twoSum(nums, target):
	hashmap = {}
	
	for i, v in enumerate(nums):
		if target - v in hashmap:
			return [hashmap[target - v], i]
		hashmap[v] = i

print(twoSum([2,1,5,3], 4))