'''
231. Power of Two
Easy

https://leetcode.com/problems/power-of-two/
Given an integer, write a function to determine if it is a power of two.
'''
import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # if n==1 or n==2:
        #     return True  # 1是2的零次幂
        # while n>1:
        #     n = n/2
        #     print(n)
        #     if n==2:
        #         return True
        # return False

        # 更快版本
        if n <= 0:
            return False
        while n % 2 == 0:  # multiple of 2
            n /= 2
        return n == 1

sol = Solution()
ans = sol.isPowerOfTwo(218)
print(ans)