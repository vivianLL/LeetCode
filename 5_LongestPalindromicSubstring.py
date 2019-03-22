'''
5. Longest Palindromic Substring
Medium

https://leetcode.com/problems/longest-palindromic-substring/
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # # 暴力法判断每个子字符串的逆序 时间复杂度O(n^3)
        # if not s or len(s) == 1: return s
        # maxlen = 1
        # maxstr = s[0]
        # for i in range(len(s) - 1):
        #     for j in range(i + 1, len(s)):
        #         if s[i:j + 1] == s[i:j + 1][::-1]:
        #             print(s[i:j + 1],i,j)
        #             length = j - i + 1
        #             if length > maxlen:
        #                 maxlen = length
        #                 maxstr = s[i:j + 1]
        # return maxstr

        # 动态规划
        n = len(s)
        maxl = 0
        start = 0
        for i in range(n):
            if i - maxl >= 1 and s[i - maxl - 1: i + 1] == s[i - maxl - 1: i + 1][::-1]:
                start = i - maxl - 1
                maxl += 2
                continue
            if i - maxl >= 0 and s[i - maxl: i + 1] == s[i - maxl: i + 1][::-1]:
                start = i - maxl
                maxl += 1
        return s[start: start + maxl]


sol = Solution()
ans = sol.longestPalindrome("babab")
print(ans)

# 基本思路是对任意字符串，如果头和尾相同，那么它的最长回文子串一定是去头去尾之后的部分的最长回文子串加上头和尾。
# 如果头和尾不同，那么它的最长回文子串是去头的部分的最长回文子串和去尾的部分的最长回文子串的较长的那一个。
# P[i,j]P[i,j]表示第i到第j个字符的回文子串数
# dp[i,i]=1
# dp[i,j]=dp[i+1,j−1]+2|s[i]=s[j]
# dp[i,j]=max(dp[i+1,j],dp[i,j−1])|s[i]!=s[j]

# 参考网址：https://blog.csdn.net/asd136912/article/details/78987624