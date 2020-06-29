class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        INF = float('inf')
        dp = [INF] * (n+1)
        dp[0] = 0
        for i in range(1, n+1):
            # Java : for (int j = 1; i - j * j >= 0; j++)
            j = 1
            while j * j <= i:
                # if dp[i - j*j] != INF:  # 可以不判断，因为任何数都可以由n个1组成，此时dp[i - j*j] != INF 肯定成立
                dp[i] = min(dp[i], dp[i - j*j] + 1)  # dp[i-j**2]
                j += 1
        return dp[n]

n = 13  # 2, 4 + 9
s = Solution()
print(s.numSquares(n))