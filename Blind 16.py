# -*- coding: utf-8 -*-
"""
@author: Oluwayelu Ifeoluwa

Leetcode 70: Climbing Stairs
"""

def climbingStairs(n):
    step1, step2 = 1, 1
    
    for i in range(n-1):
        step1, step2 = step1 + step2, step1
    return step1

print(climbingStairs(5))

