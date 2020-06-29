# class Solution(object):
#     def lengthOfLIS(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if not nums: return 0
#         # dp[i] 表示以nums[i]为结尾的最长上升子序列的长度
#         dp = [1] * len(nums)
#         for i in range(len(nums)):
#             for j in range(i):
#                 if nums[j] < nums[i]:
#                     dp[i] = max(dp[i], dp[j] + 1)
#         return max(dp)

# 可以打印子序列的版本
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0

        n = len(nums)
        # dp[i] 表示以nums[i]为结尾的最长上升子序列的长度
        dp = [1] * n

        pi = [-1] * n  # 决策数组，记录前一次选的哪一个
        pEnd = 0  # 结束标志
        res = 0

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

                    if dp[j] + 1 == dp[i]:  # 产生更新
                        pi[i] = j  # 决策数组记录, 从j转移过来

            res = max(res, dp[i])  # res记录最大值

            if dp[i] == res:  # 如果是当前最大，记录一下结束标志pEnd
                pEnd = i

        seq = [-1] * res  # 打印序列数组

        for i in range(res-1, -1, -1):  # 反向找前一个状态
            seq[i] = nums[pEnd]
            pEnd = pi[pEnd]  # 更新为前一个

        print(pi)
        print(seq)

        return res

nums = [10, 9, 2, 5, 3, 7, 101, 18]  # 4， [2, 3, 7, 18]
nums2 = [4, 2, 4, 5, 3, 7]  # 4， [2, 4, 5, 7]
s = Solution()
print(s.lengthOfLIS(nums))
print(s.lengthOfLIS(nums2))