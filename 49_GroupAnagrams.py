'''
49. Group Anagrams
Medium

https://leetcode.com/problems/group-anagrams/
Given an array of strings, group anagrams together.
Note:
All inputs will be in lowercase.
The order of your output does not matter.
'''
import collections
class Solution:
    def groupAnagrams(self, strs):
        # # 按已排序的字符串进行分类 时间复杂度O(NKlogK) 空间复杂度O(NK)
        # ans = {}
        # for s in strs:
        #     if tuple(sorted(s)) in ans:       # 注意dict的key不能为list或set
        #         ans[tuple(sorted(s))].append(s)
        #     else:
        #         ans[tuple(sorted(s))]= [s]
        # return list(ans.values())

        # # 上述方法等价于：
        # ans = collections.defaultdict(list)   # 对于不存在的key, d[key] 也有一个默认值，这个默认值是int()的默认值0
        # for s in strs:
        #     ans[tuple(sorted(s))].append(s)
        # return list(ans.values())

        # 通过count排序 即用一个大小为26的int数组来统计每个单词中字符出现的次数，然后将int数组转为一个唯一的字符串，跟字符串数组进行映射
        # 时间空间复杂度 O(NK)
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1   # 返回对应的 ASCII 数值，或者 Unicode 数值
            ans[tuple(count)].append(s)
        return ans.values()

sol = Solution()
ans = sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(ans)