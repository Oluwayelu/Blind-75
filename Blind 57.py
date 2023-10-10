# -*- coding: utf-8 -*-
"""
@author: Oluwayelu Ifeoluwa

Leetcode 5: Longest Palidromic Substring
"""


def longestPalindrome(s):
    res = ""
    resLen = 0

    for i in range(len(s)):
        # palindromes with odd length
        l = r = i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > resLen:
                res = s[l:r + 1]
                resLen = r - l + 1
            l -= 1
            r += 1

        # palindromes with even length
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > resLen:
                res = s[l:r + 1]
                resLen = r - l + 1
            l -= 1
            r += 1
    return res


print(longestPalindrome("babad"))
print(longestPalindrome("cbbd"))
