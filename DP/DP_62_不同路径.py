class Solution(object):
    def uniquePaths(self, m, n):
        dp = [[1]*n for _ in range(m)]  # m * n
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:  # 第一行和第一列只有1种走法
                    dp[i][j] = 1
                    continue  

                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

m = 7
n = 3
s = Solution()
print(s.uniquePaths(m, n))