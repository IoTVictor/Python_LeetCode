# 动态规划 O(n^2)，超时
# class Solution(object):
#     def canJump(self, nums):
#         dp = [True] * len(nums)
#         dp[0] = True
#         for j in range(1, len(nums)):
#             dp[j] = False
#             # 从 i 跳到 j
#             for i in range(j):
#                 if dp[i] == True and i + nums[i] >= j:
#                     dp[j] = True
#                     break  # 任意一种情况满足即可
#
#         return dp[len(nums)-1]
class Solution(object):
    def canJump(self, nums):
        k = 0  # 能跳到最远的距离
        for i in range(len(nums)):
            if i > k:  # 表明最远也无法跳到第i位
                return False
            k = max(k, i + nums[i])  # 看最远能到哪
        return True

nums = [3,2,1,0,4]
s = Solution()
print(s.canJump(nums))