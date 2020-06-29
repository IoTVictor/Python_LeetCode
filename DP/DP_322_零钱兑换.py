class Solution(object):
    def coinChange(self, coins, amount):
        # 不同面额的硬币 coins 和一个总金额 amount
        MAX = float('inf')
        dp = [MAX for i in range(amount+1)]
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:  # 依次取不同的币值
                # 写法1
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], dp[i-coin]+1)
                # 写法2
                # if i >= coin and dp[i-coin] != MAX:
                #     dp[i] = min(dp[i], dp[i-coin]+1)

        if dp[amount] == MAX:  # max时表示无法用硬币拼出amount
            return -1
        return dp[amount]

amount = 11
coins = [1, 2, 5]
s = Solution()
print(s.coinChange(coins, amount))