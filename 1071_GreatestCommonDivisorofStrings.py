'''
1071. Greatest Common Divisor of Strings
Easy

https://leetcode.com/problems/greatest-common-divisor-of-strings/
For strings S and T, we say "T divides S" if and only if S = T + ... + T  (T concatenated with itself 1 or more times)
Return the largest string X such that X divides str1 and X divides str2.
'''
import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # # 我的方法 先求最大公约数
        # if str1 == str2:
        #     return str1
        # if len(str1)>len(str2):
        #     str1, str2 = str2, str1
        #
        # m = len(str1)
        # n = len(str2)
        # while n%m != 0:
        #     x = n%m
        #     n = m
        #     m = x
        # gcd = m
        #
        # while gcd>0:
        #     # 或 if str1[: gcd] * (len(str1) // gcd) == str1 and str1[: gcd] * (len(str2) // gcd) == str2:
        #     if str1[:gcd] == str2[:gcd] and str1.count(str1[:gcd]) == len(str1)/gcd and str2.count(str2[:gcd]) == len(str2)/gcd:
        #         return str1[:gcd]
        #     else:
        #         return ""

        # 数学性质法：如果str1和str2拼接后等于str2和str1拼接起来的字符串（注意拼接顺序不同），那么一定存在符合条件的字符串X。
        if str1+str2 != str2+str1:
            return ""
        else:
            candidate_len = math.gcd(len(str1), len(str2))
            return str1[: candidate_len]

sol = Solution()
ans = sol.gcdOfStrings("ABCDEFABCDEFABCDEF", "ABCDEFABCDEFABCDEFABCDEF")
print(ans)
ans = sol.gcdOfStrings("ABCDEABCDE", "ABCDEABCDE")
print(ans)
# 符合要求的最长的字符串长度为str1和str2长度的最大公约数