# -*- coding: utf-8 -*-
"""
@author: Oluwayelu Ifeoluwa

Leetcode 424: Longest Repeating Character Replacement
"""

def characterReplacement(s, k):
    count = {}
    longest = 0
    
    l = 0
    # For optimization
    maxf = 0
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        maxf = max(maxf, count[s[r]])
        
        # max(count.values()) instead of maxf
        while (r - l + 1) - maxf > k:
            count[s[l]] -= 1
            l += 1
            
        longest = max(longest, (r - l + 1))
    return longest

print(characterReplacement("ABAB", 2))
print(characterReplacement("AABABBA", 2))