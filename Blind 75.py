# -*- coding: utf-8 -*-
"""
@author: Oluwayelu Ifeoluwa

Leetcode 295: Find Median from Data Stream
"""
# Insert in-order approach
# Min and Max Heap approach

import heapq

class MedianFinder:
    def __init__(self):
        self.small, self.large = [], []
    
    def addNum(self, num):
        heapq.heappush(self.small, -1 * num)
        
        # make sure every num in small <= every num in large
        if (self.small and self.large and (-1 * self.small[0]) > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
            
        # Uneven size
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)
    
    def findMedian(self):
        
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return ((-1 * self.small[0]) + self.large[0]) / 2
    


# Test

func = ["addNum", "addNum", "findMedian", "addNum", "findMedian"]
val = [1, 2, None, 3, None]

median = MedianFinder()
for i in range(len(func)):
    if func[i] == "addNum":
        median.addNum(val[i])
        
    elif func[i] == "findMedian":
        print(median.findMedian())
