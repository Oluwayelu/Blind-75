# -*- coding: utf-8 -*-
"""
@author: Oluwayelu Ifeoluwa

Leetcode 323: Number of Connected Components in a Undirected Graph
"""
def countComponents_graph(n, edges):
    if not n:
        return 0
    
    adj = {i: set() for i in range(n)}
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
        
    res = 0
    visit = set()
    def dfs(curr):
        if curr in visit:
            return
        
        visit.add(curr)
        for nei in adj[curr]:
            dfs(nei)
            
        return 1
    
    for i in range(n):
        if i in visit:
            continue
        res += dfs(i)
        
    return res

# Union Find Approach
def countComponents(n, edges):
    par = [i for i in range(n)]
    rank = [1] * n
    
    def find(n1):
        res = n1
        
        while res != par[res]:
            par[res] = par[par[res]]
            res = par[res]
        return res
    
    def union(n1, n2):
        p1, p2 = find(n1), find(n2)
        
        if p1 == p2:
            return 0
        
        if rank[p2] > rank[1]:
            par[p1] = p2
            rank[p2] += rank[p1]
        else:
            par[p2] = p1
            rank[p1] += rank[p2]
        return 1
            
    res = n
    for n1, n2 in edges:
        res -= union(n1, n2)
    return res

print(countComponents_graph(6, [[0,1], [2,3], [4,5]]))
print(countComponents_graph(5, [[0,3], [3,2], [1,4]]))
# print(countComponents(5, [[0,1], [1,2], [3,4]]))