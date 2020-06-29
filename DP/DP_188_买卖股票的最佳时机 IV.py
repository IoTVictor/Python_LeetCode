class Solution(object):
    def maxProfit(self, k, prices):
        # k = any integer
        n = len(prices)

        if k > n/2:  # 相当于不限次数买，即k = +inf
            return self.maxProfit_k_inf(prices)

        dp = [[[0]*2 for _ in range(k+1)] for _ in range(n)]  # n * k+1 * 2
        for i in range(n):
            for j in range(k, 0, -1):  # 逆序
                if i - 1 == -1:  # badcase
                    dp[0][j][0] = 0
                    dp[0][j][1] = -prices[0]
                    continue
                # 昨天没有股票 or 昨天有股票今天卖出
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                # 昨天有股票 or 昨天没有股票今天买入(买入当作一次交易，是 j-1)
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])

        return dp[n - 1][k][0]

    # 不限k的次数,即题目2（k = +inf）
    def maxProfit_k_inf(self, prices):
        # k = +infinity，不需要记录 k 这个状态
        # dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        # dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        n = len(prices)
        dp_i_0 = 0
        dp_i_1 = float("-inf")
        for i in range(n):
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, temp - prices[i])
        return dp_i_0

s = Solution()
prices = [3, 2, 6, 5, 0, 3]
k = 2
print(s.maxProfit(k, prices))  # 7



