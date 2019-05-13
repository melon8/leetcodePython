class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 把1当作图的节点，1和1相连。问题转换成求无向图的连通分量。
        # 无向图搜索，可以用dfs来求
        def dfs(i, j):
            rn = len(grid)
            cn = len(grid[0])
            if i < 0 or i >=  rn or j < 0 or j >= cn or grid[i][j] == '0':
                return
            grid[i][j] = '0' #marked
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        if grid == None or len(grid) == 0:
            return 0
        rn = len(grid)

        cn = len(grid[0])
        islandsCount = 0
        for i in range(rn):
            for j in range(cn):
                if grid[i][j] == '1':
                    islandsCount += 1
                    dfs(i, j)
        return islandsCount
                        
        