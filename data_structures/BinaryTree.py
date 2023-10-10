# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 21:01:43 2022

@author: USER
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def __repr__(self):
        return "({},{},{})".format(self.left, self.val,  self.right)
