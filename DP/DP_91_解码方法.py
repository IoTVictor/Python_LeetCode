class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 空串时，或字符串以 '0' 开头(非法), 则直接返回0
        if s == '' or s[0] == '0':
            return 0
        n = len(s)
        dp = [0 for _ in range(n+1)]  # dp[i] 表示以第i个数字结尾的解码方式有多少种，注意第i个数字的下标为i - 1
        dp[0] = 1  # 初始条件：空串1种方式解密，不能为0
        dp[1] = 1  # 长度1的s，1种方式解码
        for i in range(2, n+1):
            if '1' <= s[i-1] <= '9':
                dp[i] += dp[i-1]  # += 前i-1个数字解密的方式树
            if '10' <= s[i-2:i] <= '26':
                dp[i] += dp[i-2]  # += 前i-2个数字解密的方式树
        return dp[-1]
ss = '12'
s = Solution()
print(s.numDecodings(ss))





