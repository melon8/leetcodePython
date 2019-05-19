from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    #通用版本，所有二叉树都适用 python2
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def dfs(node):
            if node is None:
                self.ans.append('None')
            else:
                self.ans.append(str(node.val))
                dfs(node.left)
                dfs(node.right)
        
        self.ans = []
        dfs(root)
        return ' '.join(self.ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def ddfs():
            # self.printQ(self.q)
            val = self.q.popleft()
            if val == 'None':
                return None
            node = TreeNode(int(val))
            node.left = ddfs()
            node.right = ddfs()
            return node
            
        self.q = deque(data.split())
        return ddfs()
    
    def printQ(self, q):
            ans = []
            for val in q:
                ans.append(val)
            print(ans) 

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))