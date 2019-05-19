from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return 'None'
        s = [root]
        res = ''
        while s:
            node = s.pop()
            res += str(node.val) + ','
            if node.right:
                s.append(node.right)
            if node.left:
                s.append(node.left)
        return res[:-1]
     
    # BST前序遍历，第一个是root，后面连续比root value小的是左子树的value，剩下的是有子树的value
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == 'None':
            return None
        q = deque(data.split(','))
        return self.buildTree(q)
    
    # q : deque of preOrder, return treeNode
    def buildTree(self, q):
        
        # def printQ(q):
        #     ans = []
        #     for val in q:
        #         ans.append(val)
        #     print(ans)
        # printQ(q)
        if len(q) == 0:
            return None
        root = TreeNode(int(q.popleft()))
        leftQue = deque()
        while len(q)>0 and int(q[0]) < root.val:
            leftQue.append(q.popleft())
        root.left = self.buildTree(leftQue)
        root.right = self.buildTree(q)
        return root
                        
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))