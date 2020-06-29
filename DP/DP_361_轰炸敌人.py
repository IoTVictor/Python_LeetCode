class Solution:
    def maxKilledEnemies(self, grid):
        # init
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        row, col = len(grid), len(grid[0])
        # init
        up = [[0] * col for _ in range(row)]
        down = [[0] * col for _ in range(row)]
        left = [[0] * col for _ in range(row)]
        right = [[0] * col for _ in range(row)]
        # up：从上到下
        for i in range(row):
            for j in range(col):
                if grid[i][j] != 'W':
                    if grid[i][j] == 'E':
                        up[i][j] = 1
                    if i > 0:
                        up[i][j] += up[i - 1][j]
        # down：从下到上
        for i in range(row - 1, -1, -1):
            for j in range(col):
                if grid[i][j] != 'W':
                    if grid[i][j] == 'E':
                        down[i][j] = 1
                    if i + 1 < row:
                        down[i][j] += down[i + 1][j]
        # right：从右到左
        for i in range(row):
            for j in range(col - 1, -1, -1):
                if grid[i][j] != 'W':
                    if grid[i][j] == 'E':
                        right[i][j] = 1
                    if j + 1 < col:
                        right[i][j] += right[i][j + 1]

        # left：从左到右
        for i in range(row):
            for j in range(col):
                if grid[i][j] != 'W':
                    if grid[i][j] == 'E':
                        left[i][j] = 1
                    if j > 0:
                        left[i][j] += left[i][j - 1]

        # sum
        res = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '0':  # 找空地
                    res = max(res, up[i][j] + down[i][j] + left[i][j] + right[i][j])

        return res

grid = [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]  # 在位置 (1,1) 放置炸弹可以杀死 3 个敌人。
s = Solution()
print(s.maxKilledEnemies(grid))