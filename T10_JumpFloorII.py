# -*- coding:utf-8 -*-
'''
剑指offer面试题10扩展 牛客网[编程题]变态跳台阶
https://www.nowcoder.com/practice/22243d016f6b47f2a6928b4313c85387?tpId=13&tqId=11162&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
'''

class Solution:
    def jumpFloorII(self, number):
        # 解法一：套公式f(n)=2^(n-1)
        # return 2 ** (number - 1)

        # 解法二：迭代f(n)=2*f(n-1)，自顶向下的递归
        jump = 0
        if number == 1:
            jump = jump + 1
        else:
            jump = jump + 2 * self.jumpFloorII(number - 1)
        return jump

        # 其他解法，如自底向上的循环等，复杂度比迭代低


sol = Solution()
ans = sol.jumpFloorII(6)
print(ans)

# 思路：因为n级台阶，第一步有n种跳法：跳1级、跳2级、到跳n级
# 跳1级，剩下n-1级，则剩下跳法是f(n-1)
# 跳2级，剩下n-2级，则剩下跳法是f(n-2)
# 所以f(n)=f(n-1)+f(n-2)+…+f(1)
# 因为f(n-1)=f(n-2)+f(n-3)+…+f(1)
# 所以f(n)=2*f(n-1)，即为等比数列，又因为f(1)=1,所以f(n)=2^(n-1)