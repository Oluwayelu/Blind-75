# -*- coding: utf-8 -*-
"""
@author: Oluwayelu Ifeoluwa

Lintcode 920: Meetings Rooms
"""


def canAttendMeetings(intervals):
    intervals.sort()

    for i in range(1, len(intervals)):
        if intervals[i - 1][1] > intervals[i][0]:
            return False
    return True


print(canAttendMeetings([[0, 30], [5, 10], [15, 20]]))
print(canAttendMeetings([[10, 30], [0, 10], [30, 40]]))
