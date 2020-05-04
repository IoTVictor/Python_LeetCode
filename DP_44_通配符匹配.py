class Solution(object):
    def isMatch(self, s, p):
        """
        '?' 可以匹配任何单个字符
        '*' 可以匹配任意字符串（包括空字符串）
        """
        n = len(s)
        m = len(p)
        f = [[False] * (m + 1) for i in range(n + 1)]
        f[0][0] = True

        if n == 0 and p.count('*') == m:
            return True

        for i in range(0, n + 1):
            for j in range(0, m + 1):
                if i > 0 and j > 0:
                    f[i][j] |= f[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] in ['?', '*'])

                if i > 0 and j > 0:
                    f[i][j] |= f[i - 1][j] and p[j - 1] == '*'

                if j > 0:
                    f[i][j] |= f[i][j - 1] and p[j - 1] == '*'

        return f[n][m]
S = Solution()
s = "adceb"
p = "*a*b"
print(S.isMatch(s, p))  # true
