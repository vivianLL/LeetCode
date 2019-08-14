'''
12. Integer to Roman
Medium

https://leetcode.com/problems/integer-to-roman/
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.
'''
class Solution:
    def intToRoman(self, num: int) -> str:
        # # 条件判断 粗暴做法
        # ans = (num // 1000)*'M'
        # num = num % 1000
        # print(num, ans)
        #
        # if num // 100 == 9:
        #     ans += 'CM'
        #     num = num % 900
        # elif num // 100 >= 5:
        #     ans += 'D'
        #     num = num % 500
        #     ans += (num // 100) * 'C'
        #     num = num % 100
        # elif num // 100 == 4:
        #     ans += 'CD'
        #     num = num % 400
        # else:
        #     ans += (num // 100) * 'C'
        #     num = num % 100
        #
        # print(num, ans)
        #
        # if num // 100 == 10:
        #     ans += 'C'
        #     num = num % 100
        # elif num // 10 == 9:
        #     ans += 'XC'
        #     num = num % 90
        # elif num // 10 >= 5:
        #     ans += 'L'
        #     num = num % 50
        #     ans += (num // 10) * 'X'
        #     num = num % 10
        # elif num // 10 == 4:
        #     ans += 'XL'
        #     num = num % 40
        # else:
        #     ans += (num // 10) * 'X'
        #     num = num % 10
        #
        # print(num, ans)
        #
        # if num == 10:
        #     ans += 'X'
        # elif num == 9:
        #     ans += 'IX'
        #     num = num % 9
        # elif num >= 5:
        #     ans += 'V'+ (num % 5)* 'I'
        # elif num == 4:
        #     ans += 'IV'
        #     num = num % 4
        # else:
        #     ans += num * 'I'
        #
        # print(num, ans)
        # return ans

        # # 循环
        # values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        # numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        # ans = ''
        # for i in range(0, len(values)):
        #     while num >= values[i]:
        #         num -= values[i]
        #         ans += numerals[i]
        # return ans

        # 循环2
        M = ["", "M", "MM", "MMM"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return M[num // 1000] + C[(num % 1000) // 100] + X[(num % 100) // 10] + I[num % 10]


sol = Solution()
ans = sol.intToRoman(610)  # 4， 9， 1994， 58， 61， 60
print(ans)
# 注意4和9的处理