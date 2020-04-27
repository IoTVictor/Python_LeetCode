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
        dp_i10 = 0
        dp_i11 = float("-inf")
        dp_i20 = 0
        dp_i21 = float("-inf")
        for i in range(n):
            dp_i20 = max(dp_i20, dp_i21 + prices[i])
            dp_i21 = max(dp_i21, dp_i10 - prices[i])
            dp_i10 = max(dp_i10, dp_i11 + prices[i])
            dp_i11 = max(dp_i11, -prices[i])

        return dp_i20
prices = [3,3,5,0,0,3,1,4]
s = Solution()
print(s.maxProfit(prices))