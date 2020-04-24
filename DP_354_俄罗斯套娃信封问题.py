from bisect import bisect_left
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        nums = [i[1] for i in envelopes]
        dp = []
        for i in range(len(nums)):
            idx = bisect_left(dp, nums[i])
            if idx == len(dp):
                dp.append(nums[i])
            else:
                dp[idx] = nums[i]
        return len(dp)

envelopes = [[5,4],[6,4],[6,7],[2,3]]
s = Solution()
print(s.maxEnvelopes(envelopes))