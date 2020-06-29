class Solution(object):
    def maxSlidingWindow(self, num, size):
        if not num or size <= 0:
            return []
        deque = []  # 最终结果，每个窗口的最大值
        if len(num) >= size:
            index = []  # 存放可能为最大值的下标，两端开口的队列
            # 遍历第一个窗口
            for i in range(size):
                while len(index) > 0 and num[i] >= num[index[-1]]:
                    index.pop()  # 尾部删除
                index.append(i)
            # 遍历后续窗口
            for i in range(size, len(num)):
                deque.append(num[index[0]])
                while len(index) > 0 and num[i] >= num[index[-1]]:
                    index.pop()  # 尾部删除
                if len(index) > 0 and index[0] <= i-size:
                    index.pop(0)  # 头部删除：头部元素从窗口滑出
                index.append(i)  # 最后加入的数其坐标一定加入
            # print(index)
            deque.append(num[index[0]])
        return deque
num = [2, 3, 4, 2, 6, 2, 5, 1]
size = 3
s = Solution()
print(s.maxSlidingWindow(num, size))