# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 20:01:52 2022

@author: USER
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __repr__(self):
        res = []
        res.append(str(self.val))
        
        return "".join(res)

class LinkedList:
    def __init__(self, head=None):
        
        self.head = head

    def __repr__(self):
        res = []
        curr = self.head
        while curr:
            res.append(str(curr.val))
            curr = curr.next

        return " -> ".join(res)
    
    def __len__(self):
        count = 0
        curr = self.head
        
        while curr:
            count += 1
            curr = curr.next
        
        return count

    def append(self, data):
        
        new_node = ListNode(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
            
        last_node.next = new_node
        
    def prepend(self, data):
        
        new_node = ListNode(data)
        
        new_node.next = self.head
        self.head = new_node