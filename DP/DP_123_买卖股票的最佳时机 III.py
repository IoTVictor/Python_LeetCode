'''
最多可以完成 两笔 交易。
注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
'''
'''
for (int k = max_k; k >= 1; k--) {
    if (i - 1 == -1) { /*处理 base case */ }
    dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i]);  // max(选择 rest, 选择 sell)
    dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i]); // max(选择 rest, 选择 buy)
}

dp[i][2][0] = max(dp[i-1][2][0], dp[i-1][2][1] + prices[i])
dp[i][2][1] = max(dp[i-1][2][1], dp[i-1][1][0] - prices[i])
dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][1][1] + prices[i])
dp[i][1][1] = max(dp[i-1][1][1], -prices[i])
'''

class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        # 下标含义：第i天、k交易次数、持有状态（0没有，1持有）
        dp_i10 = 0
        dp_i11 = float("-inf")
        dp_i20 = 0
        dp_i21 = float("-inf")
        for i in range(n):
            # 直接穷举k=2和k=1
            '''
            dp[i][2][0] = max(dp[i-1][2][0], dp[i-1][2][1] + prices[i])
            dp[i][2][1] = max(dp[i-1][2][1], dp[i-1][1][0] - prices[i])
            dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][1][1] + prices[i])
            dp[i][1][1] = max(dp[i-1][1][1], -prices[i])
            '''
            dp_i20 = max(dp_i20, dp_i21 + prices[i])  # 上一状态就没有 or 卖了股票现在没有了
            dp_i21 = max(dp_i21, dp_i10 - prices[i])  # 上一状态就有 or 买了股票
            dp_i10 = max(dp_i10, dp_i11 + prices[i])  # 上一状态就没有 or 卖了股票现在没有了
            dp_i11 = max(dp_i11, -prices[i])  # 上一状态就有 or 买了股票

        return dp_i20

prices = [3,3,5,0,0,3,1,4]  # 6
# 在第 4 天（股票价格 = 0）买入，在第 6 天（股票价格 = 3）卖出，利润 = 3-0 = 3 。
# 随后在第 7 天（股票价格 = 1）买入，在第 8 天 （股票价格 = 4）卖出，利润 = 4-1 = 3 。
s = Solution()
print(s.maxProfit(prices))