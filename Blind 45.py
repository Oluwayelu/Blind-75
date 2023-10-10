# -*- coding: utf-8 -*-
"""
@author: Oluwayelu Ifeoluwa

Leetcode 143: Reorder List
"""
from data_structures.LinkedList import LinkedList


def reorder(head):
    slow, fast = head, head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    second = slow.next
    prev = slow.next = None
 
    while second:
        tmp = second.next
        second.next = prev
        prev = second
        second = tmp

    # merge two halfs
    first, second = head, prev
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2

    return head


l1 = LinkedList()
l1.append(1)
l1.append(2)
l1.append(3)
l1.append(4)

print(LinkedList(reorder(l1.head)))
