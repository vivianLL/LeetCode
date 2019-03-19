'''
233. Number of Digit One
Hard

https://leetcode.com/problems/number-of-digit-one/
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.
'''
class Solution:
    def countDigitOne(self, n: int) -> int:
        # # 简单法 超时 时间复杂度O(n∗log10(n)) 空间复杂度O(log10(n))
        # num = 0
        # for i in range(n + 1):
        #     num += str(i).count('1')
        # return num

        # # 一般法 超时
        # count = 0
        # for i in range(1,n+1):
        #     c = 0
        #     while i:
        #         if i%10==1:
        #             c += 1
        #         i = i//10
        #     count += c
        # return count

        # 寻找数字规律
        if n<1 or n==None:
            return 0
        count = 0
        base = 1        # 每一位权值
        round = n
        while round>0:
            weight = round % 10    # 该位的位值
            round = round // 10    # 该位从0-9变化的次数，即比该位高的数
            count += round*base
            if weight == 1:
                count += 1+(n%base) # n%base即该位之前（比该位低）的数
            elif weight > 1:
                count += base
            base *= 10
        return count



sol = Solution()
ans = sol.countDigitOne(21345)
print(ans)
ans = sol.countDigitOne(824883294)
print(ans)

# 参考网址：https://blog.csdn.net/yi_afly/article/details/52012593