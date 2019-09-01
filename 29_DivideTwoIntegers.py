'''
29. Divide Two Integers
Medium

https://leetcode.com/problems/divide-two-integers/
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.
Return the quotient after dividing dividend by divisor.
The integer division should truncate toward zero.
Note:
Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.
'''
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # # 循环减法 超时 复杂度O(n)
        # count = 0
        # sor = divisor
        # dend = dividend
        #
        # if divisor==0:
        #     return None
        # if dividend>2**31-1 or dividend<-2**31 or divisor>2**31-1 or divisor<-2**31:
        #     return 2**31-1
        # if dividend==divisor:
        #     return 1
        # if dividend== -divisor:
        #     return -1
        # if divisor==1:
        #     return dividend
        # if divisor==-1:
        #     return -dividend
        # if divisor<0:
        #     sor = -divisor
        #
        # if dividend<0:
        #     dend = -dividend
        #
        # res = 1
        # while res > 0:
        #     res = dend - sor
        #     dend = res
        #     count += 1
        #     print(count,dend)
        # count -= 1
        #
        # if (dividend>0 and divisor<0) or (dividend<0 and divisor>0):
        #     count = -count
        # return count

        # # 二分查找 （AC不过）
        # if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
        #     if abs(dividend) < abs(divisor):
        #         return 0
        # sum = 0;
        # count = 0;
        # res = 0
        # a = abs(dividend);
        # b = abs(divisor)
        # while a >= b:
        #     sum = b
        #     count = 1
        #     while sum + sum <= a:
        #         sum += sum
        #         count += count
        #     a -= sum
        #     res += count
        # if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
        #     res = 0 - res
        # if res > 2 ** 31 - 1:
        #     return 2 ** 31 - 1
        # elif res < -2 ** 31:
        #     return -2 ** 31
        # else:
        #     return res
        # return res

        # # 模拟除法过程
        # ispositive = True
        # if dividend > 0 and divisor < 0:
        #     ispositive = False
        # if dividend < 0 and divisor > 0:
        #     ispositive = False
        # dividend = abs(dividend);
        # divisor = abs(divisor)
        # if dividend < divisor:
        #     return 0
        # num = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]
        # i = 9
        # newdividend = []
        # while i >= 0:
        #     tmp = 0
        #     while dividend >= num[i]:
        #         tmp += 1;
        #         dividend -= num[i]
        #     newdividend.append(tmp);
        #     i -= 1
        # tmpm = 0;
        # ans = 0;
        # i = 0
        # while i < 10:
        #     while tmpm < divisor:
        #         if i > 9:
        #             break
        #         j = 0;
        #         t = 0
        #         while j < 10 and tmpm != 0:
        #             t += tmpm;
        #             j += 1
        #         tmpm = t + newdividend[i];
        #         i += 1
        #         if tmpm < divisor:
        #             j = 0;
        #             t = 0
        #             while j < 10 and ans != 0:
        #                 t += ans;
        #                 j += 1
        #             ans = t
        #     if tmpm >= divisor:
        #         k = 0
        #         while tmpm >= divisor:
        #             tmpm -= divisor;
        #             k += 1
        #         j = 0;
        #         t = 0
        #         while j < 10 and ans != 0:
        #             t += ans;
        #             j += 1
        #         ans = t + k
        # if ispositive:
        #     if ans > 2147483647:
        #         return 2147483647
        #     return ans
        # if ans >= 2147483648:
        #     return -2147483648
        # return 0 - ans


        # 左移
        ispositive = True
        if dividend > 0 and divisor < 0:
            ispositive = False
        if dividend < 0 and divisor > 0:
            ispositive = False
        dividend = abs(dividend)
        divisor = abs(divisor)
        if dividend < divisor:
            return 0
        tmp = divisor
        ans = 1
        while dividend >= tmp:
            tmp <<= 1
            if tmp > dividend:
                break
            ans <<= 1
        tmp >>= 1
        nans = ans + self.divide(dividend - tmp, divisor)
        if ispositive:
            if ans > 2147483647:
                return 2147483647
            return nans
        if ans >= 2147483648:
            return -2147483648
        return 0 - nans

sol = Solution()
ans = sol.divide(-2147483648,-1)
print(ans)
# 思路：
# ①模拟除法的过程，从高位开始除，不够先右挪一位。这种方法首先要将每一位的数字都先拿出来，由于最大int类型，所以输入的长度不超过12位。接下来就是模拟除法的过程。
# ②利用左移操作来实现除法过程。将一个数左移等于将一个数×2，取一个tmp = divisor，所以将除数tmp不断左移，直到其大于被除数dividend，然后得到dividend - tmp，重复这个过程。