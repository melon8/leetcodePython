# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def getDepth(node):
            depth = 0
            while node:
                node = node.left
                depth += 1
            return depth
        if not root:
            return 0
        leftDepth = getDepth(root.left)
        rightDepth = getDepth(root.right)
        
        # print ( leftDepth, rightDepth)
        if leftDepth == rightDepth:
            #满二叉树 ps 减号优先级比 << 高
            return 1 + (1 << leftDepth) - 1 + self.countNodes(root.right)
        else:
            return 1 + self.countNodes(root.left) + (1 << rightDepth) - 1