'''
14. Longest Common Prefix
Easy

https://leetcode.com/problems/longest-common-prefix/
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
'''


class Solution:
    def longestCommonPrefix(self, strs):
        # # 垂直扫描 两重循环 比较单个字符
        # if strs==[] or '' in strs:
        #     return ''
        # if len(set(strs))==1:
        #     return strs[0]
        # j = 0
        # maxlen = min(len(x) for x in strs)
        # while j<maxlen:
        #     i = 0
        #     temp = strs[i][j]
        #     while i < len(strs)-1:
        #         if strs[i+1][j] == temp:
        #             i += 1
        #         else:
        #             return strs[0][:j]
        #
        #     j += 1
        # return strs[0][:j]
        #
        # # 比较字符子串&设立flag 较快
        # if len(strs) == 0 or '' in strs:
        #     return ''
        # if len(set(strs)) == 1:
        #     return strs[0]
        # maxlen = min([len(e) for e in strs])
        # check = 1
        # i = 0
        # while (check != 0 & i < maxlen):
        #     sub = [e[:i] for e in strs]
        #     if len(set(sub)) == 1:
        #         i += 1
        #     else:
        #         check = 0
        # return strs[0][:i - 1]

        # 最快
        res = ""
        if len(strs) == 0:
            return ""
        for each in zip(*strs):  # zip()函数用于将可迭代对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表
            if len(set(each)) == 1:  # 利用集合创建一个无序不重复元素集
                res += each[0]
            else:
                return res
        return res


sol = Solution()
ans = sol.longestCommonPrefix(["fog"]) # ["flower","flow","flight"]
print(ans)
ans = sol.longestCommonPrefix(["dog","racecar","car"])
print(ans)

# 其他方法：水平扫描、分治、二分搜索、字典树 详见LeetCode Solution