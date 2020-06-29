class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        # 通用：n行，m列
        if n == 0:
            return
        m = n  # 列数
        # 偏移量
        dx = (0, 1, 0, -1)  # row index's change in 4 directions，[右、下、左、上]
        dy = (1, 0, -1, 0)  # column index's change in 4 directions，[右、下、左、上]

        # res = []  # 结果矩阵：二维列表
        # for i in range(n):
        #     res.append(list())
        #     for j in range(n):
        #         res[i].append(-1)
        res = [[-1 for _ in range(m)] for _ in range(n)]  # 不能写'-1'

        x = 0
        y = 0
        d = 0
        for k in range(1, n*m+1):  # # k 从 1 到 n*n
            res[x][y] = k
            # 移动
            nx = x + dx[d]
            ny = y + dy[d]
            # 如果超出边界，或者格子已经被访问
            if nx < 0 or nx >= n or ny < 0 or ny >= m or res[nx][ny] != -1:
                d = (d + 1) % 4
                nx = x + dx[d]
                ny = y + dy[d]

            # 更新坐标
            x = nx
            y = ny

        return res
n = 3
s = Solution()
print(s.generateMatrix(n))