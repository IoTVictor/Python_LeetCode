class Solution(object):
    def longestPalindromeSubseq(self, s):
        n = len(s)
        dp = [[0] * n for _ in range(n)]  # dp 数组全部初始化为 0
        # base case, 对角线必为1，i < j为0
        for i in range(n):
            dp[i][i] = 1
        # 从下往上遍历
        # 反着遍历保证正确的状态转移
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n, 1):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        # 整个 s 的最长回文子串长度
        return dp[0][n - 1]

S = Solution()
s = "bbbab"
print(S.longestPalindromeSubseq(s))