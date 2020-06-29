class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        # flowerbed = [0] + flowerbed +[0]
        # i = 1
        # count = 0
        # while i <= len(flowerbed)-1:
        #     if flowerbed[i-1:i+2] == [0, 0, 0]:
        #         count += 1
        #         i += 2
        #     else:
        #         i += 1
        # return n <= count
        i = 0
        count = 0
        while i < len(flowerbed):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                count += 1
            i += 1
        return count >= n
