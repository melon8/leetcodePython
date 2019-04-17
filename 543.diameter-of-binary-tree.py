# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 1
        
        # 找到最长path上的节点数
        def recursivePathNodeCount(node: TreeNode) -> int:
            if not node:
                return 0
            left = recursivePathNodeCount(node.left)
            right = recursivePathNodeCount(node.right)

            #以当前节点作为拐角的path
            self.ans = max(self.ans, left + right + 1)

            #沿着当前左子树或者右子树path继续往上传递
            return max(left, right) + 1
        
        recursivePathNodeCount(root)
        
        # 返回的边长度 = node数-1
        return self.ans - 1