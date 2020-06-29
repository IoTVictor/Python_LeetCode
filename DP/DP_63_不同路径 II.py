class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # dp table (m * n)
        dp = obstacleGrid
        m = len(dp)
        if m == 0:
            return 0
        n = len(dp[0])
        if n == 0:
            return 0
        # 特殊情况：左上角堵死了，直接返回0
        if obstacleGrid[0][0] == 1:
            return 0
        for i in range(m):
            for j in range(n):
                # 有障碍
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0  # 路不通
                    continue
                # 无障碍
                # 左上角,如果左上角有障碍，会在上个if中continue出
                if i == 0 and j == 0:
                    dp[i][j] = 1
                    continue
                dp[i][j] = 0
                if i > 0:  # 有上面一行
                    dp[i][j] += dp[i-1][j]  # 从上面走过来的
                if j > 0:  # 有左边一列
                    dp[i][j] += dp[i][j-1]  # 从左边走过来的
        return dp[m-1][n-1]
grid1 = [[0]]
grid = [[0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0]]  # 4
s = Solution()
print(s.uniquePathsWithObstacles(grid))