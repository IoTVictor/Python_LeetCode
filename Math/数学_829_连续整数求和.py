class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        # 给定一个正整数 N ，试求有多少组连续正整数满足所有数字之和为 N
        # N 是 sum
        # 起点 i 和 区间长度 k
        # 等差数列求和 i + (i+1) + (i+2) ... + (i+k-1) = k(2i+k-1)//2 = i*k + k(k-1)//2
        # 令 N = i*k + k(k-1)//2
        # 则 i = N - k(k-1)//2
        res = 0
        # 枚举区间长度k， 求起始点i
        for k in range(1, N + 1):
            if k * (k + 1) > 2 * N:
                break
            if (N - k * (k - 1) // 2) % k == 0:  # %k?
                res += 1
        return res
