# class Solution(object):
#     def maxProfit(self, prices):
#         # dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
#         # dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
#         n = len(prices)
#         dp_i_0 = 0
#         dp_i_1 = float("-inf")
#         for i in range(n):
#             temp = dp_i_0
#             dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
#             dp_i_1 = max(dp_i_1, temp - prices[i])
#         return dp_i_0

class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        if n == 0:
            return 0
        res = 0
        for i in range(1, n):
            if prices[i] - prices[i-1] > 0:
                res += prices[i] - prices[i-1]
        return res

# 直观做法：贪心
prices = [7,1,5,3,6,4]
s = Solution()
print(s.maxProfit(prices))

