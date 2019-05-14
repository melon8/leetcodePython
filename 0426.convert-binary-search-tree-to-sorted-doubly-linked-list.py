"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def helper(node):
            nonlocal last, first
            if not node:
                return
            
            #left
            helper(node.left)
            
            #current
            if last:
                node.left = last
                last.right = node
            else:
                first = node
            last = node
            
            #right
            helper(node.right)
        
        if not root:
            return None
        
        first, last = None, None
        
        helper(root)
        
        first.left = last
        last.right = first
        
        return first