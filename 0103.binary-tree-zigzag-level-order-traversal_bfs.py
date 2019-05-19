from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 逐层遍历广度优先搜索（每层都是从左到右）
# 记住每层的size，每层之前新建一个tempArr = [size]
# 偶数层倒着写入tempArr，技术层正着写入temp数组

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        level = 1
        res = []
        while len(q):
            size = len(q)
            temp = [0] * size
            for i in range(size):
                node = q.popleft()
                # print("node=", node.val)
                idx = i
                if level % 2 == 0:
                    idx = size - i - 1
                temp[idx] = node.val
                if node.left:q.append(node.left)
                if node.right:q.append(node.right)
                # print("q=", q)
            res.append(temp)
            level += 1
        return res