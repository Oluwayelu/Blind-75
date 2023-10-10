# -*- coding: utf-8 -*-
"""
@author: Oluwayelu Ifeoluwa

Leetcode 48: Rotate Image
"""

def rotate(matrix): 
    l, r = 0, len(matrix[0]) - 1
    
    while l < r:
        
        for i in range(r - l):
            top, bottom = l, r
            
            # save top-left value
            topLeft = matrix[top + i][l]
            
            # move bottom-left to top-left
            matrix[top + i][l] = matrix[bottom][l + i]
            
            # move bottom-right to bottom-left
            matrix[bottom][l + i] = matrix[bottom - i][r]
            
            # move top-right to bottom-right
            matrix[bottom - i][r] = matrix[top][r - i]
            
            # move saved top-left to top-right
            matrix[top][r - i] = topLeft
        l += 1
        r -= 1
        
    return matrix

print(rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(rotate([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))