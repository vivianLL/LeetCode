'''
387. First Unique Character in a String
Easy

https://leetcode.com/problems/first-unique-character-in-a-string/
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
'''
import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # 建立哈希表，扫描两次
        # strcount = {}
        # for i in range(len(s)):
        #     if s[i] not in strcount:
        #         strcount[s[i]] = 1
        #     else:
        #         strcount[s[i]] += 1
        # print(strcount)              # 以上也可以用strcount = collections.Counter(s)替代  # 为hashable对象计数，是字典的子类
        #
        # for i,str in enumerate(strcount):   # enumerate将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标
        #     if strcount[str]==1:
        #         print(str)
        #         return s.index(str)   # 不可在此处break然后将return放在最外面，以防字符串中只有重复字符时str为最后一个索引
        # return -1

        # 参考答案
        count = collections.Counter(s)
        # find the index
        index = 0
        for ch in s:
            if count[ch] == 1:
                return index
            else:
                index += 1
        return -1

sol = Solution()
ans = sol.firstUniqChar("loveleetcode")
print(ans)
ans = sol.firstUniqChar("lll")
print(ans)
ans = sol.firstUniqChar("")
print(ans)