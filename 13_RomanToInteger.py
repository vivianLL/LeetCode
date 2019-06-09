'''
13. Roman to Integer
Easy

https://leetcode.com/problems/roman-to-integer/
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
'''
class Solution:
    def romanToInt(self, s: str) -> int:
        # # 自写代码 两个词典 有优先级
        # sum = 0
        # dic1 = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        # dic2 = {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        # i = 0
        # while i <len(s):
        #     if i<len(s)-1 and s[i]+s[i+1] in dic2:
        #         sum += dic2[s[i]+s[i+1]]
        #         i += 2
        #     elif s[i] in dic1:
        #         sum += dic1[s[i]]
        #         i += 1
        # return sum

        # 一个词典
        MAPPING = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        year, last = 0, 0
        for c in reversed(s):
            c = MAPPING[c]
            if c < last:
                year -= c
            else:
                year += c
            last = c
        return year

sol = Solution()
ans = sol.romanToInt("MCMXCIV")
print(ans)