class Solution(object):
    # 674. 最长连续递增序列 Longest Continuous Increasing Subsequence
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                dp[i] = dp[i-1] + 1
        return max(dp)
nums = [1,3,5,4,7]
s = Solution()
print(s.findLengthOfLCIS(nums))
# 最长连续递增序列是 [1,3,5], 长度为3
# 尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为5和7在原数组里被4隔开。

# 相似题：300，最长上升子序列LIS，会返回4，[1,3,5,7]