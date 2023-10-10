# -*- coding: utf-8 -*-
"""
@author: Oluwayelu Ifeoluwa

Lintcode 919: Meetings Rooms II
"""


def minMeetingRooms(intervals):
    start = sorted([interval[0] for interval in intervals])
    end = sorted([interval[1] for interval in intervals])

    res, count = 0, 0
    s, e = 0, 0

    while s < len(intervals):
        if start[s] < end[e]:
            s += 1
            count += 1
        else:
            e += 1
            count -= 1

        res = max(res, count)
    return res


print(minMeetingRooms([[0, 30], [5, 10], [15, 20]]))
