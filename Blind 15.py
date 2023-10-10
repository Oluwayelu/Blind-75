# -*- coding: utf-8 -*-
"""
@author: Oluwayelu Ifeoluwa

Leetcode 190: Reverse Bits
"""


def reverseBits(n):
    res = 0

    for i in range(32):
        bit = (n >> i) & 1
        res = res | (bit << (31 - i))
    return res


print(reverseBits(43261596))
