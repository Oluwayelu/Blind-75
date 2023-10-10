# -*- coding: utf-8 -*-
"""
@author: Oluwayelu Ifeoluwa

Leetcode 55: Jump Game
"""

def jumpGames(nums):
    dp = [False] * len(nums)
    dp[-1] = True
    
    for i in range(len(nums) - 2, -1, -1):
        for j in range(1, nums[i] + 1):
            if dp[i]:
                continue
            dp[i] = dp[i+j]
            
    return dp[0]

def jumpGame(nums):
    goal = len(nums) - 1
    
    for i in range(len(nums) - 2, -1, -1):
        if i + nums[i] >= goal:
            goal = i
    return True if goal == 0 else False

print(jumpGame([2,3,1,8,4]))

print(jumpGame([3,2,1,0,4]))
