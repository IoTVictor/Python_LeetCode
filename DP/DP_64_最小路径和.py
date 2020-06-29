import copy
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 不开辟新空间，直接在grid修改，好处不用用临时变量
        m = len(grid)
        n = len(grid[0])
        grid1 = copy.deepcopy(grid)  # 深拷贝
        #grid1 = grid[:]  # 这种写法也不行
        print(grid1)
        # 决策数组pi
        # pi[i][j]=0 标记从上过来
        # pi[i][j]=1 标记从左过来
        pi = [[0]*n for _ in range(m)]
        # 第一行
        for i in range(1, n):
            grid[0][i] += grid[0][i-1]
            pi[0][i] = 1  # 决策pi只能是从左过来的
        # 第一列
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
            pi[i][0] = 0  # 决策pi只能是从上过来的
        # table
        for i in range(1, m):
            for j in range(1, n):
                t = min(grid[i-1][j], grid[i][j-1])  # 当前值 + min(从上过来的最优值，从左过来的最优值)
                # 标记pi
                if t == grid[i-1][j]:
                    pi[i][j] = 0  # 从上边来
                else:
                    pi[i][j] = 1  # 从左边来

                grid[i][j] += t

        path = [0] * (m+n-1)  # 路径数组（逆序存）
        # 从右下角开始
        x = m-1
        y = n-1
        for p in range(m+n-1):
            path[p] = grid1[x][y]  # 从深拷贝的原数组中取“路径值”
            if pi[x][y] == 0:
                x -= 1  # 向上移动
            elif pi[x][y] == 1:
                y -= 1  # 向左移动

        # 逆序打印
        for i in range(m+n-2, -1, -1):
            print(path[i])
        print('原始grid：', grid1)
        print('dp：', grid)
        print('决策数组：', pi)
        print('路径path[::-1]：', path[::-1])

        return grid[-1][-1]

# grid = [[1,3,1],
#         [1,5,1],
#         [4,2,1]]  # 路径 1→3→1→1→1 的总和，7

grid = [[1,5,7,6,8],
        [4,7,4,4,9],
        [10,3,2,3,2]]  # 路径 1→4→7→3→2→3→2 的总和，22
s = Solution()
print(s.minPathSum(grid))

