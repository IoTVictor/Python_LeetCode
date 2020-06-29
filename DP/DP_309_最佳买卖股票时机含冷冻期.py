class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        dp = [[0, 0] for _ in range(n + 1)]
        prices.insert(0, 0)  # 下标1算第一天, 方便处理

        dp[1][1] = -prices[1]
        for i in range(2, n + 1):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])

        return dp[n][0]
