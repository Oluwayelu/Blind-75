# -*- coding: utf-8 -*-
"""
@author: Oluwayelu Ifeoluwa

Leetcode 76: Minimum Window Substring
"""

def minimumWindow(s, t):
    """
    Time: O(n)
        where n is the length of s
    """
    if t == "": return ""
    
    countT, window = {}, {}
    
    for c in t:
        countT[c] = 1 + countT.get(c, 0)
    
    l = 0
    have, need = 0, len(countT)
    res, resLen = [-1, -1], float("infinity")
    for r in range(len(s)):
        c = s[r]
        window[c] = 1 + window.get(c, 0)
        
        if c in countT and window[c] == countT[c]:
            have += 1
            
        while have == need:
            # Update our result`
            if (r - l + 1) < resLen:
                res = [l, r]
                resLen = (r - l + 1)
            
            # Pop from the left of our window
            window[s[l]] -= 1
            if s[l] in countT and window[s[l]] < countT[s[l]]:
                have -= 1
            l += 1
            
    l, r = res
    return s[l:r + 1] if resLen != float("infinity") else ""
        

print(minimumWindow("ADOBECODEBANC", "ABC"))