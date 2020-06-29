# from bisect import bisect_left
# class Solution(object):
#     def maxEnvelopes(self, envelopes):
#         """
#         :type envelopes: List[List[int]]
#         :rtype: int
#         """
#         envelopes.sort(key=lambda x: (x[0], -x[1]))
#         nums = [i[1] for i in envelopes]
#         dp = []
#         for i in range(len(nums)):
#             idx = bisect_left(dp, nums[i])
#             if idx == len(dp):
#                 dp.append(nums[i])
#             else:
#                 dp[idx] = nums[i]
#         return len(dp)
# 法一：dp，O(n*n)超时
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        # case： [[5, 4], [6, 4], [6, 7], [2, 3]]

        n = len(envelopes)
        envelopes.sort(key=lambda x: (x[0], -x[1]))  # 宽度w升序排；当w相等时，高度h降序排, [[2, 3], [5, 4], [6, 7], [6, 4]]

        # 转换成求LIS
        nums = [i[1] for i in envelopes]  # nums是高度序列, [3, 4, 7, 4]
        dp = [1] * n
        res = 0
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
            res = max(res, dp[i])
        return res

envelopes = [[5,4],[6,4],[6,7],[2,3]]
s = Solution()
print(s.maxEnvelopes(envelopes))