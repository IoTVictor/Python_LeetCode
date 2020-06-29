class Solution:
    def isMatch(self, s, p):
        m = len(s)  # text
        n = len(p)  # pattern
        dp = [[False for i in range(0, n + 1)] for j in range(0, m + 1)]  # m*n
        dp[0][0] = True  # dp[0][0]初始化为true，由此开始转移
        # 特例：处理 m = 0，即s为空串
        for i in range(1, n + 1):
            if p[i - 1] == '*':
                dp[0][i] = dp[0][i - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2]  # 不要 x*, 去掉p串后两个字符
                    if s[i - 1] == p[j - 2] or p[j - 2] == '.':  # '*'不去匹配
                        dp[i][j] |= dp[i - 1][j]
                else:  # p[j - 1] != '*',是正常字符
                    if s[i - 1] == p[j - 1] or p[j - 1] == '.':  # 如果两字符相同或者为.
                        dp[i][j] = dp[i - 1][j - 1]  # 当前状态由前一个转移而来

        return dp[m][n]

# class Solution(object):
#     def isMatch(self, text, pattern):
#
#         memo = dict()  # 备忘录
#         def dp(i, j):
#             if (i, j) in memo:
#                 return memo[(i, j)]
#             if j == len(pattern):
#                 return i == len(text)
#
#             first = i < len(text) and pattern[j] in {text[i], '.'}
#
#             if j <= len(pattern) - 2 and pattern[j + 1] == '*':
#                 ans = dp(i, j + 2) or \
#                         first and dp(i + 1, j)
#             else:
#                 ans = first and dp(i + 1, j + 1)
#
#             memo[(i, j)] = ans
#             return ans
#
#         return dp(0, 0)

S = Solution()
s = 'aab'
p = 'c*a*b'
print(S.isMatch(s, p)) # True