class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        #bfs 从右到左逐层遍历，每层第一个节点存入result
        if not root:
            return []
        result = []
        queue = deque([root])
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if i == 0: result.append(node.val)
                if node.right: queue.append(node.right)
                if node.left: queue.append(node.left)
        return result