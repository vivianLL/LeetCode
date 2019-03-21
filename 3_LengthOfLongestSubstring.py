'''
3. Longest Substring Without Repeating Characters
Medium

https://leetcode.com/problems/longest-substring-without-repeating-characters/
Given a string, find the length of the longest substring without repeating characters.
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # # 自写代码 二重循环 时间复杂度O(n^2)
        # output = ''
        # for i in range(len(s)):
        #     chset = set()           # 建立集合判断是否重复
        #     chstr = ''              # 对于每个起点重新设置空字符串
        #     for j in range(i,len(s)):
        #         if s[j] not in chset:
        #             chstr = chstr+s[j]
        #             chset.add(s[j])
        #             print(chset, chstr)
        #             if len(chstr)>len(output):    # 找最长的输出
        #                 output = chstr
        #             if len(chstr)==len(s):        # 如果该起点到终点的全部字符都不重复，则跳出循环，否则字符串无法置空
        #                 break
        #         else:
        #             if len(chstr)>len(output):    # 如果重复 则看当前字符串长度是否最长，然后跳出
        #                 output = chstr
        #             break
        #
        # print(output)
        # return len(output)


        # 剑指offer方法 动态规划 借助哈希查找key O(n)时间复杂度
        maxlen = 0
        start = 0
        dic = {}
        for i in range(len(s)):
            cur = s[i]
            if cur not in dic.keys():
                dic[cur] = i
            else:                   # 如果当前字符出现过，获取当前字符串c上次出现的位置 pre = dic[c]
                if dic[cur] + 1 > start:   # 注意此处为dic[cur]+1，如果pre在start后面即pre>start，则把start移动到pre的下一位，start = pre + 1，这样保证cur继续向后遍历中从start到cur没有重复元素，否则start不动，start移动到某一个位置，说明在这个位置之前有重复的元素了，所以start只往后移动不往回移动
                    start = dic[cur] + 1
                dic[cur] = i        # 字典里保留重复字符最后出现的位置
            if i - start + 1 > maxlen:   # 如果 cur - start + 1 (衡量当前没重复子串开头到结尾的长度) 比长度变量l大，那就替换l为  cur - start + 1
                maxlen = i - start + 1

        return maxlen

        # # 最快
        # if s == 0:
        #     return 0
        # maxlen = 0
        # indHash = {}
        # leftside = -1
        # ls = len(s)
        # for ind, ch in enumerate(s):
        #     if (ch in indHash) and (leftside < indHash[ch]):
        #         leftside = indHash[ch]
        #     currentlen = ind - leftside
        #     if currentlen > maxlen:
        #         maxlen = currentlen
        #     indHash[ch] = ind
        # currentlen = ls - leftside - 1
        # if currentlen > maxlen:
        #     maxlen = currentlen
        # return maxlen


sol = Solution()
# ans = sol.lengthOfLongestSubstring("bbbbb")
# print(ans)
# ans = sol.lengthOfLongestSubstring("pwwkew")
# print(ans)
# ans = sol.lengthOfLongestSubstring("abcabcbb")  # 3
# print(ans)
# ans = sol.lengthOfLongestSubstring("abc")
# print(ans)
# ans = sol.lengthOfLongestSubstring("aab")
# print(ans)
# ans = sol.lengthOfLongestSubstring("b")
# print(ans)
# ans = sol.lengthOfLongestSubstring("")
# print(ans)
ans = sol.lengthOfLongestSubstring("arabcacfr")
print(ans)

# 思路：动态规划 第i个字符为结尾的最长不重复子字符串长度为f(i)
# 若第i个字符之前没出现过，则f(i)=f(i-1)+1
# 若第i个字符之前出现过：
# 若第i个字符和它上次出现的位置的距离d小于等于f(i-1)（即i-dic[cur] <= i-1-start+1，即dic[cur] + 1 > start），则第i个字符串上次出现在f(i-1)对应的最长子字符串中，因此f(i)=d         (如i==2,s[i]=='a')
# 即，f(i) = d = i - start + 1 = i - (dic[cur] + 1)+1 = i - dic[cur]   (dic[cur]为上次i出现的值)
# 若第i个字符和它上次出现的位置的距离d大于f(i-1)，则第i个字符串上次出现在f(i-1)对应的最长子字符串之前，因此f(i)=f(i-1)+1    (如i==8,s[i]=='r')
#