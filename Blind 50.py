# -*- coding: utf-8 -*-
"""
@author: Oluwayelu Ifeoluwa

Leetcode 3: Longest Substring Without Repeating Charcters
"""

def lengthOfLongestSubstring(s):
    """
    Time: O(n^2)
    Space: O(n)
    """
    subStr = ""
    longest = 0
    
    for i in range(len(s) - 1):
        for j in range(i, len(s)):
            
            if s[j] in subStr:
                longest = max(longest, len(subStr))
                subStr = ""
                subStr += s[j]
            else:
                subStr += s[j]
    return longest

def lengthOfLongestSubstring_s(s):
    """
    Time: O(n)
    Space: O(n)
    """
    subStr = set()
    longest = 0
    
    l = 0
    for r in range(len(s)):
        while s[r] in subStr:
            subStr.remove(s[l])
            l += 1
            
        subStr.add(s[r])
        longest = max(longest, r - l + 1)
        print(longest, subStr)
    return longest

            

print(lengthOfLongestSubstring_s("aabcdbcbb"))