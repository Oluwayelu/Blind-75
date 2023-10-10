# -*- coding: utf-8 -*-
"""
@author: Oluwayelu Ifeoluwa

Leetcode 125: Valid Palindrome
"""


def isPalindrome(s):
    newStr = ""

    for c in s:
        if (ord(c.lower()) in range(ord("0"), ord("9") + 1) or 
            ord(c.lower()) in range(ord("a"), ord("z") + 1)):
            newStr += c.lower()

    return True if newStr == newStr[::-1] else False

def isPalindromes(s):
    l, r = 0, len(s) - 1
    
    while l < r:
        while l < r and not alphaNum(s[l]):
            l += 1
        while r > l and not alphaNum(s[r]):
            r -= 1
        
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
        
    return True
    
def alphaNum(c):
    return (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))


print(isPalindromes("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
