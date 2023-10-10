# -*- coding: utf-8 -*-
"""
@author: Oluwayelu Ifeoluwa

Leetcode 178: Graph Valid Tree
"""

def validTree(n, edges):
    """
    Time: O(E + V)
    Space: O(E + V)
    """
    if not  n:
        return True
    
    adj = { i: set() for i in range(n)}
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
        
    visited = []
    def dfs(curr, prev = -1):
        if curr in visited:
            return False
    
        visited.append(curr)
        for nei in adj[curr]:
            print(visited, curr, prev)
            if nei == prev:
                continue
            if not dfs(nei, curr):
                return False
        return True
                
    return dfs(1) and n == len(visited)
    
    
print(validTree(5, [[0,1], [0,2], [0,3], [1,4]]))