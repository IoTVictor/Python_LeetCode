class Solution(object):
    # 法一：通用解法
    # def maxProduct(self, nums):
    #     if nums is None:
    #         return 0
    #     dp = [[0 for _ in range(2)] for _ in range(2)]  # 只需保存前一次的结果，所以只需要2*2数组
    #     # 保存最大值dp[x][0]，负最大值（即最小值）dp[x][1]
    #     dp[0][1], dp[0][0], res = nums[0], nums[0], nums[0]
    #     for i in range(1, len(nums)):
    #         x, y = i % 2, (i-1) % 2  # 滚动数组，交替保存，x当前，y前一个状态
    #         dp[x][0] = max(dp[y][0] * nums[i], dp[y][1] * nums[i], nums[i])  # 存最大值
    #         dp[x][1] = min(dp[y][0] * nums[i], dp[y][1] * nums[i], nums[i])  # 存最小值
    #         res = max(res, dp[x][0])
    #     return res

    # 法二：可读性好，通用性差（只适用于本题）
    def maxProduct(self, nums):
        if nums is None:
            return 0
        res, curMax, curMin = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            curMax, curMin = curMax * num, curMin * num
            curMax, curMin = max(curMax, curMin, num), min(curMax, curMin, num)
            res = max(curMax, res)

        return res

    #  法三：与法二原理一样
    # def maxProduct(self, nums):
    #     if not nums:
    #         return None
    #
    #     global_max = prev_max = prev_min = nums[0]
    #     for num in nums[1:]:
    #         if num > 0:
    #             curt_max = max(num, prev_max * num)  # 当前最大
    #             curt_min = min(num, prev_min * num)  # 当前最小
    #         else:
    #             curt_max = max(num, prev_min * num)  # min * 负数
    #             curt_min = min(num, prev_max * num)  # max * 负数
    #
    #         global_max = max(global_max, curt_max)
    #         prev_max, prev_min = curt_max, curt_min
    #
    #     return global_max

#nums = [2, 3, -2, 4]  # 6
nums = [2, -5, -2, -4, 3]  # 24
s = Solution()
print(s.maxProduct(nums))