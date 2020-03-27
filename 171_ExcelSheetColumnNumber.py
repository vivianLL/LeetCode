'''
171. Excel Sheet Column Number
Easy

https://leetcode.com/problems/excel-sheet-column-number/
Given a column title as appear in an Excel sheet, return its corresponding column number.
'''
class Solution:
    def titleToNumber(self, s: str) -> int:
        n = len(s)
        ss = 0
        for i in range(n):
            # print(s[i])
            ss += (26 ** (n - i - 1)) * (ord(s[i]) - ord("A") + 1)
        return ss

        # 一行代码
        # return sum([(ord(s[i]) - 64) * 26 ** (len(s) - 1 - i) for i in range(len(s))])

        # 另一种写法
        # res = 0
        # for c in map(ord, s):
        #     res = res * 26 + c - 64
        # return res


sol = Solution()
ans = sol.titleToNumber("AB")
print(ans)
# 例如：BAA = 2 * 26 ^ 2 + 1 * 26 ^ 1 + 1 * 26 ^ 0