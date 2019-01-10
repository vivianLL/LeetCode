'''
7. Reverse Integer
https://leetcode.com/problems/reverse-integer/
Given a 32-bit signed integer, reverse digits of an integer.
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 转换成字符串 切片倒置 runtime:108ms
        if str(x)[0]!='-':
            rev = int(str(x)[::-1])
        else:
            rev = 0-int(str(x).split('-')[-1][::-1])
        if rev>(2**31-1) or rev<(-2)**31:
            return 0
        else:
            return rev

        # # 方法2：转换成列表 reverse倒置
        # list_x = list(str(abs(x)))
        # list_x.reverse()
        #
        # rev = int(''.join(list_x)) * (1, -1)[x < 0]
        # if rev>(2**31-1) or rev<(-2)**31:
        #     return 0
        # else:
        #     return rev


sol = Solution()
ans = sol.reverse(-123)
print(ans)
ans = sol.reverse(120)
print(ans)
ans = sol.reverse(1534236469)
print(ans)
ans = sol.reverse(9646324351)
print(ans)
ans = sol.reverse(7463847421)
print(ans)

# 注意负号和结果溢出