class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 点睛：与打家劫舍I的区别是屋子围成了一个环
        # 偷首不偷尾
        # 不偷首偷尾
        # 分别计算不包含首和不包含尾这两种情况来判断哪个大哪个小

        # 1.dp[i] 代表当前最大子序和
        # 2.动态方程: dp[i] = max(dp[i-1] and , nums[i-1]+dp[i-2])
        # 3.初始化: 给没有房子时，dp一个位置，即：dp[0]
        #   3.1 当size=0时，没有房子，dp[0]=0；
        #   3.2 当size=1时，有一间房子，偷即可：dp[1]=nums[0]

        nums1 = nums[1:]  # 除去句首的子串
        nums2 = nums[:-1] # 除去句尾的子串
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        def handle(n, nums):
            dp1 = 0
            dp2 = nums[0]
            for i in range(2, n+1):
                dp1 = max(dp2, nums[i-1] + dp1)
                dp1, dp2 = dp2, dp1
            return dp2

        res1 = handle(n-1, nums1)
        res2 = handle(n-1, nums2)

        return max(res1, res2)
nums = [1,2,3,1]
s = Solution()
print(s.rob(nums))
