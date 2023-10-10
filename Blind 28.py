# -*- coding: utf-8 -*-
"""
@author: Oluwayelu Ifeoluwa

Leetcode 207: Course Schedule
"""


def canFinish(numCourses, prerequisites):
    preMap = {i: [] for i in range(numCourses)}
    for crs, pre in prerequisites:
        preMap[crs].append(pre)

    visited = set()
    def dfs(crs):
        if crs in visited:
            return False
        if preMap[crs] == []:
            return True

        visited.add(crs)
        for pre in preMap[crs]:
            if not dfs(pre):
                return False

        visited.remove(crs)
        preMap[crs] = []
        return True

    for crs in range(numCourses):
        if not dfs(crs):
            return False

    return True


print(canFinish(5, [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]))
print(canFinish(4, [[0, 1], [2, 3]]))
 