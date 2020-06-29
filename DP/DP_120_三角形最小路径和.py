class Solution(object):
    # Modify the original triangle, bottom-up
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        return triangle[0][0]

    # bottom-up, O(n) space
    def minimumTotal2(self, triangle):
        if not triangle:
            return
        res = triangle[-1]  # 转一维res = list(triangle[-1])
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                res[j] = min(res[j], res[j + 1]) + triangle[i][j]
        return res[0]
s = Solution()
triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
print(s.minimumTotal(triangle))
triangle2 = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
print(s.minimumTotal2(triangle2))