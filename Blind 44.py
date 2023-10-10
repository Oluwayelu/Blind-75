# -*- coding: utf-8 -*-
"""
@author: Oluwayelu Ifeoluwa

Leetcode 19: Remove Nth Node From End of List
"""
from data_structures.LinkedList import LinkedList, ListNode


def removeNthFromEnd(head, n):
    if n == 0:
        return head

    dummy = ListNode(0, head)
    left = dummy

    right = head
    while right and n > 0:
        right = right.next
        n -= 1

    while right:
        left = left.next
        right = right.next

    left.next = left.next.next
    return dummy.next


l1 = LinkedList()
l1.append(1)
l1.append(2)
l1.append(3)
l1.append(4)
l1.append(5)

print(LinkedList(removeNthFromEnd(l1.head, 2)))
