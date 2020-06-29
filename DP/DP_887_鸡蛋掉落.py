class Solution(object):
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        memo = dict()  # key为(K,N),value为尝试次数

        def dp(K, N):  # K个鸡蛋、N层楼
            if K == 1:  # 当鸡蛋数 K 为 1 时，显然只能线性扫描所有楼层
                return N
            if N == 0:  # 当楼层数 N 等于 0 时，显然不需要扔鸡蛋
                return 0
            if (K, N) in memo:  # memo避免重复计算
                return memo[(K, N)]
            # 法一： 穷举所有可能，时间复杂度是 O(K*N*N)
            # res = float('INF')
            # for i in range(1, N+1):
            #     res = min(res,
            #             max(
            #                 dp(K - 1, i - 1), # 碎
            #                 dp(K, N - i)  # 没碎
            #                 ) + 1  # 在i楼扔了一次
            #             )

            # 法二优化：用二分搜索代替线性搜索，时间复杂度降为 O(K*N*logN)
            res = float('INF')
            low, high = 1, N
            while low <= high:
                mid = (low + high) // 2
                broken = dp(K - 1, mid - 1)  # 碎
                not_broken = dp(K, N - mid)  # 没碎
                # res = min(max(碎，没碎) + 1)
                if broken > not_broken:
                    high = mid - 1  # 碎了，去低层找
                    res = min(res, broken + 1)
                else:
                    low = mid + 1  # 没碎，从高层找
                    res = min(res, not_broken + 1)

            memo[(K, N)] = res
            return res

        return dp(K, N)

