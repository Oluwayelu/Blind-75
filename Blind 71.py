# -*- coding: utf-8 -*-
"""
@author: Oluwayelu Ifeoluwa

Leetcode 208: Implement Trie (Prefix Tree)
"""

class TrieNode:
    def __init__(self):
        self.children = {} 
        self.endOfWord = False
        
    def __repr__(self):
        return "{}".format(self.children)
        
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def __repr__(self):
        return "{}".format(self.root.children)
        
    def insert(self, word):
        cur = self.root
        
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True
        
    def search(self, word):
        cur = self.root
        
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord
    
    def startsWith(self, prefix):
        cur = self.root
        
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
    