class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        INF = float('inf')
        dp = [INF] * (n+1)  # dp[i]为字符串前i个字符s[0...i-1] 最少可以划分成 几个回文串

        if n == 0:
            return 0

        isPalin = self.calcPalin(s)  # 判断回文的二维数组,isPlain[i][j]表示s[i...j]是否是回文串

        dp[0] = 0
        for i in range(n+1):
            for j in range(i):
                if isPalin[j][i-1] == True:  # 表示s[j...i-1]是否是回文串
                    dp[i] = min(dp[i], dp[j]+1)


        return dp[n] - 1  # 返回符合要求的最少分割次数 = 几个回文串 - 1



    # 思想：生成回文串，中心扩展，O(n*n)
    def calcPalin(self, s):
        n = len(s)
        f = [[False]*n for _ in range(n)]

        # 从中心扩展两边
        # odd 奇数，从 中心字符 向两边扩展
        for c in range(n):
            i = j = c
            while i >= 0 and j <= n-1 and s[i] == s[j]:
                f[i][j] = True
                i -= 1
                j += 1
        # even 偶数，从 中心轴线 向两边扩展
        for c in range(n-1):  # 区别
            i = c
            j = c + 1
            while i >= 0 and j <= n-1 and s[i] == s[j]:
                f[i][j] = True
                i -= 1
                j += 1

        return f

s = 'aabbac'
S = Solution()
print(S.minCut(s))  # 返回切割次数，2




