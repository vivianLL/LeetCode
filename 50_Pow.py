'''
50. Pow(x, n)
Medium

https://leetcode.com/problems/powx-n/
Implement pow(x, n), which calculates x raised to the power n (x^n).
Note:
-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−2^31, 2^31 − 1]
'''

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # # 常规做法 运行高次方时会超时
        # if n==0:
        #     if x==0:
        #         return False
        #     else:
        #         return 1
        # elif n>0:
        #     num = 1
        #     while n!=0:
        #         num = num*x
        #         n = n-1
        #     return num
        # else:
        #     num = 1
        #     while (-n) != 0:
        #         num = num * x
        #         n = n + 1
        #     return 1/num

        # # 递归法 将幂不断除2，除到奇数时减1继续除，使得程序复杂度控制在O(log n)里
        # if n < 0:
        #     return 1.0 / self.myPow(x, -n)  #或self.myPow(1 / x, -n)
        # if n == 0:
        #     return 1
        # if n == 2:
        #     return x * x
        # return self.myPow(self.myPow(x, n / 2), 2) if not n % 2 else x * self.myPow(self.myPow(x, n // 2), 2)

        # 按位运算 思路同上，为了消除递归使用了位运算及循环
        if n == 0:
            return 1
        elif n < 0:
            x = 1 / x
            n = -n
        ans = 1.0
        while n > 0:
            if n & 1:  # 判断奇偶性，0则为偶，1则为奇，与n%2效果一样，但n&1更快
                ans *= x
            x *= x
            n >>= 1 # 除以2
        return ans


sol = Solution()
num = sol.myPow(5,-2)
print(num)
num = sol.myPow(0.00001,2147483647)
print(num)

# 注意1：零和负数，0的0次方，0的倒数
# 注意2：递归法如果不设置则会报错：RecursionError: maximum recursion depth exceeded in comparison。
# 因为python默认的递归深度是很有限的（默认是1000），因此当递归深度超过999的样子，就会引发这样的一个异常。