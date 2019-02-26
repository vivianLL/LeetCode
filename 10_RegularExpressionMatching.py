'''
10. Regular Expression Matching

https://leetcode.com/problems/regular-expression-matching/
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).
Note:
s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
'''
import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 正则匹配
        return re.match('^' + p + '$', s) != None  # ^匹配字符串的开头 $匹配字符串的末尾 +匹配1个或多个的表达式。

        # # 递归写法
        # # s已被匹配且p已耗完
        # if not s and not p:  # not比len()==0和s==[]或s==""更简便
        #     return True
        # # p已耗完但s未被完全匹配
        # if len(s) > 0 and len(p) == 0:  # 或if not p
        #     return False
        #
        # # 如果模式第二个字符是*
        # if len(p) > 1 and p[1] == '*':
        #     if len(s) > 0 and (s[0] == p[0] or p[0] == '.'):
        #         # 如果第一个字符匹配，三种可能1、模式后移两位；2、字符串移1位
        #         return self.isMatch(s, p[2:]) or self.isMatch(s[1:], p)
        #     else:
        #         # 如果第一个字符不匹配，模式往后移2位，相当于忽略x*
        #         return self.isMatch(s, p[2:])
        # # 如果模式第二个字符不是*
        # if len(s) > 0 and (s[0] == p[0] or p[0] == '.'):
        #     return self.isMatch(s[1:], p[1:])
        # else:
        #     return False


        # # 递归简化写法
        # if p == "":
        #     return s == ""
        # if len(p) > 1 and p[1] == "*":
        #     return self.isMatch(s, p[2:]) or (s and (s[0] == p[0] or p[0] == '.') and self.isMatch(s[1:], p))
        # else:
        #     return s and (s[0] == p[0] or p[0] == '.') and self.isMatch(s[1:], p[1:])

        # 动态规划
        dp = [[False for j in range(len(p) + 1)] for i in range(len(s) + 1)]  # 初始化二维表dp
        print(dp)
        dp[0][0] = True  # s 和 p 都为空时
        #  若 s 为空时
        for j in range(1, len(p) + 1):
            # dp[0][j]= (p[j-1]=="*")and(j>=2)and(dp[0][j-2])            #  等同于下列语句
            if p[j - 1] == '*':
                if j >= 2:
                    dp[0][j] = dp[0][j - 2]
        print(dp)

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                #  j-1才为正常字符串中的索引
                #  p当前位置为"*"时，(代表空串--dp[i][j-2]、一个或者多个前一个字符--( dp[i-1][j] and (p[j-2]==s[i-1] or p[j-2]=='.'))
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2] or (
                                dp[i - 1][j] and (p[j - 2] == s[i - 1] or p[j - 2] == '.'))  # dp[i][j-1] or
                #  p当前位置为"."时或者与s相同时，传递dp[i-1][j-1]的真值
                else:
                    dp[i][j] = (p[j - 1] == '.' or p[j - 1] == s[i - 1]) and dp[i - 1][j - 1]

        return dp[len(s)][len(p)]


sol = Solution()
ans = sol.isMatch("aa","a*")
print(ans)
ans = sol.isMatch("aa",".*")
print(ans)
# 递归时注意判断s和p的长度，防止越界
