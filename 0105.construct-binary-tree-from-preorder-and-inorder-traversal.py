# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        ## inOrder 子串在原inOrder数组中开始和结束元素的下标 start index 和 end index
        def helper(in_start, in_end):
            nonlocal pre_start
            if in_end < in_start:
                return None
            val = preorder[pre_start]
            index = indexDict[val]
            node = TreeNode(val)
            ## 因为是按照先序遍历的顺序decode的，所以preOrder的root的index就可以用
            ## 全局的 pre_start，每次调用+1
            pre_start += 1
            # print ("val = ", val,"index=",index, "in_start =", in_start, "in_end=", in_end, 'pre_start', pre_start)
            node.left = helper(in_start, index - 1)
            node.right = helper(index + 1, in_end)
            return node

        indexDict = {}
        for i in range(len(inorder)):
            indexDict[inorder[i]] = i
        pre_start = 0
        # print(indexDict)
        return helper(0, len(inorder) - 1)