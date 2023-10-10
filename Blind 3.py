# -*- coding: utf-8 -*-
"""
@author: Oluwayelu Ifeoluwa

Leetcode 217: Contains Duplicate
"""
def duplicate(nums):
	"""
	Time: O(nlogn)
	Space: O(1)
	"""
	nums.sort()
	l, r = 0, 1
	
	while r < len(nums):
		if nums[l] == nums[r]:
			return True
		l += 1
		r += 1
	return False

def duplicates(nums):
	"""
	Time: O(n)
	Space: O(n)
	"""
	hashSet = set()
	
	for n in nums:
		if n in hashSet:
			return True
		hashSet.add(n)
	return False

print(duplicate([1,2,3,1]))