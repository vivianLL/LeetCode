'''
28. Implement strStr()

https://leetcode.com/problems/implement-strstr/
Implement strStr().
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # # 库函数
        # return haystack.find(needle)

        # 扫描haystack，当遇到与needle首字符相同的位置时，检查haystack从该位置开始的与needle长度相同的块，与needle是否相同
        # if not needle:
        #     return 0
        # for i in range(len(haystack) - len(needle) + 1):  # 不用range到len(haystack),防止越界，因为与needle首字符相同的位置一定在len(haystack) - len(needle) + 1前。
        #     if haystack[i] == needle[0]:
        #         j = 1
        #         while j < len(needle) and haystack[i + j] == needle[j]: # 判断有几个连续的字符相等
        #             j += 1
        #         if j == len(needle):  # 判断相等字符的个数是否等于needle长度
        #             return i
        # return -1

        # 利用类似substring的方法简化上面的代码
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:  # 直接判断字符串相等，因为haystack[0:0]为空，等于空字符串，所以包含了needle为空的特殊情况
                return i
        return -1

        # # KMP算法。该算法对于任何模式和目标序列，都可以在线性时间内完成匹配查找（O(n+m)），而不会发生退化（原理不懂）
        # if not needle:
        #     return 0
        #     # generate next array, need O(n) time
        # i, j, m, n = -1, 0, len(haystack), len(needle)
        # next = [-1] * n
        # while j < n - 1:
        #     # needle[k] stands for prefix, neelde[j] stands for postfix
        #     if i == -1 or needle[i] == needle[j]:
        #         i, j = i + 1, j + 1
        #         next[j] = i
        #     else:
        #         i = next[i]
        # # check through the haystack using next, need O(m) time
        # i = j = 0
        # while i < m and j < n:
        #     if j == -1 or haystack[i] == needle[j]:
        #         i, j = i + 1, j + 1
        #     else:
        #         j = next[j]
        # if j == n:
        #     return i - j
        # return -1



sol = Solution()
ans = sol.strStr("hello","ll")
print(ans)
ans = sol.strStr("aaaaa","bba")
print(ans)
ans = sol.strStr("a","")
print(ans)
ans = sol.strStr("aaa","aaaaaa")
print(ans)
ans = sol.strStr("bbaa","aab")
print(ans)

# 注意：needle为空、用相等字符个数判断返回条件，比用flag=True更方便
# 参考网址：https://blog.csdn.net/coder_orz/article/details/51708389