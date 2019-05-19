# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 先序遍历，深度优先搜索。
# 当result的lenghth<level时新插入一个array；
# 否则，取出level所在的array， 偶数排append到最后，奇数排insert到最前面
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        def helper(node, depth, res):
            if node:
                if len(res) < depth:
                    res.append([])
                if depth % 2:
                    res[depth-1].append(node.val)
                else:
                    res[depth-1].insert(0,node.val)
                helper(node.left, depth+1, res)
                helper(node.right, depth+1, res)
                
        helper(root, 1, res)
        return res
 
        