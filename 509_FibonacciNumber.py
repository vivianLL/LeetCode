'''
509. Fibonacci Number
https://leetcode.com/problems/fibonacci-number/
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
F(0) = 0,   F(1) = 1,   F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).
'''
import math

class Solution:
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        # # 解法一：简单递归 时间复杂度：O(2^N) 第n个数要执行1+2+4+8+…+2^(n−2)次
        # if N == 0:
        #     return 0
        # if N == 1:
        #     return 1
        # if N > 1:
        #     return self.fib(N-1)+self.fib(N-2)

        # 解法一变形：递归 空间换时间 先求解子问题并存起来
        fib=[]
        if N == 0:
            fib[0]=0
            return 0
        if N == 1:
            fib[1]=1
            return 1
        if N > 1:
            for i in range(3,N):
                fib[i] = fib[i-1]+fib[i-2]
            return fib[N]

        # # 解法二：使用通项公式 缺点为使用了浮点数，但是浮点数精度有限，当oj中n不大时可以通过，但实测当 N>71 时出现错误
        # return int(5**(-0.5)*(((1+5**(0.5))/2)**N-((1-5**(0.5))/2)**N))

        # # 解法三：循环，每次循环给这两个数重新赋值 O(N)
        # if N == 0 or N == 1:
        #     return N
        # fbn1 = 0
        # fbn2 = 1
        # for i in range(1, N):
        #     tmp = fbn1 + fbn2;
        #     fbn1 = fbn2;
        #     fbn2 = tmp;
        # return fbn2

        # # 解法四：矩阵法 思路详见《剑指offer》
        # def multi(a, b):  # 计算二阶矩阵的相乘
        #     c = [[0, 0], [0, 0]]  # 定义一个空的二阶矩阵
        #     for i in range(2):
        #         for j in range(2):
        #             for k in range(2):  # 新二阶矩阵的值计算
        #                 c[i][j] = c[i][j] + a[i][k] * b[k][j]
        #     return c
        #
        # base = [[1, 1], [1, 0]]  # 元矩阵，这里可以把元矩阵看做是2**0=1
        # ans = [[1, 0], [0, 1]]  # 结果矩阵  最开始的结果矩阵也可以看做是1，因为这个矩阵和任意二阶A矩阵相乘结果都是A
        # while N:
        #     if N & 1:  # 取n的二进制的最后一位和1做与运算，如果最后一位是1，则进入if体内部
        #         ans = multi(ans, base)  # 如果在该位置n的二进制为1，则计算ans和base矩阵
        #     base = multi(base, base)  # base矩阵相乘，相当于初始base矩阵的幂*2
        #     N >>= 1  # n的二进制往右移一位
        # return ans[0][1]  # 最后获取到的二阶矩阵的[0][1]即f(n)的值


        # # 解法五：升级递归算法 F(2n−1)=Fn^2+F(n−1)^2;F(2n)=(2F(n−1)+Fn)⋅Fn，推导详见 http://blog.zhengyi.one/fibonacci-in-logn.html
        # if N == 0:
        #     return 0
        # if N == 1:
        #     return 1
        # k = (N + 1) / 2 if N % 2 else N / 2
        # fib_k = self.fib(k)
        # fib_k_1 = self.fib(k - 1)
        # return fib_k ** 2 + fib_k_1 ** 2 if N % 2 else (2 * fib_k_1 + fib_k) * fib_k


sol = Solution()
ans = sol.fib(7)
print(ans)
