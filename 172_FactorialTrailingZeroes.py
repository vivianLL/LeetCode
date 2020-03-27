'''
172. Factorial Trailing Zeroes
Easy

https://leetcode.com/problems/factorial-trailing-zeroes/
Given an integer n, return the number of trailing zeroes in n!.
'''
import math
class Solution:
    def trailingZeroes(self, n: int) -> int:
        # # 暴力求阶乘法 超时
        # num = 1
        # for i in range(2,n+1):
        #     num *= i
        # print(num)
        # strnum = str(num)
        # return len(strnum)-len(strnum.strip('0'))

        # # 我的方法的改进 依然超时
        # if n==0:         # 0的阶乘是1
        #     return 0
        # count = 0
        # for i in range(2,n+1):
        #     while i>0:
        #         if i%5==0:    # 尾数是5
        #             count += 1
        #             i /= 5
        #         else:
        #             break
        # return count

        # 继续改进
        count = 0
        while n > 0:
            count += n//5
            n = n//5
        return count

sol = Solution()
ans = sol.trailingZeroes(40)
print(ans)

# 思路：10由2*5构成，含有5的因子比含有2的因子出现的少，因此只需找到有多少个5。
# 注意25可以分解为5*5,125可以分解为5*5*5···要对接下来的这部分情况进行统计，
# 我们可以对n取25的商，即n//25，这样就找到了包含有2个5的数（且因为是对5×5取商，没有重复计入），依此类推，可以循环对n取5, 25, 125...的商，将所有的情况都包括，最终将所有的商汇总即0的个数。
# n // 25 == n // 5 // 5，因此可以对n循环取5的商，其效果是一样的。