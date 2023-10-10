# -*- coding: utf-8 -*-
"""
@author: Oluwayelu Ifeoluwa

Leetcode 121: Best time to buy and Sell a Stock
"""

def maxProfit(prices):
	l, r = 0, 1
	max_profit = 0
	
	while r < len(prices):
		if prices[l] < prices[r]:
			profit = prices[r] - prices[l]
			max_profit = max(max_profit, profit)
			
		else:
			l = r
		r += 1
	return max_profit
	
print(maxProfit([9,7,5,8,0,11]))