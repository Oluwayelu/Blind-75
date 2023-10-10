# -*- coding: utf-8 -*-
"""
@author: Oluwayelu Ifeoluwa

Leetcode 141: Linked List Cycle
"""
from data_structures.LinkedList import ListNode

def isCycles(head):
    """
    Time: O(n)
    Space: O(n)
        Hash Set solution
    """
    visited = set()
    curr = head
    
    while curr:
        if curr in visited:
            return True
        visited.add(curr)
        curr = curr.next
        
    return False

def isCycle(head):
    """
    Time: O(n)
    Space: O(1)
        Two Pointers (Floyd's Tortoise and Hare') Algorithm
    """
    slow, fast = head, head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
        
    return False

# Test data
head = ListNode(3)
n = ListNode(2)
head.next = n
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)

# make a cycle
# head.next.next.next.next = n

print(isCycle(head))