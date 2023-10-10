# -*- coding: utf-8 -*-
"""
@author: Oluwayelu Ifeoluwa

Leetcode 21: Merge K Sorted Lists
"""
from data_structures.LinkedList import LinkedList, ListNode

def mergeKLists(lists):
    if not lists or len(lists) == 0:
        return None
    
    while len(lists) > 1:
        mergedLists = []
        
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if (i + 1) < len(lists) else None
            mergedLists.append(LinkedList(mergeLists(l1.head, l2.head)))
        lists = mergedLists
        
    return lists[0]
            

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

#  Test cases

l1 = LinkedList()
l1.append(5)
l1.append(8)
l1.append(9)

l2 = LinkedList()
l2.append(3)
l2.append(5)
l2.append(7)

l3 = LinkedList()
l3.append(2)
l3.append(10)
l3.append(11)

l4 = LinkedList()
l4.append(1)
l4.append(4)
l4.append(6)

lists = [l1, l2, l4]
mergedLists = mergeKLists(lists)
print(mergedLists)