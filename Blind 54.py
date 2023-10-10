# -*- coding: utf-8 -*-
"""
@author: Oluwayelu Ifeoluwa

Leetcode 49: Group Anagrams
"""
from collections import defaultdict


def groupAnagrams_brute(strs):
    res = []

    for s in strs:
        ana = []
        for i in range(len(strs)):
            if sorted(s) == sorted(strs[i]):
                ana.append(strs[i])

        if ana not in res:
            res.append(ana)

    return res


def groupAnagrams(strs):
    count = defaultdict(list)

    for s in strs:
        alpha = [0] * 26

        for c in s:
            alpha[ord(c) - ord("a")] += 1

        count[tuple(alpha)].append(s)

    return count.values()


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
