# 求图中有多少个岛，可以用并查集来求，初始状态为所有的1分别是一个集合，parent=self。
# 遍历整个二维数组，每遇到相邻的1，则connect。最后返回并查集的count就是小岛数
class UnionFind:
        def __init__(self, grid):
            nr = len(grid)
            nc = len(grid[0])
            self.parent = [0] * (nr * nc)
            self.rank = [0] * (nr * nc)
            self.count = 0
            for r in range(nr):
                for c in range(nc):
                    if grid[r][c] == '1':
                        idx = r*nc + c
                        # print (r, c, nr, nc, idx)
                        self.parent[idx] = idx
                        # 使用rank压缩路径，rank代表包含该节点，以及该节点所有子数的结点数
                        self.rank[idx] = 1
                        self.count += 1
        
        # root parent of q
        def find(self, p):
            while p != self.parent[p]:
                p = self.parent[p]
            return p
        
        # if p and q are connected
        def connected(self, p, q):
            return self.find(p) == self.find(q)
        
        # connect p and q
        def union(self, p, q):
            i = self.find(p)
            j = self.find(q)
            if i == j:
                return
            if  self.rank[i] < self.rank[j]:
                self.parent[i] = j
                self.rank[j] += self.rank[i]
            else:
                self.parent[j] = i
                self.rank[i] += self.rank[j]
            self.count -= 1
            
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid == None or len(grid) == 0:
            return 0
        nr = len(grid)
        nc = len(grid[0])
        islandsCount = 0
        uf = UnionFind(grid)
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == '1':
                    grid[r][c] = '0' #mark
                    idx = r*nc + c
                    if r - 1 >= 0 and grid[r - 1][c] == '1':
                        uf.union(idx, (r - 1)*nc + c)
                    if c - 1 >= 0 and grid[r][c-1] == '1':
                        uf.union(idx, r * nc + c - 1)
                    if r + 1 < nr and grid[r + 1][c] == '1':
                        # print("aaa",r,c, (idx, (r + 1) * nc + c))
                        uf.union(idx, (r + 1) * nc + c)
                    if c + 1 < nc and grid[r][c + 1] == '1':
                        uf.union(idx, r * nc + c+1)
             
        return uf.count
                        
        