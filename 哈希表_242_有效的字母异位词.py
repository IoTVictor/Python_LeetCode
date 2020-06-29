# class Solution(object):
#     def isAnagram(self, s, t):
#         # map : 底层哈希表
#         dict1 = {}
#         dict2 = {}
#         for item in s:
#             dict1[item] = dict1.get(item, 0) + 1  # dict.get(key, default=None) 如果key的value不存在，返回default
#         for item in t:
#             dict2[item] = dict2.get(item, 0) + 1
#         return dict1 == dict2

class Solution(object):
    def isAnagram(self, s, t):
        # 手工构建哈希表
        dict1 = [0]*26
        dict2 = [0]*26
        for item in s:
            dict1[ord(item) - ord('a')] += 1  # 自定义哈希算法，ord()返回对应的 ASCII 数值
        for item in t:
            dict2[ord(item) - ord('a')] += 1
        return dict1 == dict2
# 法二：排序
# class Solution(object):
#     def isAnagram(self, s, t):
#         return sorted(s) == sorted(t)

S = Solution()
s = "anagram"
t = "nagaram"
print(S.isAnagram(s, t))
