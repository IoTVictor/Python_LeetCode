class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 二进制转换十进制,加上LeetCode反而不通过（未解？？？）
        # n = str(n)
        # n = int(n, 2)

        count = 0
        # 如果为负数，用补码表示
        if n < 0:
            n = n & 0xffffffff
        while n:
            count += 1
            n = (n - 1) & n  # 原整数先减去1，再与原整数做“与&”，相当于把最右边的1变成0

        return count

#n = 5
#n = 101

#n = 0b00000000000000000000000000001011
#n = 11111111111111111111111111111101  # dp不能通过，需要一个大数组，开辟时会造成memoryError
s = Solution()
print(s.hammingWeight(n))  # 4：100， 5:101