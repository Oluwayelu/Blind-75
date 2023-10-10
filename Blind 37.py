# -*- coding: utf-8 -*-
"""
@author: Oluwayelu Ifeoluwa

Leetcode 435: Non-overlapping Intervals
"""

def eraseOverlapIntervals(intervals):
    intervals.sort()
    
    res = 0
    prevEnd = intervals[0][1]
    
    for start, end in intervals[1:]:
        if start >= prevEnd:
            prevEnd = end
        else:
            res += 1
            prevEnd = min(end, prevEnd)
    return res


print(eraseOverlapIntervals([[1,2], [2,3], [3,4], [1,3]]))