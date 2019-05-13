# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        #dfs 中右左
        self.result = []
        def dfs(node: TreeNode, depth: int):
            if not node:
                return
            if depth == len(self.result):
                self.result.append(node.val)
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
            
        dfs(root, 0)
        
        return self.result