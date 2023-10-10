# -*- coding: utf-8 -*-
"""
@author: Oluwayelu Ifeoluwa

Leetcode 200: Number of Island
"""
import collections

def numIslands(grid):
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    visit = set()
    islands = 0
    
    def bfs(r, c):
        q = collections.deque()
        visit.add((r, c))
        q.append((r, c))
        
        while q:
            # make use of q.pop() for dfs
            print(q)
            row, col = q.pop()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                r, c = row + dr, col + dc
                
                if (r in range(rows) and c in range(cols) and grid[r][c] == 1 and (r, c) not in visit):
                    q.append((r, c))
                    visit.add((r, c))
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r, c) not in visit:
                bfs(r, c)
                islands += 1
                
    return islands

print(numIslands([[1,1,1,0,0], [1,1,0,0,0], [1,1,0,0,0], [0,0,0,1,1]]))