# -*- coding: utf-8 -*-
"""
@author: Oluwayelu Ifeoluwa

Leetcode 191: Number of 1 Bits
"""

def hammingWeight(n):
    res = 0
    while n:
        res += n % 2
        n = n >> 2
    return res

def hammingWeights(n):
    res = 0
    while n:
        n &= (n - 1)
        res += 1
    return res

