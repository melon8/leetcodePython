# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    ## init 到 next 的过程，就是用stack对BST中序遍历的过程
    def __init__(self, root: TreeNode):
        self.stack = []
        self.pushAllLeft(root)
        
    def next(self) -> int:
        """
        @return the next smallest number
        """
        node = self.stack.pop()
        self.pushAllLeft(node.right)
        return node.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        # print('====start====')
        # for node in self.stack:
        #     print(node.val)
        # print('====end====')
        return len(self.stack) > 0
    
    def pushAllLeft(self, node):
        """
        @return whether we have a next smallest number
        """
        while node:
            self.stack.append(node)
            node = node.left
        
    
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()