class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0
        n = len(costs)  # 房子数 n
        k = len(costs[0])  # 颜色数 k
        INF = float('inf')
        dp = [[INF for _ in range(k)] for _ in range(n+1)]

        # init
        for i in range(k):
            dp[0][i] = 0

        id1, id2 = 0, 0  # 最小值和次小值的下标
        for i in range(1, n+1):
            min1 = INF  # 花费最小值，记录之前的dp，同时用 id1 记录 j 时的颜色
            min2 = INF  # 花费次小值

            for j in range(k):  # 找到上一个状态[i-1]的花费最小数和次小数
                if dp[i-1][j] < min1:
                    min2 = min1  # 将最小值 传给次小值
                    id2 = id1
                    min1 = dp[i-1][j]
                    id1 = j
                else:
                    if dp[i-1][j] < min2:
                        min2 = dp[i-1][j]
                        id2 = j

            for j in range(k):
                dp[i][j] = costs[i-1][j]  # 当前房子的花费，注意对齐下标，dp是n+1维，costs是n维

                if j != id1:  # 与上个状态最后的房子 不撞色，选最小值min1
                    dp[i][j] += min1
                else:  # 与上个状态最后的房子 撞色，选次小值min2
                    dp[i][j] += min2

        # res = INF
        # for i in range(k):
        #     res = min(res, dp[n][i])

        res = min(dp[n][:])

        return res


costs = [[14,2,11],[11,14,5],[14,3,10]]  # 三个屋子分别使用第1,2,1种颜色,花费2+5+3，总花费是10
s = Solution()
print(s.minCostII(costs))

