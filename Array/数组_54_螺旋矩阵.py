class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        if matrix == []:
            return matrix
        rows = len(matrix)
        columns = len(matrix[0])
        # 偏移量
        dx = (0, 1, 0, -1)  # row index's change in 4 directions，[右、下、左、上]
        dy = (1, 0, -1, 0)  # column index's change in 4 directions，[右、下、左、上]

        res = []  # 结果一维维列表
        visited = [[-1 for _ in range(columns)] for _ in range(rows)]  # 标记矩阵，访问过就置为1
        # flattenMatrix = [n for row in matrix for n in row]  # Matrix二维转一维

        x = 0
        y = 0
        d = 0
        for i in range(rows * columns):  # 一共就rows*columns个数
            res.append(matrix[x][y])
            visited[x][y] = 1
            # 移动
            nx = x + dx[d]
            ny = y + dy[d]
            # 如果超出边界，或者格子已经被访问
            if nx < 0 or nx >= rows or ny < 0 or ny >= columns or visited[nx][ny] != -1:
                d = (d + 1) % 4
                nx = x + dx[d]
                ny = y + dy[d]

            # 更新坐标
            x = nx
            y = ny

        return res

matrix = [[1,  2,  3,  4],
          [5,  6,  7,  8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]
matrix2 = [[1], [2], [3], [4], [5]]
matrix3 = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
s = Solution()
print(s.spiralOrder(matrix))
print(s.spiralOrder(matrix3))