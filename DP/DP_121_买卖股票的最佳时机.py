# class Solution(object):
#     def maxProfit(self, prices):
#
#         n = len(prices)
#         # base case: dp[-1][0] = 0, dp[-1][1] = -infinity
#         # dp[i][0] = max(dp[-1][0], dp[-1][1] + prices[i]) = max(0, -infinity + prices[i]) = 0
#         # dp[i][1] = max(dp[-1][1], dp[-1][0] - prices[i]) = max(-infinity, 0 - prices[i]) = -prices[i]
#         dp_i_0 = 0  # max_profit
#         dp_i_1 = float("-inf")  # min_price
#         for i in range(n):
#             # dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
#             dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
#             # dp[i][1] = max(dp[i-1][1], -prices[i])
#             dp_i_1 = max(dp_i_1, -prices[i])
#
#         return dp_i_0

# 直观解法
class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        if n == 0:
            return 0
        res = 0
        minV = prices[0]  # 记录最低价
        for i in range(1, n):
            res = max(res, prices[i] - minV)  # 差值
            minV = min(minV, prices[i])  # 记录之前的最低价
        return res

prices = [7,1,5,3,6,4]
s = Solution()
print(s.maxProfit(prices))
