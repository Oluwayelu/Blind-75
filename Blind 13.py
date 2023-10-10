# -*- coding: utf-8 -*-
"""
@author: Oluwayelu Ifeoluwa

Leetcode 338: Counting Bits
"""


def countBits(n):
    """
    Time: O(nlogn)
    space: O(1)
    """
    res = []
    for i in range(n + 1):
        rem, count = i, 0
        while rem > 0:
            if rem % 2:
                count += 1
            rem = rem // 2
        res.append(count)
    return res


def countBits_DP(n):
    """
    Time: O(n)
    space: O(1)
    """
    dp = [0] * (n + 1)
    offset = 1

    for i in range(1, n + 1):
        if offset * 2 == i:
            offset = i
        dp[i] = 1 + dp[i - offset]
    return dp


print(countBits_DP(5))
