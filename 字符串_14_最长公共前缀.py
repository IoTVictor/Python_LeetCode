class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # zip(*str) 将 str 中所有字符串并列到迭代器中，逐次并列返回 str 中所有字符串的第 1、2、3、…… 个字符
        # list(zip(*["abc","efg","jk"])) --例子输出-→ [('a', 'e', 'j'), ('b', 'f', 'k')] # 加*表示反向zip()
        res = ''
        for c in zip(*strs):
            if len(set(c)) == 1:
                res += c[0]
                # print(c)
            else:
                break  # 一旦出现第一个不同的字符，提前break

        return res


strs = ["flower", "flow", "flight"]
s = Solution()
print(s.longestCommonPrefix(strs))
