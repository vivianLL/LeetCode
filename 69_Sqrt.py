'''
69. Sqrt(x)
Easy

Implement int sqrt(int x).
Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
'''
import math
class Solution:
    def mySqrt(self, x):
        # # 二分查找 关键在于结果的向下取整
        # if x == 1:
        #     return 1
        # l = 1
        # h = x // 2
        # while h > l:
        #     m = (l + h) // 2
        #     if m ** 2 > x:
        #         h = m - 1
        #     elif m ** 2 < x:
        #         l = m + 1
        #     else:
        #         return m
        # if h == l:
        #     if (h - 1) ** 2 < x < h ** 2:
        #         return h - 1
        #     else:
        #         return h
        # elif h < l:
        #     return h

        # if x == 0:
        #     return 0
        # l = 1
        # r = x
        #
        # while l <= x:
        #     res = (l + r) // 2
        #     s = res ** 2
        #
        #     if s <= x < (res + 1) ** 2:   # 在判断平方时可以优化 因为向下取整
        #         return res
        #     if s < x:
        #         l = res
        #     if s > x:
        #         r = res

        # 牛顿法
        # if x < 1e-6:
        #     return 0
        # last = x
        # c = x / 2
        # while math.fabs(c - last) > 1e-6:
        #     last = c
        #     c = (c + x / 2) / 2
        # return c

        lr = 1e-6  # lr是学习率和最小误差
        a = x / 2
        while (a * a - x) > lr:
            print(a)
            a -= lr
        return a


        # 自己写的 可以求浮点数的平方
        # if x==None or x<0:   # 不能用not x 因为x可以等于0
        #     return False
        # elif x==1 or x==0:
        #     return x
        # elif x<1:
        #     left = x
        #     right = 1
        #     while left < right:
        #         mid = (left+right)/2
        #         if abs(mid**2 - x)<0.00000001:
        #             return mid
        #         elif mid**2<x:
        #             left = mid
        #         else:
        #             right = mid
        # else:
        #     left = 1
        #     right = x
        #     while left < right:
        #         mid = (left+right)/2
        #         if abs(mid**2 - x)<0.00000001:
        #             return mid
        #         elif mid**2<x:
        #             left = mid
        #         else:
        #             right = mid


sol = Solution()
ans = sol.mySqrt(9)
print(ans)

# 牛顿法思路：f(x)=x2−a
# 所以f(x)的一次导是：
# f′(x)=2x
# 牛顿迭代式：
# xn+1 = xn-f(xn)/f'(xn) = xn-(xn^2-a)/2xn
# xn+1=1/2(xn+a/xn)
