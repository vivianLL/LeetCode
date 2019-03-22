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

        # 动态规划 n*n的二维矩阵用于存储f(i,j)的值.f(i,j)表示s[i:j]子串是否是回文串。当j-i<=1时，如果s[i] == s[j]则表示s[i:j]为回文串
        # f(i,j) = (s(i)==s(j)    , j-i<=1
        # f(i,j) = (s(i)==s(j) and f(i+1,j-1)    ,j-i>1
        k = len(s) # 计算字符串的长度
        matrix = [[0 for i in range(k)] for i in range(k)] # 初始化n*n的列表
        logestSubStr = ""  # 存储最长回文子串
        logestLen = 0      # 最长回文子串的长度

        for j in range(0, k):
            for i in range(0, j + 1):             # 之所以是j+1是因为i可以等于j
                if j - i <= 1:
                    if s[i] == s[j]:
                        matrix[i][j] = 1           # 此时f(i,j)置为true
                        if logestLen < j - i + 1:   # 将s[i:j]的长度与当前的回文子串的最长长度相比 
                            logestSubStr = s[i:j + 1]  # 取当前的最长回文子串
                            logestLen = j - i + 1  # 当前最长回文子串的长度
            else:
                if s[i] == s[j] and matrix[i + 1][j - 1]: # 判断
                    matrix[i][j] = 1
                    if logestLen < j - i + 1:
                        logestSubStr = s[i:j + 1]
                        logestLen = j - i + 1
        return logestSubStr



        # 动态规划 O(n)
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
