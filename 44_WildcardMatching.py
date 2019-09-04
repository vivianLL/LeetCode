'''
44. Wildcard Matching
Hard

https://leetcode.com/problems/wildcard-matching/
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).
Note:
s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # # 动态规划
        # n = len(s)
        # m = len(p)
        # dp = [[False for _ in range(n+1)] for _ in range(m+1)]
        # dp[0][0] = True
        # # 当s为空时必须有*才可能满足匹配，并且他的真值一定和去掉*及其前面的符号相同
        # for j in range(1, m + 1):
        #     dp[j][0] = p[j - 1] == '*' and dp[j - 1][0]
        #
        # for i in range(1,n+1):
        #     for j in range(1,m+1):
        #         # 当 p上一个字符为'？'或者p上一个字符等于s上一个字符，则当前真值与上一位相同
        #         if p[j-1]=='?' or s[i-1]==p[j-1]:
        #             dp[j][i] = dp[j-1][i-1]
        #         # p上一个字符为'*'时，则*可表示p往后走一位或者s往后走一位
        #         elif p[j-1]=='*':
        #             dp[j][i] = dp[j-1][i] or dp[j][i-1]
        #
        # return dp[m][n]

        # # 动态规划的另一种写法
        # lp = len(p)
        #
        # ls = len(s)
        # dp = [[0] * (lp + 1) for i in range(ls + 1)]
        # dp[0][0] = 1
        # for i in range(lp):
        #     if p[i] == '*' and dp[0][i] == 1:
        #         dp[0][i + 1] = 1
        #
        # for i in range(ls):
        #     for j in range(lp):
        #         if p[j] == s[i] or p[j] == '?':
        #             dp[i + 1][j + 1] = dp[i][j]
        #         if p[j] == "*":
        #             dp[i + 1][j + 1] = dp[i + 1][j] or dp[i][j + 1] or dp[i][j]
        # return dp[ls][lp] == 1

        # 双指针 O(n)
        lenS, lenP, si, pi = len(s), len(p), 0, 0
        lastP, lastS = -1, -1
        while si < lenS:
            # 相等或p的位置 为?时，两个指针都向下移动；
            if pi < lenP and (s[si] == p[pi] or p[pi] == '?'):
                si += 1
                pi += 1
            # 不相等但是p的指针处是 * 时，记录此时pi（lastP）,si（lastS）的位置，si就是当前pi位置的 * 可以开始匹配的位置，同时pi下移；
            elif pi < lenP and p[pi] == '*':
                lastP, lastS = pi, si
                pi += 1
            # 不相等但是lastP有值说明有*时，说明lastS可以继续下移，当前字符接着匹配p中的 *,si下移，pi回到lastP+1的位置（代表 * 之后对应的字符位置）
            elif lastP != -1:
                lastS += 1
                pi = lastP + 1
                si = lastS
            # 不符合以上情况就false了
            else:
                return False
        # 最后在处理p后面可能的*，都对应空串就可以
        for i in range(pi, lenP):
            if p[i] != '*':
                return False
        return True


sol = Solution()
ans = sol.isMatch("acdcb", "a*c?b")
print(ans)
ans = sol.isMatch("adceb", "*a*b")
print(ans)
ans = sol.isMatch("cb", "?a")
print(ans)