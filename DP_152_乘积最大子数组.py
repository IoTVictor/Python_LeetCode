class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None:
            return 0
        dp = [[0 for _ in range(2)] for _ in range(2)]  # 只需保存前一次的结果，所以只需要2*2数组
        # 保存最大值dp[][0]，负最大值（即最小值）dp[x][1]
        dp[0][1], dp[0][0], res = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            x, y = i % 2, (i-1) % 2  # 滚动数组，交替保存
            dp[x][0] = max(dp[y][0] * nums[i], dp[y][1] * nums[i], nums[i])  # 存最大值
            dp[x][1] = min(dp[y][0] * nums[i], dp[y][1] * nums[i], nums[i])  # 存最小值
            res = max(res, dp[x][0])
        return res
    # def maxProduct(self, nums):
    #     if nums is None:
    #         return 0
    #     res, curMax, curMin = nums[0], nums[0], nums[0]
    #     for i in range(1, len(nums)):
    #         num = nums[i]
    #         curMax, curMin = curMax * num, curMin * num
    #         curMax, curMin = max(curMax, curMin, num), min(curMax, curMin, num)
    #         res = max(curMax, res)
    #
    #     return res


nums = [2, 3, -2, 4]  # 6
nums = [2, -5, -2, -4, 3]  # 24
s = Solution()
print(s.maxProduct(nums))