# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        
        def isLeaf(node:TreeNode) -> bool:
            return node.left is None and node.right is None
        
        def recursiveLeft(node:TreeNode):
            if node is None:
                return
            if isLeaf(node):
                return
            self.result.append(node.val)
            if node.left:
                recursiveLeft(node.left)
            else:
                recursiveLeft(node.right)
        
        def recursiveRight(node:TreeNode):
            if node is None:
                return
            if isLeaf(node):
                return
            if node.right:
                recursiveRight(node.right)
            else:
                recursiveRight(node.left)
            # print("right val=", node.val)
            self.result.append(node.val)
        
        def recursiveLeaf(node:TreeNode):
            if node is None:
                return
            if isLeaf(node):
                # print("leaf val=", node.val)
                self.result.append(node.val)
            recursiveLeaf(node.left)
            recursiveLeaf(node.right)
            
        if root is None:
            return []
        self.result = [root.val]
        
        if root.left:
            recursiveLeft(root.left)
        
        if root.left or root.right:
            recursiveLeaf(root)
        
        if root.right:
            recursiveRight(root.right)
        return self.result