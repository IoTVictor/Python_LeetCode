class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        # dp[i] 表示以nums[i]为结尾的最长上升子序列的长度
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

nums = [10, 9, 2, 5, 3, 7, 101, 18]
s = Solution()
print(s.lengthOfLIS(nums))