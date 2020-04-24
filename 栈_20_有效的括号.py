class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pattern_map = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c not in pattern_map:  # 如果左括号，压栈
                stack.append(c)
            elif stack == [] or pattern_map[c] != stack.pop():  # 如果右括号，先看栈是否为空，再看是否匹配
                return False
        return not stack  # 判断最终栈是否为空

s1 = '([)]'
s2 = '{[]}'
s = Solution()
print(s.isValid(s1))
print(s.isValid(s2))