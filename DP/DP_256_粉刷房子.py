class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        MAX = float('inf')
        n = len(costs)
        if n == 0:
            return 0

        dp = [[MAX]*3 for _ in range(n+1)]  # n+1 * 3 （从0-n，表示前n个房子的累计）
        # 初始条件
        dp[0][0], dp[0][1], dp[0][2] = 0, 0, 0  # 前0个房子，没有房子

        for i in range(1, n+1):  # 房子编号0-(n-1)，此处第i-1号房子，即当前的房子

            # 第i-1号房子的颜色j(当前房子)
            for j in range(3):

                # 第i-2号房子的颜色k（前一个房子）
                for k in range(3):
                    if j != k:  # 邻居不撞色
                        # 前一个房子染k色 + 当前房子染j色的cost（dp和cost下标不是对齐的）
                        dp[i][j] = min(dp[i][j], dp[i-1][k] + costs[i-1][j])  # 注意是costs[i-1][j]

        return min(dp[n][0], dp[n][1], dp[n][2])

costs = [[14,2,11],
         [11,4,5],
         [14,3,10]]  # 2+5+3=10
costs1 = [[17,2,17],
          [16,16,5],
          [14,3,19]]  # 2+5+3=10
s = Solution()
print(s.minCost(costs1))