# -*- coding: utf-8 -*-
"""
@author: Oluwayelu Ifeoluwa

Leetcode 206: Reverse Linked List
"""

from data_structures.LinkedList import LinkedList

def reverseList_twoptrs(head):
    """
    Time: O(n)
    Space: O(1)
    """
    prev, temp = None, head

    while temp:
        nxt = temp.next
        temp.next = prev
        prev = temp
        temp = nxt
    return prev


def reverseList_recur(head):
    """
    Time: O(n)
    Space: O(n)
    """
    if not head:
        return None

    newHead = head
    if head.next:
        newHead = reverseList_recur(head.next)
        head.next.next = head
    head.next = None

    return newHead


l1 = LinkedList()
l1.append(1)
l1.append(2)
l1.append(3)
l1.append(4)

print(l1)
print(LinkedList(reverseList_twoptrs(l1.head)))

l1 = LinkedList()
l1.append(1)
l1.append(2)
l1.append(3)
l1.append(4)

print(l1)
print(LinkedList(reverseList_recur(l1.head)))
