class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0] * n  # dp = [0 for i in range(n)]
        dp[0] = nums[0]
        max_sum = dp[0]

        for i in range(1, n):
            dp[i] = nums[i] + (dp[i-1] if dp[i-1]>0 else 0)  # java dp[i-1]>0 ? dp[i-1] : 0
            max_sum = max(max_sum, dp[i])
        print(dp)
        return max_sum

nums = [-2,1,-3,4,-1,2,1,-5,4]
s = Solution()
print(s.maxSubArray(nums))
