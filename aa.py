class Solution:
    def findseq(self, N, L):
        if N < 3:
            return []
        small = 1
        big = 2
        mid = (N + 1) // 2
        curN = small + big
        res = []
        while small < mid:
            if curN == N:
                seq = list(range(small, big + 1))
                seqlen = len(seq)
                if seqlen >= L:
                    res.append(seq)
                    big += 1
                    curN += big
            elif curN > N:
                curN -= small
                small += 1
            else:
                big += 1
                curN += big

        return res[-1]
s = Solution()
print(s.findseq(15, 2))
print(s.findseq(100, 5))