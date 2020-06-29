class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 1.dp[i] 代表当前最大子序和
        # 2.动态方程: dp[i] = max(dp[i-1], nums[i-1]+dp[i-2])，即max(最后一个房子不偷， 最后一个房子偷)
        # 3.初始化: 给没有房子时，dp一个位置，即：dp[0]
        #   3.1 当n=0时，没有房子，dp[0]=0；
        #   3.2 当n=1时，有一间房子，偷即可：dp[1]=nums[0]

        n = len(nums)
        if n == 0:
            return 0
        dp = [0] * (n+1)  # 开辟n+1空间，[0, n]
        dp[0] = 0  # 没有房子
        dp[1] = nums[0]  # 一栋房子
        for i in range(2, n+1):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i-1])

        return dp[n]
nums = [3, 1, 2, 4] # 7
s = Solution()
print(s.rob(nums))