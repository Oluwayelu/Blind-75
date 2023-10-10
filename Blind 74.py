# -*- coding: utf-8 -*-
"""
@author: Oluwayelu Ifeoluwa

Leetcode 212: Word Search II
"""

# import heapq


def topKFrequent(nums, k):
    count = {}
    bucket = [[] for i in range(len(nums) + 1)]

    for n in nums:
        count[n] = 1 + count.get(n, 0)

    for n, f in count.items():
        bucket[f].append(n)

    res = []
    for i in range(len(bucket) - 1, 0, -1):
        for n in bucket[i]:
            res.append(n)
            if len(res) == k:
                return res


print(topKFrequent([1, 1, 1, 2, 2, 3, 4], 2))
