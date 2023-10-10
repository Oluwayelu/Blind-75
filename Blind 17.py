# -*- coding: utf-8 -*-
"""
@author: Oluwayelu Ifeoluwa

Leetcode 322: Coin Change
"""

def coinChange(coins, amount):
    """
    Time: O(n * m)
        where n = amount and m = number of coins
    Space: O(n)
        where n = amount + 1
    """
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], 1 + dp[a - c])
    
    return dp[-1] if amount + 1 not in dp else -1

print(coinChange([1,2,5], 11))
