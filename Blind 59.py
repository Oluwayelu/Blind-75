# -*- coding: utf-8 -*-
"""
@author: Oluwayelu Ifeoluwa

Lintcode 659: Encode and Decode
"""

def encode(strs):
    res = ""
    for s in strs:
        res += str(len(s)) + "#" + s
        
    return res

def decode(strs):
    res, i = [], 0
    
    while i < len(strs):
        j = i
        while strs[j] != "#":
            j += 1
        length = int(str(strs[i:j]))
        res.append(strs[j + 1 : j + length + 1])
        i = j + length + 1
        
    return res

strs = ["lint", "code", "love", "you"]
encodedStr = encode(strs)


print(strs == decode(encodedStr))