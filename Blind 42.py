# -*- coding: utf-8 -*-
"""
@author: Oluwayelu Ifeoluwa

Leetcode 21: Merge Two Sorted Lists
"""
from data_structures.LinkedList import LinkedList, ListNode

def mergeLists(l1, l2):
    dummy = ListNode()
    tail = dummy
    
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next        
        tail = tail.next
    
    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2
        
    return dummy.next
            

l1 = LinkedList()
l1.append(1)
l1.append(2)
l1.append(4)

l2 = LinkedList()
l2.append(1)
l2.append(3)
l2.append(4)

print(LinkedList(mergeLists(l1.head, l2.head)))

