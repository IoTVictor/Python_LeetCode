class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1 or n == 2:
            return n
        memo = [0 for i in range(n)]
        memo[0], memo[1] = 1, 2
        for i in range(2, n):
            memo[i] = memo[i-1] + memo[i-2]
        return memo[n-1]  # 下标n-1存的就是f(n)

s = Solution()
print(s.climbStairs(3))
