# coding:utf-8
'''
191. Number of 1 Bits

https://leetcode.com/problems/number-of-1-bits/
Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).
'''


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # # 内置函数
        # num = bin(n)  # 十进制转二进制 0b1011
        # num = str(num).split('b')[-1]
        # i = 0
        # count = 0
        # while i != len(num):
        #     if num[i]=='1':
        #         count=count+1
        #     i=i+1
        # return count

        # 常规解法
        count, bit = 0, 1
        while n:
            if bit & n:
                count += 1
                n -= bit
            bit = bit << 1
        return count

        # # 快速算法
        # count = 0
        # while n:
        #     print("iter %d: %d" % (count, n))
        #     count += 1
        #     n = n & (n - 1)
        # return count

sol = Solution()
ans = sol.hammingWeight(11111111111111111111111111111101)
print(ans)

# 注：常规解法和快速算法输出的结果有时和LeetCode上的不一样，如11111111111111111111111111111101
