class Solution(object):
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            # 法一
            # # odd case, like "aba"
            # tmp = self.helper(s, i, i)
            # if len(tmp) > len(res):
            #     res = tmp
            # # even case, like "abba"
            # tmp = self.helper(s, i, i + 1)
            # if len(tmp) > len(res):
            #     res = tmp

            # 法二：简单写法
            res = max(self.helper(s, i, i), self.helper(s, i, i + 1), res, key=len)
        return res

    # get the longest palindrome, l, r are the middle indexes
    # from inner to outer
    def helper(self, s, l, r):
        # while循环由于l或r超出范围而停止，或者因为s[l] != s[r]
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        # print(l, r)
        return s[l + 1:r]  # 最长的回文既不属于s[l]也s[r]不能成为其一部分，辅助函数返回s[l+1:r]（左侧包括且右侧排除）

S = Solution()
s = 'babad'
print(S.longestPalindrome(s))