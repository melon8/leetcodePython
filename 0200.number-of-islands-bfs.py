from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 把1当作图的节点，1和1相连。问题转换成求无向图的连通分量。
        # 无向图搜索，可以用bfs来求
        if grid == None or len(grid) == 0:
            return 0
        nr = len(grid)
        nc = len(grid[0])
        islandsCount = 0
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == '1':
                    grid[i][j] = '0' #mark
                    islandsCount += 1
                    queue = deque([i * nc + j])
                    while len(queue) > 0:
                        idx = queue.popleft()
                        r = idx // nc
                        c = idx % nc
                        if r - 1 >= 0 and grid[r - 1][c] == '1':
                            grid[r - 1][c] = '0'#mark
                            queue.append((r - 1) * nc + c)
                        if c - 1 >= 0 and grid[r][c-1] == '1':
                            grid[r][c-1] = '0'#mark
                            queue.append(r * nc + c - 1)
                        if r + 1 < nr and grid[r + 1][c] == '1':
                            grid[r + 1][c] = '0'#mark
                            queue.append((r + 1) * nc + c)
                        if c + 1 < nc and grid[r][c + 1] == '1':
                            grid[r][c + 1] = '0'#mark
                            queue.append(r * nc + c+1)              
        return islandsCount
                        
        